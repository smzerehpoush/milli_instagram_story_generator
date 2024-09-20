FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt  .
COPY 11.png .
COPY 17.png .
COPY YekanBakh-VF.ttf .
COPY YekanBakhFaNum-SemiBold.woff2 .

RUN pip install -r requirements.txt && rm requirements.txt

COPY script.py .

CMD [ "python", "-u", "script.py" ]