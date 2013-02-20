import Graylog2Logger
import sys



def push(logs,config):
    """
    Writes logs to a file
    """
    fileConfig=dict(config)
    
    try:
        f=open(fileConfig["path"],'a')
        for log in logs:
            f.write(str(log))
            
    except Exception, e:
        print('Error writing logs to file. {0}'.format(e))        
        Graylog2Logger.logToGraylog2('Error writing logs to file. {0}'.format(e))
    finally:
        f.close()