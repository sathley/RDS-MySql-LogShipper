RDSMySqlLogShipper
==================

Ships logs from RDS mysql to a configurable recipient.

To run this script, run the file called Runner.py with a command line argument which is the path to the yaml configuration file.
This can be done as python Runner.py <path to yaml config file>

A test yaml config file is given below:

input:
  mysql:
    host: mysql-write.aws.appacitive.com
    user: Gossamer
    password: zaq1ZAQ!
    rotate_logs: false
output:
#  udp:
#    hostname: graylog.aws.appacitive.com
#    port: 22514
#  tcp:
#    hostname: graylog.aws.appacitive.com
#    port: 22514
#  redis:
#    hostname: graylog.aws.appacitive.com
#    port: 6379
#    datatype: list
#    key: logstash
  file:
    path: /home/sushant/Public/test.log
#  rabbitmq:
#    name: exchange_name
#    hostname: my_amqp_server
#    exchange_type: fanout
output_format: plain/json/xml(default:plain)
