FROM centos:7

RUN \
  yum install -y epel-release && \
  yum install -y git python-pip python-devel && \
  pip install pika warctools requests

RUN \
  git clone https://github.com/ukwa/python-har-daemon.git && \
  git clone https://github.com/ukwa/python-warcwriterpool.git && \
  cd python-warcwriterpool && python setup.py install && cd .. && \
  git clone https://github.com/ukwa/python-daemonize.git && \
  cd python-daemonize && python setup.py install && cd ..

COPY settings.py /python-har-daemon/harchiverd/settings.py

COPY runner.py /python-har-daemon/runner.py

WORKDIR python-har-daemon

VOLUME /logs

VOLUME /images

CMD python runner.py
