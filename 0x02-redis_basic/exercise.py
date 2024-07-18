#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Return the generate uuid key
    """
    def __init__(self) -> None:
        """
        Initializes a cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store a value in a Redis data storage and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
