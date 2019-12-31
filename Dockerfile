FROM ubuntu:18.10

LABEL MAINTAINER  rafa

EXPOSE 5000

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.7-dev && \
    apt-get install -y iputils-ping 

RUN apt-get install -y libldap2-dev libsasl2-dev ldap-utils 

RUN apt-get install -y nginx uwsgi uwsgi-plugin-python3

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY ./nginx.conf /etc/nginx/nginx.conf

WORKDIR /

COPY . /

RUN adduser --disabled-password --gecos '' nginx\
  && chown -R nginx:nginx /app \
  && chmod 777 /run/ -R \
  && chmod 777 /root/ -R

ENTRYPOINT [ "/bin/bash", "/launcher.sh"]