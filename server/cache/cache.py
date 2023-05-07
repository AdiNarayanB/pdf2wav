import redis
import struct
import numpy as np
import random
import string
import json



class RedisCache:

    def __init__(self,cache_url):
        r = redis.Redis(host = cache_url.split(":")[0],port=int(cache_url.split(":")[1]))

        self.cache_url = cache_url
        self.redis_obj = r
    def validateToken(self,username,token):
        return self.get(username,token)

    def generateToken(self):
        N =15
        res = "".join(random.choices(string.ascii_uppercase+string.digits,k=N))
        return res
    def toRedis(self,username,password):
        token = self.generateToken()
        valueString = json.dumps({"username":username, "token":token })
        self.redis_obj.set(username,valueString)


        return token

    def fromRedis(self,username, token):
        """Retrieve Numpy array from Redis key 'n'"""
        valueString = self.redis_obj.get(username)
        print(json.loads(valueString))
        if json.loads(valueString)['token'] != token:
                return False
        else:
                return True


    def put(self,username,password):

        token = self.toRedis(username,password)
        return token
    def get(self,username,token):
        isFound = self.fromRedis(username,token)

        return isFound




