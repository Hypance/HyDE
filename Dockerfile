FROM python:3.9-alpine3.16

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install python and postgres dependencies under a virtual package
RUN apk update
RUN apk add git
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev musl-dev
RUN pip install --upgrade pip -r requirements.txt

# Delete virtual packages as we installed our dependencies
RUN apk del .tmp-build-deps

# Copy and set our project folder from local to container
RUN mkdir /hyde_project
WORKDIR /hyde_project
COPY ./ /hyde_project
