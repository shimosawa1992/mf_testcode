FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY main.py .
COPY db.py .
COPY transactions.py .
RUN pip install mysqlclient

RUN pip install debugpy
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install sqlalchemy

CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8888", "--forwarded-allow-ips", "*"]