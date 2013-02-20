"""
author: Sushant Athley
date: 19 Feb 2013

Property of Appacitive Softwares Pvt. Ltd.
"""
import sys
import YAMLParser as yp
import LogPuller as lp
import LogFormatter as lf


if (__name__ == '__main__'):
    if(len(sys.argv)<2):
        print('input config file missing. pass path of yaml config file as command line parameter')
        sys.exit()
    dataMap=yp.Parse(sys.argv[1])
    
    
    #pull logs
    if(dataMap.has_key("input") and dict(dataMap["input"]).has_key("mysql")):
        mysqlConfig=dataMap["input"]["mysql"]
        print(mysqlConfig)
        rotate_logs=True if dict(mysqlConfig).has_key("rotate_logs") and mysqlConfig["rotate_logs"]== True else False
        slowLogs=lp.pullSlowLogsFromMysql(mysqlConfig["host"],mysqlConfig["user"],mysqlConfig["password"],rotate_logs)
        generalLogs=lp.pullGeneralLogsFromMysql(mysqlConfig["host"],mysqlConfig["user"],mysqlConfig["password"],rotate_logs)
        
        print(slowLogs)
        print(generalLogs)
        unformattedLogs=slowLogs
        unformattedLogs.extend(generalLogs)
        
        if(unformattedLogs.__len__()==0):
            print('No logs found')
            sys.exit()
    else:
        print('mysql config missing')
        sys.exit()
        
    # Format the logs accourding to configuration     
    logs=[] 
    if(dataMap.has_key("output_format") and dataMap["output_format"] != None):
        out_format=str(dataMap["output_format"])
        formattedLogs=lf.formatLogs(unformattedLogs,out_format)
        logs.append(formattedLogs)
    else:
        logs=unformattedLogs
    
    #push logs
    if(dataMap.has_key("output") ==False or dataMap["output"]==None):
        print('No output specified')
        sys.exit()
        
    outputConfig=dict(dataMap["output"])
    
    if(outputConfig.has_key("tcp") and len(dict(outputConfig["tcp"]).keys())>0):
        tcpConfig=outputConfig["tcp"]
        import TCPLogPusher
        TCPLogPusher.push(logs,tcpConfig)
        
    elif(outputConfig.has_key("udp") and len(dict(outputConfig["udp"]).keys())>0):
        udpConfig=outputConfig["udp"]
        import UDPLogPusher
        UDPLogPusher.push(logs,udpConfig)
        
    elif(outputConfig.has_key("file") and len(dict(outputConfig["file"]).keys())>0):
        fileConfig=outputConfig["file"]
        import FileLogPusher
        FileLogPusher.push(logs,fileConfig)
        
    elif(outputConfig.has_key("redis") and len(dict(outputConfig["redis"]).keys())>0):
        redisConfig=outputConfig["redis"]
        import RedisLogPusher
        RedisLogPusher.push(logs,redisConfig)
        
    elif(outputConfig.has_key("amqp") and len(dict(outputConfig["amqp"]).keys())>0):
        amqpConfig=outputConfig["amqp"]
        import AMQPLogPusher
        AMQPLogPusher.push(logs,amqpConfig)
        
    else:
        print('no output configuration found')        
        
    sys.exit()
        
        
        
        
        