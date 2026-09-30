FROM python:3.12-slim

RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

WORKDIR /app

RUN pip install --no-cache-dir Flask

USER nyu

COPY --chown=nyu:nyu . .

EXPOSE 8080

CMD [ "python", "./run.py" ]