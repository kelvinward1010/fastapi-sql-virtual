### Bước 1: Cài đặt môi trường
pip install poetry
mkdir fastapi_project
cd fastapi_project
poetry init --no-interaction

### Bước 2: Cài đặt các gói cần thiết
poetry add fastapi uvicorn sqlalchemy asyncpg alembic

### Bước 3: Khởi tạo Alembic
poetry run alembic init src/alembic

### Bước 4: Tạo cấu hình và tệp cần thiết
### Tạo các tệp config.py, database.py, models.py, main.py, crud.py, schemas.py trong thư mục src/app
### Chỉnh sửa alembic.ini và src/alembic/env.py như đã hướng dẫn ở trên

### Bước 5: Khởi động PostgreSQL bằng Docker
docker-compose up -d

### Bước 6: Vào môi trường Poetry
poetry shell

### Bước 7: Chạy ứng dụng
uvicorn src.app.main:app --reload

### Bước 8: Khởi tạo và áp dụng migration với Alembic
alembic revision -m "create users table"
alembic upgrade head
