
FROM python:3.5.3

ADD requirements.txt /
ADD backend/create_db.py /
ADD backend/server.py /
ADD frontend/app.py / 
ADD backend/db_connection.py /
ADD backend/validation.py /
ADD backend/__pycache__ /
ADD frontend/templates /
ADD frontend/static/stylesheets /



# Install app dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt


EXPOSE 5000
EXPOSE 3000
CMD python3 create_db.py
CMD python3 app.py
CMD python3 server.py
