FROM python:3.6
RUN apt-get -y update \
    && apt-get -y install gcc python3-dev musl-dev \
    && apt-get -y install nginx
RUN pip install mysqlclient  
WORKDIR /app
RUN rm /etc/nginx/sites-enabled/default
COPY . .
COPY site.conf /etc/nginx/sites-enabled/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 80
CMD service nginx start  && gunicorn --config gunicorn_config.py app.app:app

