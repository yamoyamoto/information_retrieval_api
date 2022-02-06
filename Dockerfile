FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update && \
  apt-get install -y curl git man unzip vim wget sudo file sqlite3
#   apt-get install -y mecab libmecab-dev

# RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git && \
#   cd mecab-ipadic-neologd && \
#   bin/install-mecab-ipadic-neologd -y

RUN python -m pip install mecab-python3 ipadic sqlalchemy pytest

COPY . /app/
WORKDIR /app/app

ENV DB_PATH="/app/ir_db.db"

RUN python /app/setup.py && python /app/scripts/seed.py

CMD uvicorn main:app --host 0.0.0.0 --port $PORT --reload