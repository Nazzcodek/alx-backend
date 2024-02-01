#!/usr/bin/env python3
"""LIFO module"""
from base_caching import BaseCaching as BC


class LIFOCache(BC):
    '''this is lifo caching object instance'''

    def __init__(self):
        super().__init__()
        self.stack_data = []

    def put(self, key, item):
        '''this is a cache put method'''
        if key is None or item is None:
            return

        data = self.cache_data
        stack = self.stack_data

        if len(data) >= BC.MAX_ITEMS:
            if stack:
                discard = stack.pop()
                del data[discard]
                print(f'DISCARD: {discard}')

        data[key] = item
        stack.append(key)

    def get(self, key):
        '''this method get cache key'''
        return self.cache_data.get(key, None)
