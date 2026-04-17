FROM ubuntu:22.04

# system deps
RUN apt-get update && apt-get install -y \
    build-essential m4 git python3 python3-dev python3-distutils \
    gfortran libssl-dev libffi-dev libgmp-dev libmpfr-dev libmpc-dev \
    libblas-dev liblapack-dev libboost-all-dev \
    wget ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# install Sage from source
WORKDIR /opt
RUN wget https://mirrors.mit.edu/sage/src/sage-10.4.tar.gz && \
    tar xzf sage-10.4.tar.gz && \
    rm sage-10.4.tar.gz

WORKDIR /opt/sage-10.4
RUN make -j$(nproc)

# install full Cremona DB
RUN ./sage -i database_cremona_ellcurve

# install Python deps for ACSC
RUN ./sage -python -m pip install \
    numpy pandas tqdm scikit-learn gudhi ripser

# workspace
WORKDIR /workspace

# expose Jupyter
EXPOSE 8888

CMD ["./sage", "-python", "-m", "jupyterlab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
