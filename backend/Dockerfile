FROM python:3.5.3

ADD requirements.txt /
ADD server.py /
ADD db_connection.py /
ADD validation.py /


# Install app dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt


EXPOSE 5000
CMD python3 server.py
