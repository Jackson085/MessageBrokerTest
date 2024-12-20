FROM python:3.9-slim

ARG PORT
WORKDIR /app

RUN mkdir "Commons"
COPY Commons /app/Commons

RUN mkdir "Domain"
COPY Domain /app/Domain

RUN mkdir "Docker"
COPY Docker /app/Docker

RUN mkdir "Remote"
COPY Remote /app/Remote

RUN mkdir "wwwroot"
COPY wwwroot /app/wwwroot

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE $Port

CMD ["python", "-u", "-m", "Docker.entrypoint"]
