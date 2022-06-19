FROM python:3.8

COPY requirements.txt .

RUN pip install -U pip && pip install  -r requirements.txt

COPY / /

WORKDIR /

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "$PORT"]