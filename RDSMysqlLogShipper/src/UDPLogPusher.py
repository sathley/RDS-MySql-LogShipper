import socket
import Graylog2Logger


def push(logs,config):
    """
        Pushes the logs via UDP
    """
    
    udpConfig=dict(config)
    
    udp_host=str(udpConfig["hostname"])
    udp_port=int(udpConfig["port"])
    
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    for log in logs:
        try:
            sock.sendto(str(log),(udp_host,udp_port))
        except Exception as err:
            print('UDP connection failed. {0}'.format(err))
            Graylog2Logger.logToGraylog2('UDP connection failed. {0}'.format(err))