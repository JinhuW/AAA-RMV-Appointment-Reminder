FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip \
    pip install beautifulsoup4 \
    pip install requests \
    pip install load_dotenv

COPY . .

CMD [ "python", "./app.py" ]
