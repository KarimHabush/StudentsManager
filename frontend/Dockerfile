FROM python:3.6

EXPOSE 3000

WORKDIR /frontend

COPY requirements.txt /frontend
RUN pip install -r requirements.txt

COPY app.py /frontend
CMD python app.py