# -*- coding: utf8 -*-
#from https://www.dyxmq.cn/databases/redis/redis-demo-visit-limit.html with minor modify 
import web
import redis
import time 
"""
LIMIT_TIME：在多长的时间范围内
LIMIT_TIMES：最多访问多少次
"""
LIMIT_TIMES = 3
LIMIT_TIME = 10
 
#conn = redis.StrictRedis()
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True) 
conn = redis.Redis(connection_pool=pool)

"""
路由处理
"""
urls = (
    "/", "Index"
)




class Index:
    @staticmethod
    def __mk_h1(data):
        return "<title>HelloWorld</title><div align=center><h1>%s</h1></div>" % data
 
    def __visit(self, key_name):
        n = int(conn.llen(key_name))
        if n < LIMIT_TIMES:
            conn.lpush(key_name, time.time())
            return self.__mk_h1("Hello!")
        else:
            now = time.time()
            t = float(conn.lrange(key_name, 2, 2)[0])  # lrange returns a list, 取出目前保存的最早的一次登陆时间
            print now, t, now - t
            if time.time() - t <= LIMIT_TIME:
                return self.__mk_h1("Error, please retry at %f second(s) later" % (t + LIMIT_TIME - time.time()) )
            else:
                # 弹出最右边的元素，即最先被插进来的元素
                conn.rpop(key_name)
                # 插入元素
                conn.lpush(key_name, now)
                return self.__mk_h1("Hello")
 
    def GET(self):
        """
        处理用户请求
        """
        params = web.input()
        if "user" not in params:
            return self.__mk_h1("Who are you")
        else:
            user = params["user"]
            key_name = "login:times:%s" % user
            return self.__visit(key_name)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
