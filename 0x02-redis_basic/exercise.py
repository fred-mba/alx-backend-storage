#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    A class to generate and store uuid keys
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float]) -> str:
        key = str(uuid.uuid())
        self._redis.set(key, data)
        return key
