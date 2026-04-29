# docker/Dockerfile (recommended)
FROM mambaorg/micromamba:1.4.0

ARG USER=star
ARG UID=1000
ARG CONDA_ENV=star-env
ARG PYTHON_VERSION=3.10

ENV PATH=/opt/conda/bin:$PATH
ENV MAMBA_DOCKERFILE_ACTIVATE=1
SHELL ["/bin/bash", "-lc"]

# Install minimal system deps needed for conda packages and pip wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    curl \
    git \
    build-essential \
    cmake \
    pkg-config \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Create conda env with Python 3.10 and install TDA libs from conda-forge
# Use micromamba to create env and install binary packages
RUN micromamba create -y -n ${CONDA_ENV} python=${PYTHON_VERSION} -c conda-forge \
    numpy scipy pandas \
    gudhi=3.5.1 ripser=0.6.2 persim=0.6.0 \
    && micromamba clean --all --yes

# Activate env for subsequent RUNs
ENV CONDA_DEFAULT_ENV=${CONDA_ENV}
ENV CONDA_PREFIX=/opt/conda/envs/${CONDA_ENV}
ENV PATH=${CONDA_PREFIX}/bin:${PATH}

# Create non-root user
RUN useradd -m -u ${UID} ${USER}
WORKDIR /home/${USER}/app
COPY --chown=${USER}:${USER} . /home/${USER}/app

USER ${USER}

# Install package in editable mode with dev and tda extras using the same interpreter
RUN python -m pip install --upgrade pip setuptools wheel \
 && python -m pip install --no-cache-dir -e ".[dev,tda]"

ENV PYTHONPATH=/home/${USER}/app:$PYTHONPATH
WORKDIR /home/${USER}/app

# Default command for quick verification
CMD ["bash", "-lc", "python -c \"import sys, gudhi, ripser; print('py', sys.version.split()[0], 'gudhi', gudhi.__version__, 'ripser', ripser.__version__)\""]
