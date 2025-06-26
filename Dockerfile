# 1. Python 3.10 bazasini yuklaymiz
FROM python:3.10-slim

# 2. Loyihamiz uchun ishchi papka
WORKDIR /app

# 3. Kompyuterdan barcha fayllarni konteynerga nusxalaymiz
COPY . /app

# 4. Flaskni o‘rnatamiz
RUN pip install flask

# 5. Flask serverga port ochamiz
EXPOSE 5000

# 6. Saytni ishga tushiramiz
CMD ["python3", "app.py"]
