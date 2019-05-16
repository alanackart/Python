from kafka import KafkaConsumer
import thread
import inspect
import time

grp_id = str(time.time() )
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def con1(consumer):
    while  1:
        for msg in consumer:
            print msg
        print ("sleep for 1 second", lineno() )
        time.sleep(1)

print ( 'grp_id is ', grp_id)
consumer1 = KafkaConsumer('TutorialTopic', group_id=grp_id, bootstrap_servers=['localhost:9092'])

thread.start_new_thread(con1, (consumer1,))
while 1 :
    data = raw_input("Press q to exit\n")
    if data == 'q':
        break;
