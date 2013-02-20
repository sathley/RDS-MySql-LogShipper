import mysql.connector
import Graylog2Logger


def pullSlowLogsFromMysql(host,user,password,rotate_logs):
    """
    Pulls slow logs from mysql and rotates the table if asked to
    """
    
    try:
        cnx=mysql.connector.connect(user=user,host=host,password=password,database='mysql')
    
        logs=[]
        
        #rowDict = {'start_time':'','query_time':'','lock_time':'','rows_sent':'','rows_examined':'','db':'','last_insert_id':'','insert_id':'','server_id':'','sql_text':'' }
        cursor = cnx.cursor()
        
        query = ("SELECT start_time, query_time, lock_time, rows_sent, rows_examined, db, `last_insert_id`, insert_id, server_id, sql_text FROM mysql.slow_log limit 10 ; ")

        cursor.execute(query)

        for (start_time, query_time, lock_time, rows_sent, rows_examined, db, last_insert_id, insert_id, server_id, sql_text) in cursor:
            rowDict={}
            rowDict['start_time']=str(start_time)
            rowDict['query_time']=str(query_time)
            rowDict['lock_time']=str(lock_time)
            rowDict['rows_sent']=str(rows_sent)
            rowDict['rows_examined']=str(rows_examined)
            rowDict['db']=str(db)
            rowDict['last_insert_id']=str(last_insert_id)
            rowDict['insert_id']=str(insert_id)
            rowDict['server_id']=str(server_id)
            rowDict['sql_text']=str(sql_text)
            logs.append(rowDict)
            
        cursor.close() 
        
        if rotate_logs:
            cur=cnx.cursor()
            cur.execute('CALL mysql.rds_rotate_slow_log;')
            cur.close()
        
        return logs
    
    except Exception as err:
        Graylog2Logger.logToGraylog2('Connection to production mysql failed. {0}'.format(err))    
    
    finally:
        cnx.close()

def pullGeneralLogsFromMysql(host,user,password,rotate_logs):
    """
    Pulls general logs from mysql and rotate the table
    """
    
    try:
        cnx=mysql.connector.connect(host=host,user=user,password=password,database='mysql')
    
        logs=[]
        
#        rowDict = {'event_time':'','user_host':'','thread_id':'','server_id':'','command_type':'','argument':'' }
        cursor = cnx.cursor()
        
        query = ("SELECT event_time, user_host, thread_id, server_id, command_type, argument FROM mysql.general_log limit 10 ; ")

        cursor.execute(query)

        for (event_time, user_host, thread_id, server_id, command_type, argument) in cursor:
            rowDict={}
            rowDict['event_time']=str(event_time)
            rowDict['user_host']=str(user_host)
            rowDict['thread_id']=str(thread_id)
            rowDict['server_id']=str(server_id)
            rowDict['command_type']=str(command_type)
            rowDict['argument']=str(argument)
            logs.append(rowDict)
            
        cursor.close() 
        
        if rotate_logs:
            cur=cnx.cursor()
            cur.execute('CALL mysql.rds_rotate_general_log;')
            cur.close()
        
        
        return logs
    
    except Exception as err:
        Graylog2Logger.logToGraylog2('Connection to production mysql failed. {0}'.format(err))   
    
    finally:
        cnx.close()
    
