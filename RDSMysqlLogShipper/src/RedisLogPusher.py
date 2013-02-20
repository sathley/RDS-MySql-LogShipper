import redis
import Graylog2Logger


def push(logs,config):
    """
    Pushes logs to redis server
    """    
    redisConfig=dict(config)
    try:
        red=redis.Redis(redisConfig['hostname'])
    
        for log in logs:
            red.lpush(redisConfig['key'],log)
            
    except Exception as err:
        print('Connection to logging redis failed. {0}'.format(err))
        Graylog2Logger.logToGraylog2('Connection to logging redis failed. {0}'.format(err))
    