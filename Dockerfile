FROM python:3

WORKDIR /

# environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# apt-get update
RUN apt-get update

# psycog2 dependencies
RUN apt-get -y install libpq-dev python-dev
RUN pip install psycopg2

# dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

# copy project and set workdir
COPY . /
WORKDIR /hyde