FROM python:latest

ADD bot.py .
ADD .env .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./bot.py"]
