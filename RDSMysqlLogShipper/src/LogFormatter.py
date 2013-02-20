import json
import dict2xml
import sys



def formatLogs(logs,format):
    """
        Formats the logs according to the specified format in the config yaml
    """
    formattedLogs=[]
    
    if(format.__eq__("json")):
        for log in logs:
            formattedLogs.append(json.dumps(dict(log)))
        return formattedLogs
    elif(format.__eq__("xml")):
        for log in logs:
            formattedLogs.append(dict2xml.dict2xml(dict(log)))
        return formattedLogs
    else:
        return logs