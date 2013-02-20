import yaml
import os.path
import Graylog2Logger

def Parse(path):
    """
        Parses config yaml file passed to Runner as command line argument
    """
    # Check if file exists at path
    
    if(os.path.isfile(str(path)) == False):
        print('Oh dear ! No file found at the specified path for the yaml config file.')
        Graylog2Logger.logToGraylog2('No file found at {0}'.format(str(path)))
        
    # Try loading the yaml config file
    
    
    try:
        f=open(path)
        dataMap=yaml.load(f)
    except:
        print('Error parsing yaml file')
        Graylog2Logger.logToGraylog2('Error parsing yaml file')
        return None
    
    if not(dataMap is None):
        return dataMap
    






# for testing
if __name__ == '__main__':
    Parse("/home/sushant/workspace/GitRepos/RDSMySqlLogPuller/MysqlLogPuller/src/config.yaml")
        