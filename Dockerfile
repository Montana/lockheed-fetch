FROM python:3.9-slim
WORKDIR /
COPY . .
RUN pip install requests
CMD ["python", "./lomar-fetch.py"]
