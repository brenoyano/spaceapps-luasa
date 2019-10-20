FROM python

COPY code /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /code