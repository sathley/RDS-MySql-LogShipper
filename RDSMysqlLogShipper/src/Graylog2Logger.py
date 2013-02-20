

import logging
import graypy


graylog2Config={"host":"graylog.aws.appacitive.com", "port":12201}



def logToGraylog2(log):
    """
        Logs internal errors in this script to graylog server.
    """
    my_logger = logging.getLogger('Mysql Log Puller')
    my_logger.setLevel(logging.CRITICAL)

    handler = graypy.GELFHandler(graylog2Config["host"], graylog2Config["port"])
    my_logger.addHandler(handler)

    my_logger.critical(log)