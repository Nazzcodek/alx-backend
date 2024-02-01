#!/usr/bin/env python3
"""FIFO module"""
from base_caching import BaseCaching as BC


class FIFOCache(BC):
    '''this is fifo caching object instance'''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''this is a cache put method'''
        if key is None or item is None:
            return

        data = self.cache_data
        if len(data) >= BC.MAX_ITEMS:
            discard, _ = data.popitem(last=False)
            print(f'DISCARD: {discard}')

    def get(self, key):
        '''this method get cache key'''
        return self.cache_data.get(key, None)
