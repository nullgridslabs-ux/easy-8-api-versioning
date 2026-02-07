FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
ENV FLAG=CTF{easy_api_version_bug}
EXPOSE 5000
CMD ["python","app.py"]
