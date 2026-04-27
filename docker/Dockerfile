FROM sagemath/sagemath:latest

# Disable tzdata prompts system-wide
RUN echo 'tzdata tzdata/Areas select America' | debconf-set-selections && \
    echo 'tzdata tzdata/Zones/America select New_York' | debconf-set-selections && \
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Install system dependencies you need
RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copy your project into the container
WORKDIR /workspace
COPY . /workspace

