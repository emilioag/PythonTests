FROM python:3

ADD . /gdrive

RUN pip install -e /gdrive

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENTRYPOINT ["gdrive"]