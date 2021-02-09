FROM python:3.5.3


# Install app dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


EXPOSE 5000
EXPOSE 3000
CMD python3 /backend/create_db
CMD python3 /backend/server.py
CMD python3 /frontend/app.py
