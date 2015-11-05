import gzip
import json
import pika
import uuid
import shutil
import logging
import requests
from harchiverd import settings
from daemonize import Daemon
from datetime import datetime
from urlparse import urlparse
from hanzo.warctools import WarcRecord
from warcwriterpool import WarcWriterPool, warc_datetime_str

logger = logging.getLogger("harchiverd")
handler = logging.FileHandler(settings.LOG_FILE)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
        warcwriter = WarcWriterPool(gzip=True, output_dir=settings.OUTPUT_DIRECTORY)
        while True:
            try:
                logger.debug("Starting connection %s:%s." % (settings.HAR_QUEUE_HOST, settings.HAR_QUEUE_NAME))
                connection = pika.BlockingConnection(pika.ConnectionParameters(settings.HAR_QUEUE_HOST))
                channel = connection.channel()
                channel.queue_declare(queue=settings.HAR_QUEUE_NAME, durable=True)
                for method_frame, properties, body in channel.consume(settings.HAR_QUEUE_NAME):
                    callback(warcwriter, body)
                    channel.basic_ack(method_frame.delivery_tag)
            except Exception as e:
                logger.error(str(e))
                requeued_messages = channel.cancel()
                logger.debug("Requeued %i messages" % requeued_messages)

