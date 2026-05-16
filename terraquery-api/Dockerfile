FROM rust:1.86 AS builder

WORKDIR /app

COPY terraquery-api/Cargo.toml ./Cargo.toml
COPY terraquery-api/src ./src

RUN cargo build --release

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    unzip \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir "laspy[lazrs]" numpy scipy

RUN mkdir -p /opt/potreeconverter \
    && curl -L -o /tmp/PotreeConverter.zip \
      https://github.com/potree/PotreeConverter/releases/download/2.1.1/PotreeConverter_2.1.1_x64_linux.zip \
    && unzip /tmp/PotreeConverter.zip -d /opt/potreeconverter \
    && chmod +x /opt/potreeconverter/PotreeConverter_linux_x64/PotreeConverter \
    && rm /tmp/PotreeConverter.zip

ENV LD_LIBRARY_PATH=/opt/potreeconverter/PotreeConverter_linux_x64

COPY terraquery-api/scripts /app/scripts
COPY --from=builder /app/target/release/terraquery-api /usr/local/bin/terraquery-api

EXPOSE 8080

CMD ["terraquery-api"]