from aws_lambda_powertools import Logger
from lib.s3_tools import tag_buckets

logger = Logger()


def lambda_handler(event, _context):

    try:
        buckets_tagged = tag_buckets()
        logger.info("tagged", extra={"buckets": buckets_tagged})
    except Exception as e:
        logger.exception(e, extra={"event": event})
        raise e
