#coding=utf-8

import redis
pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
r = redis.Redis(connection_pool=pool)

lua_2 = """
    redis.call("setnx", KEYS[1], ARGV[1])
    redis.call("expire", KEYS[1], ARGV[2])
    local ret = redis.call("get", KEYS[1])
      return ret
    """
script_2 = r.register_script(lua_2)

print(script_2(keys=["hugo"], args=[11, 6]))

