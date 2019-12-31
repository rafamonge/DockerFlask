FROM ubuntu:18.10

LABEL MAINTAINER  rafa

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.7-dev && \
    apt-get install -y iputils-ping 

RUN apt-get install -y libldap2-dev libsasl2-dev ldap-utils 

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

EXPOSE 5000

CMD [ "app/app.py" ]