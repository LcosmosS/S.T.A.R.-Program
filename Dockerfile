FROM sagemath/sagemath:latest
USER root

# install build tools required by the installer
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential make wget ca-certificates git curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# run the installer (may take time)
RUN sage -i --verbose database_cremona_ellcurve

# clone John Cremona repos (optional)
RUN git clone https://github.com/JohnCremona/eclib.git /opt/eclib || true && \
    git clone https://github.com/JohnCremona/ecdata.git /opt/ecdata || true

# python deps
RUN sage -python -m pip install --no-cache-dir numpy pandas tqdm scikit-learn gudhi ripser

WORKDIR /workspace
VOLUME ["/workspace"]
EXPOSE 8888
CMD ["bash", "-lc", "sage -python -m jupyterlab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='acsc2026'"]
