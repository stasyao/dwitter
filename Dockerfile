FROM python:3.9-alpine 
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /dwitter
COPY requirements.txt .
RUN apk update && apk add --no-cache --virtual \
                    .build-deps \
                    ca-certificates \
                    gcc \
                    nano \
                    postgresql-dev \
                    python3-dev \
                    linux-headers \
                    musl-dev \
                    libffi-dev \
                    jpeg-dev \
                    zlib-dev \
                    && pip install -r /dwitter/requirements.txt

COPY . .

ENTRYPOINT sh ./entrypoint.sh
