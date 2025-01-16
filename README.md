# FastAPI Backend

## Giới thiệu

Đây là dự án backend sử dụng FastAPI, SQLModel, PostgreSQL và Docker.

## Cài đặt và chạy dự án

### 1. Cài đặt các phụ thuộc

Sử dụng [Poetry](https://python-poetry.org/) để cài đặt các phụ thuộc:

```sh
poetry install
```

### 2. Tạo file .env

### 3. Chạy PostGreQSL bằng Docker
Chạy lệnh sau để khởi động dịch vụ PostgreSQL:
```sh
docker-compose up -d
```

### 4. Khởi tạo cơ sở dữ liệu
Chạy lệnh sau để tạo các bảng trong cơ sở dữ liệu:
```sh
alembic upgrade head
```

### 5. Chạy ứng dụng FastAPI
Chạy trong môi trường ảo
```sh
poetry shell
```

Chạy backend:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```