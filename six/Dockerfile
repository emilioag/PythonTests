FROM python:3

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD jwtauthexample /jwtauthexample

ADD docker_entrypoint.sh /bin/entrypoint

EXPOSE 8000

ENTRYPOINT ["/bin/entrypoint"]