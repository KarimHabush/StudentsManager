FROM python:3.5.3

ADD requirements.txt /
ADD create_db.py /
ADD server.py /
ADD db_connection.py /
ADD validation.py /
ADD backend/__pycache__ /


# Install app dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt


EXPOSE 5000
CMD python3 create_db.py
CMD python3 server.py