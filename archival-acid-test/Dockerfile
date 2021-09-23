FROM python:3

RUN \
  pip install flask

COPY aat /aat

WORKDIR aat

EXPOSE 5000

CMD python aat.py
