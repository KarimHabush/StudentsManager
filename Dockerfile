FROM python:3.5.3

ADD requirements.txt /
ADD backend/create_db.py /
ADD backend/server.py /
ADD frontend/app.py / 


# Install app dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt


EXPOSE 5000
EXPOSE 3000
CMD python3 /backend/server.py


