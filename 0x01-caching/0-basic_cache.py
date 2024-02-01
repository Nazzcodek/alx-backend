#!usr/bin/env python3
"""Basic cache module"""
from base_caching import BaseCaching as BC


class BasicCache(BC):
    """this is a basic cache object instance"""

    def put(self, key, item):
        """cache put method"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """this mehtod get key of a catche"""
        return self.cache_data.get(key, None)
