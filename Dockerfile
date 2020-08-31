FROM python:3.8.1-alpine3.11

ENV PYTHONUNBUFFERED=1 COLUMNS=200

ADD ./src/requirements.txt /src/

RUN sed -i "s/dl-cdn.alpinelinux.org/mirror.neolabs.kz/g" \
    /etc/apk/repositories \
    && apk update \
    && apk --no-cache add bash postgresql-dev binutils gdal-dev geos-dev \
    && apk add bash \
# Add build dependencies
    && apk --no-cache add --virtual .build-deps \
    tzdata libffi-dev gcc g++ curl-dev libressl-dev \
    musl-dev python3-dev make \
# Upgrade pip
    && pip install --upgrade pip \
# Add project dependencies
    && pip install --no-cache-dir -Ur /src/requirements.txt \
# Remove build dependencies
    && apk del .build-deps

COPY ./src /src

WORKDIR /src
CMD ["./entrypoint.sh"]
