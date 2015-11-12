FROM centos:7

RUN \
  yum -y install wget bzip2 && \
  curl -O -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2 && \
  bunzip2 phantomjs-1.9.8-linux-x86_64.tar.bz2 && tar xf phantomjs-1.9.8-linux-x86_64.tar 

RUN \
  yum install -y epel-release && \
  yum install -y git python-pip python-devel libpng-devel libjpeg-devel gcc gcc-c++ make && \
  pip install Django==1.8.6 && \
  pip install Pillow pika gunicorn

RUN \
  yum -y install fontconfig libfontenc fontconfig-devel \
  libXfont ghostscript-fonts xorg-x11-font-utils urw-fonts

RUN \
  git clone https://github.com/ukwa/django-phantomjs.git

COPY settings.py /django-phantomjs/phantomjs/

WORKDIR django-phantomjs

RUN \
  python manage.py migrate

EXPOSE 8000

CMD gunicorn -c gunicorn.ini wsgi:application
