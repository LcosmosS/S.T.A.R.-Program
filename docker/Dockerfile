FROM sagemath/sagemath:latest

# Switch to root so we can modify system files
USER root

# Disable tzdata prompts system-wide
RUN apt-get update && \
    echo 'tzdata tzdata/Areas select America' | debconf-set-selections && \
    echo 'tzdata tzdata/Zones/America select New_York' | debconf-set-selections && \
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure tzdata

# Install system dependencies
RUN apt-get install -y git python3-pip && apt-get clean

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copy project
WORKDIR /workspace
COPY . /workspace
