FROM python:3.14

WORKDIR /app

COPY . .

RUN echo "Docker Build Successful"

CMD ["python", "--version"]