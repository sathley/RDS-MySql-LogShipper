import socket
import Graylog2Logger


def push(logs,config):
    """
        Pushes the logs via TCP
    """
    tcpConfig=dict(config)
    
    tcp_host=str(tcpConfig["hostname"])
    tcp_port=int(tcpConfig["port"])
    
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    for log in logs:
        try:
            sock.sendto(str(log),(tcp_host,tcp_port))
        except Exception as err:
            print('TCP connection failed. {0}'.format(err))
            Graylog2Logger.logToGraylog2('TCP connection failed. {0}'.format(err))