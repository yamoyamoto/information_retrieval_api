FROM python:3.9

RUN apt-get update && \
  apt-get install -y curl git man unzip vim wget sudo file sqlite3

RUN python -m pip install mecab-python3 ipadic pytest google-api-python-client gunicorn

COPY . /code
WORKDIR /code

RUN python -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV DB_PATH="/code/ir_db.db"
ENV FORWARDED_ALLOW_IPS="*"
ENV PYTHONPATH "/code/"

RUN python ./setup.py && python ./app/scripts/add_document.py && python ./app/scripts/seed.py

RUN adduser myuser
USER myuser

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80", "--forwarded-allow-ips", "*"]