#!/usr/bin/env python3
"""LRU module"""
from base_caching import BaseCaching as BC


class LRUCache(BC):
    '''this is lru caching object instance'''

    def __init__(self):
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        '''this is a cache put method'''
        if key is None or item is None:
            return

        data = self.cache_data
        order = self.use_order

        if len(data) >= BC.MAX_ITEMS:
            if order:
                discard = order.pop()
                del data[discard]
                print(f'DISCARD: {discard}')

        data[key] = item
        order.append(key)

    def get(self, key):
        '''this method get cache key'''
        if key in self.cache_data:
            self.use_order.remove(key)
            self.use_order.append(key)

        return self.cache_data.get(key, None)
