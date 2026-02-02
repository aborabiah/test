FROM tiangolo/uwsgi-nginx-flask:python3.12
RUN pip install prometheus_client
ENV LISTEN_PORT=8000
EXPOSE 8000
COPY ./app /app 
WORKDIR /app
EXPOSE 8000
