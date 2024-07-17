# User-Order Microservices

## Overview

This project consists of two microservices: `user-service` and `order-service`, which interact with each other using
gRPC. The `user-service` manages user information, while the `order-service` manages order information and communicates
with `user-service` to validate user existence.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/YaroslavKumpan/user-order-microservices.git
    cd user-order-microservices
    ```


2. Start the services using Docker Compose:

    ```bash
    docker-compose up --build
    ```

## Usage

- `user-service` will be available on port `50051`.
- `order-service` will be available on port `50052`.

You can use gRPC clients like [BloomRPC](https://github.com/uw-labs/bloomrpc) to interact with the services.

## Endpoints

### User Service

- `CreateUser(UserRequest) returns (UserResponse)`
- `GetUser(UserId) returns (UserResponse)`
- `UpdateUser(UserRequest) returns (UserResponse)`

### Order Service

- `CreateOrder(OrderRequest) returns (OrderResponse)`
- `GetOrder(OrderId) returns (OrderResponse)`
- `UpdateOrder(OrderRequest) returns (OrderResponse)`

## License

This project is licensed under the MIT License.
