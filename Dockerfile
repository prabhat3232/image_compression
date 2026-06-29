FROM python:3.11-slim AS builder

ARG MOZJPEG_VERSION=4.1.5

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    nasm \
    curl \
    ca-certificates \
    libpng-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/build \
    && curl -fsSL "https://github.com/mozilla/mozjpeg/archive/v${MOZJPEG_VERSION}.tar.gz" \
    | tar -zxf - -C /root/build \
    && cd "/root/build/mozjpeg-${MOZJPEG_VERSION}" \
    && cmake -DCMAKE_INSTALL_PREFIX=/opt/mozjpeg -DENABLE_STATIC=0 -DWITH_ARITH_ENC=1 -DWITH_ARITH_DEC=1 . \
    && make -j"$(nproc)" install/strip \
    && rm -rf /root/build

ENV LD_LIBRARY_PATH=/opt/mozjpeg/lib64:/opt/mozjpeg/lib
ENV PKG_CONFIG_PATH=/opt/mozjpeg/lib64/pkgconfig:/opt/mozjpeg/lib/pkgconfig

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --no-binary=Pillow -r requirements.txt

FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    libheif1 \
    libavif-dev \
    libwebp7 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/mozjpeg /opt/mozjpeg
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

ENV LD_LIBRARY_PATH=/opt/mozjpeg/lib64:/opt/mozjpeg/lib

WORKDIR /app

COPY . .

RUN mkdir -p uploads static

EXPOSE 3000

CMD ["python", "filecompress.py"]
