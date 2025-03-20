FROM alpine:3.14

WORKDIR /app

RUN apk add --no-cache python3 py3-pip ffmpeg

RUN ln -s /usr/bin/python3 /usr/bin/python

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]