import os

import grpc
from dotenv import load_dotenv

import user_pb2_grpc, user_pb2

load_dotenv()

USER_SERVICE_HOST = os.getenv("GRPC_USER_SERVICE_HOST")
USER_SERVICE_PORT = os.getenv("GRPC_USER_SERVICE_PORT")

if not USER_SERVICE_HOST or not USER_SERVICE_PORT:
    raise ValueError(
        "GRPC_USER_SERVICE_HOST or GRPC_USER_SERVICE_PORT environment variable is not set"
    )


def get_user(user_id):
    with grpc.insecure_channel(f"{USER_SERVICE_HOST}:{USER_SERVICE_PORT}") as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        try:
            response = stub.GetUser(user_pb2.UserId(id=user_id))
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            else:
                raise
