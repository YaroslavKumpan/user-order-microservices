from concurrent import futures
import grpc

import user_pb2
import user_pb2_grpc
from models import User
from database import SessionLocal

class UserService(user_pb2_grpc.UserServiceServicer):

    def AddUser(self, request, context):
        db = SessionLocal()
        user = User(
            id=request.id,
            name=request.name,
            email=request.email,
            age=request.age,
        )
        db.add(user)
        db.commit()
        db.close()
        return user_pb2.UserResponse(success=True, message="User added successfully")

    def GetUser(self, request, context):
        db = SessionLocal()
        user = db.query(User).filter(User.id == request.id).first()
        db.close()
        if user:
            return user_pb2.User(
                id=user.id, name=user.name, email=user.email, age=user.age
            )
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")

    def UpdateUser(self, request, context):
        db = SessionLocal()
        user = db.query(User).filter(User.id == request.id).first()
        if user:
            user.name = request.name
            user.email = request.email
            user.age = request.age
            db.commit()
            db.close()
            return user_pb2.UserResponse(
                success=True, message="User updated successfully"
            )
        else:
            db.close()
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
