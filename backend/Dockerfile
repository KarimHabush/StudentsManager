FROM python:3.6

COPY db_connection.py /backend
COPY validation.py /backend

EXPOSE 5000

WORKDIR /backend

COPY requirements.txt /backend
RUN pip install -r requirements.txt

COPY server.py /app
CMD python server.py