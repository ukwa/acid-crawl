FROM centos:7

RUN \
  yum install -y epel-release && \
  yum install -y git python-pip && \
  pip install flask

COPY simple /simple

WORKDIR simple

EXPOSE 5000

CMD python simple.py
