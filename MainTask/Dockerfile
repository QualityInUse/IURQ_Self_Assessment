FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r MainTask/requirements.txt

COPY . .

CMD ["python", "main.py"]

