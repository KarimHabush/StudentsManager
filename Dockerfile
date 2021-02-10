FROM ubuntu:14.04.3
RUN apt-get update && apt-get install -y mysql-server

# Ensure we won't bind to localhost only
RUN grep -v bind-address /etc/mysql/my.cnf > temp.txt \
  && mv temp.txt /etc/mysql/my.cnf

# It doesn't seem needed since I'll use -p, but it can't hurt
EXPOSE 3306

CMD /etc/init.d/mysql start

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
CMD python3 app.py
CMD python3 server.py
