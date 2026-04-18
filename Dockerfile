# Dockerfile — sagemath base, copy ecdata cremona files into Sage DB
FROM sagemath/sagemath:latest

USER root

# install tools needed for cloning and copying
RUN apt-get update && apt-get install -y --no-install-recommends \
    git wget ca-certificates tar && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# clone John Cremona repos
RUN git clone https://github.com/JohnCremona/ecdata.git /opt/ecdata || true
RUN git clone https://github.com/JohnCremona/eclib.git /opt/eclib || true

# If ecdata contains a 'cremona' directory or a tarball, copy/extract it into Sage DB
# Try common possibilities: a directory /opt/ecdata/cremona or a tarball /opt/ecdata/cremona.tar.gz
RUN mkdir -p /usr/local/share/sage/databases && \
    if [ -d /opt/ecdata/cremona ]; then \
        cp -a /opt/ecdata/cremona /usr/local/share/sage/databases/cremona; \
    elif [ -f /opt/ecdata/cremona.tar.gz ]; then \
        tar -xzf /opt/ecdata/cremona.tar.gz -C /usr/local/share/sage/databases; \
    else \
        echo "No cremona dir or tarball found in ecdata; installer fallback may be required"; \
    fi && \
    chmod -R a+rX /usr/local/share/sage/databases/cremona || true

# install eclib into Sage's python if it provides a package (best-effort)
RUN sage -python -m pip install --no-cache-dir /opt/eclib || true

# project Python deps (adjust as needed)
RUN sage -python -m pip install --no-cache-dir numpy pandas tqdm scikit-learn gudhi ripser || true

WORKDIR /workspace
VOLUME ["/workspace"]
EXPOSE 8888

CMD ["bash", "-lc", "sage -python -m jupyterlab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='acsc2026'"]
