FROM python:3.6
ADD requirements.txt /eorzea/requirements.txt
WORKDIR /eorzea
RUN pip install -r requirements.txt
