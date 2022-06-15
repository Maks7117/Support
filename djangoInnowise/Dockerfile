FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/djangoInnowise

#RUN apk update \
 #   && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /

COPY . /usr/src/djangoInnowise

ENTRYPOINT ["/entrypoint.sh" ]


EXPOSE 8000


