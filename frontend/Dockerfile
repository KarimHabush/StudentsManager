
FROM python:3.5.3

ADD requirements.txt /
ADD app.py / 
ADD templates /
ADD static/stylesheets /



# Install app dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt


EXPOSE 3000
CMD python3 app.py
