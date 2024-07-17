from concurrent import futures

import grpc

from grpc_client import get_user
from database import get_db

from models import Order
from order_service.proto import order_pb2_grpc


class OrderService(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        user = get_user(request.user_id)
        if user is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")

        db = next(get_db())
        order = Order(
            name=request.name,
            description=request.description,
            user_id=request.user_id,
        )
        db.add(order)
        db.commit()
        db.refresh(order)
        return order_pb2.OrderResponse(
            id=order.id,
            name=order.name,
            description=order.description,
            user_id=order.user_id,
        )

    def GetOrder(self, request, context):
        db = next(get_db())
        order = db.query(Order).filter(Order.id == request.id).first()
        if order is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")
        return order_pb2.OrderResponse(
            id=order.id,
            name=order.name,
            description=order.description,
            user_id=order.user_id,
        )

    def UpdateOrder(self, request, context):
        db = next(get_db())
        order = db.query(Order).filter(Order.id == request.id).first()
        if order is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")

        order.name = request.name
        order.description = request.description
        order.user_id = request.user_id
        db.commit()
        db.refresh(order)
        return order_pb2.OrderResponse(
            id=order.id,
            name=order.name,
            description=order.description,
            user_id=order.user_id,
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
