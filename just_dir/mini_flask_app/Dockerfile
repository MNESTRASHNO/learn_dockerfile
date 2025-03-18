FROM python:3.9-slim

WORKDIR /opt/app

COPY . .

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

CMD [ "python3", "app.py" ]
