# Use the latest stable version of Debian as the base image
FROM debian:stable-slim

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies required to build Python from source
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libncurses5-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libgdbm-dev \
        libdb5.3-dev \
        libbz2-dev \
        libexpat1-dev \
        liblzma-dev \
        tk-dev \
        ca-certificates \
        curl \
        xz-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and install Python 3.10
RUN wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz && \
    tar xzf Python-3.10.13.tgz && \
    cd Python-3.10.13 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.10.13* 

# Set Python 3.10 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.10 1 && \
    update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.10 1

# Set the working directory in the container
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Set the default command to run your Python code
# CMD ["python3", "your_script.py"]
