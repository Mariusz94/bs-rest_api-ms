FROM python:3.8-slim
ARG GITHUB_RUN_NUMBER

RUN apt update && apt install tzdata -y
ENV TZ="Europe/Warsaw"

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY app/ .

CMD ["python", "-u", "server.py"]
