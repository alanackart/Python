from kafka import KafkaProducer
import thread
import inspect
import time

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


def pro1(producer):
    msg = 'Hello world at '
    while  1:
        msg2 = msg +  str(time.time())
        producer.send('TutorialTopic', (msg2))
        #print ("sleep for 1 second", lineno() )
        #time.sleep(1)

producer1 = KafkaProducer(bootstrap_servers=['localhost:9092'])

thread.start_new_thread(pro1, (producer1,))
while 1 :
    data = raw_input("Press q to exit\n")
    if data == 'q':
        break;
