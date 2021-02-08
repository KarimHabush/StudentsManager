FROM python:2.7.16


# Install app dependencies
#RUN pip install -r requirements.txt


EXPOSE 5000
CMD python /backend/create_db
CMD python /backend/server.py
