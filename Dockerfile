FROM python:3.9

RUN apt-get update && \
  apt-get install -y curl git man unzip vim wget sudo file sqlite3

RUN python -m pip install mecab-python3 ipadic pytest google-api-python-client gunicorn

COPY . /code
WORKDIR /code

RUN python -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV DB_PATH="/code/ir_db.db"
ENV PYTHONPATH "/code/"

RUN python /code/setup.py && python /code/app/scripts/add_document.py && python /code/app/scripts/seed.py

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port $PORT --forwarded-allow-ips '*'