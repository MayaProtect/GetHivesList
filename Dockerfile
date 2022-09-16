FROM python:3.10-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV MONGO_HOST=localhost
ENV MONGO_PORT=27017

EXPOSE 8080

CMD python show_all_lists.py
