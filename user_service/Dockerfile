FROM python:3.11-slim

WORKDIR /app


RUN pip install poetry grpcio-tools


COPY . .


RUN poetry install --no-dev


RUN python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./proto/*.proto



ENV PYTHONPATH=/app/proto


CMD ["poetry", "run", "python", "app/grpc_server.py"]