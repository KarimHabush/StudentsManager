FROM python:2.7.16


# Install app dependencies
#RUN pip install -r requirements.txt


EXPOSE 8080
CMD [ "python", "backend/server.py"]