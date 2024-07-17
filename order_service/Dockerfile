FROM python:3.11-slim

WORKDIR /app

# Установите Poetry и необходимые зависимости
RUN pip install poetry grpcio-tools

# Копируем файлы проекта
COPY . .

# Установите зависимости проекта с помощью Poetry
RUN poetry install --no-dev

# Генерация protobuf файлов
RUN python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./proto/*.proto

# Установите PYTHONPATH
ENV PYTHONPATH=/app/proto

# Запустите основной скрипт
CMD ["poetry", "run", "python", "app/grpc_server.py"]
