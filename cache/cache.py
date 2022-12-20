import redis
import struct
import numpy as np


class RedisCache:
    def __init__(self,cache_url):
        r = redis.Redis()

        self.cache_url = cache_url
        self.redis_obj = r

    def toRedis(self,a,n):
        """Store given Numpy array 'a' in Redis under key 'n'"""
        h, w = a.shape
        shape = struct.pack('>II',h,w)
        encoded = shape + a.tobytes()

        # Store encoded data in Redis
        self.redis_obj.set(n,encoded)
        return

    def fromRedis(self,n):
        """Retrieve Numpy array from Redis key 'n'"""
        encoded = self.redis_obj.get(n)
        h, w = struct.unpack('>II',encoded[:8])
        # Add slicing here, or else the array would differ from the original
        a = np.frombuffer(encoded[8:]).reshape(h,w)
        return a

    def put(self,wavByteObj,filename):
        self.toRedis(self,wavByteObj,filename)
        return True
    def get(self,filename):
        cacheWavNpArray = self.fromRedis(self,filename)
        return cacheWavNpArray




