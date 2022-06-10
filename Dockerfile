FROM python:3.4.0

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

ADD pmysql /pmysql/
WORKDIR /pmysql/
CMD python /pmysql/main.py