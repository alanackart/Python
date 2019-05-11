#coding=utf-8

import redis    
import pickle

class Employee:
        def __init__(self, name, age, job):
            self.name = name
            self.age = age
            self.job = job
        def work(self):
            print(self.name, 'is working...')

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True) 
r = redis.Redis(connection_pool=pool)
#r.set('gender', 'male')   
#print(r.get('gender'))   
em  = Employee('abc', 22, 'waiter')
em_dmp  = pickle.dumps(em)
r.hset('employees', 'no.1' , em_dmp)
em_dmp2 = (r.hget('employees', 'no.1'))   
p = pickle.loads(em_dmp2)
p.work()
