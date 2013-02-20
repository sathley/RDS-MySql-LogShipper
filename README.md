RDSMySqlLogShipper
==================

Ships logs from RDS mysql to a configurable recipient.

To run this script, run the file called Runner.py with a command line argument which is the path to the yaml configuration file.
This can be done as follows
>>python Runner.py [path to yaml config file]

A test yaml config file is given below:
<pre>
input:
  mysql:
    host: mysql_host
    user: mysql_user
    password: mysql_pass
    rotate_logs: false
output:
  udp:
    hostname: udp_ip
    port: udp_port
  tcp:
    hostname: tcp_ip
    port: tcp_port
  redis:
    hostname: redis_host
    port: redis_port
    key: redis_list_key
  file:
    path: /home/john_doe/Public/logs/mysql_logs_rds.log
  rabbitmq:
    name: exchange_name
    hostname: my_amqp_server
    exchange_type: fanout
output_format: plain/json/xml(default:plain)
</pre>
