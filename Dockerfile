FROM quay.io/astronomer/astro-runtime:6.0.3-base as stage1

LABEL maintainer="Astronomer <humans@astronomer.io>"
ARG BUILD_NUMBER=-1
LABEL io.astronomer.docker=true
LABEL io.astronomer.docker.build.number=$BUILD_NUMBER
LABEL io.astronomer.docker.airflow.onbuild=true
# Install OS-Level packages
COPY packages.txt .
RUN apt-get update && cat packages.txt | xargs apt-get install -y

FROM stage1 AS stage2
USER root
RUN apt-get -y install git python3 openssh-client \
    && mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
# Install Python packages
COPY requirements.txt .
RUN --mount=type=ssh,id=github pip install --no-cache-dir -q -r requirements.txt

FROM stage1 AS stage3
# Copy requirements directory
COPY --from=stage2 /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=stage2 /usr/local/bin /home/astro/.local/bin
ENV PATH="/home/astro/.local/bin:$PATH"

COPY . .