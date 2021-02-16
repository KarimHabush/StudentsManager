FROM python:3.6

COPY db_connection.py /
COPY validation.py /

EXPOSE 5000

WORKDIR /

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY server.py /app
CMD python server.py