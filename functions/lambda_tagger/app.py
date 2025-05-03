from aws_lambda_powertools import Logger
from lib.lambda_tools import tag_lambdas

logger = Logger()


def lambda_handler(event, _context):

    try:
        lambdas_tagged = tag_lambdas()
        logger.info("tagged", extra={"lambdas": lambdas_tagged})
    except Exception as e:
        logger.exception(e, extra={"event": event})
        raise e
