from threading import Thread
import time

from pykafka import KafkaClient
from kafka import KafkaConsumer
from kafka import KafkaProducer


def get_msg_1():
    return '''{
    "name" : "Customer_MakerQuote_Req",
    "extend" : "",
    "time" : 1562813858244,
    "comstar_grp" : "A",
    "props" : {
        "B_StipulationYield2" : "3.0",
        "S_StipulationYield2" : "2.9",
        "StrategySeq" : "",
        "B_OrderQty" : 0,
        "CUS_NUMBER" : 856,
        "DEALER" : 478,
        "QUOTEKIND" : 1,
        "Strategy_Remark" : "this is a test",
        "ACTION_TIMEOUT" : 60,
        "S_OrderQty" : 0,
        "RoutingID" : "A",
        "SecurityID" : "100204",
        "StrategyIDList" : "USER_DEFINED_RANKING",
        "MDSubType" : "107",
        "QuoteTransType" : "R",
        "OrigClOrdID" : "MQ2019071185600039",
        "RoutingType" : 5,
        "ACTION_TYPE" : 3,
        "Bid_Rank" : 5,
        "Ofr_Rank" : 3
    }
}
}'''





def generate_bootstrap_data():
    client = KafkaClient(hosts='172.19.223.70:9035')
    producer = client.topics['CmsResponseTopicA'.encode('utf8')].get_sync_producer()

    while True:
        producer.produce(get_msg_1().encode('utf8'))
        time.sleep(10)
        # producer.produce(get_msg_3().encode('utf8'))
        # time.sleep(14)


def market_data_transfer():
    client = KafkaClient(hosts='192.168.234.19:9092')
    producer = client.topics['MakerEventNew'.encode('utf8')].get_sync_producer()
    consumer = KafkaConsumer('MakerEventNew', group_id='I\'m alan', bootstrap_servers='172.19.223.70:9035')
    for msg in consumer:
        producer.produce(msg.value)


bootstrap_data_thread = Thread(target=generate_bootstrap_data)
bootstrap_data_thread.start()

# market_data_thread = Thread(target=market_data_transfer)
# market_data_thread.start()
