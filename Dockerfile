FROM python:3.7.4-alpine3.10

COPY api /api
COPY migrations /migrations
COPY run.py flask-migrate.py requirements.txt ./

WORKDIR /

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

CMD ["gunicorn", "-b 0.0.0.0:5000", "api:create_api()"]

