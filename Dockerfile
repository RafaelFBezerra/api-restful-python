FROM python:3.11-slim

WORKDIR /app

COPY . /app 

RUN apt-get update && \
    apt-get install -y --no-install-recommends make apt-transport-https ca-certificates curl gnupg && \
    \
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | \
    gpg --dearmor -o /usr/share/keyrings/doppler-cli-archive-keyring.gpg && \
    \
    echo "deb [signed-by=/usr/share/keyrings/doppler-cli-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | \
    tee /etc/apt/sources.list.d/doppler-cli.list && \
    \
    apt-get update && \
    apt-get install -y --no-install-recommends doppler && \
    \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r src/requirements.txt 

EXPOSE 8000

CMD ["sh", "-c", "PYTHONPATH=$PYTHONPATH:/app/src gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000"]