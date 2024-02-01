#!/usr/bin/env python3
"""LFU module"""
from base_caching import BaseCaching as BC


class LFUCache(BC):
    '''this is lfu caching object instance'''

    def __init__(self):
        super().__init__()
        self.use_order = []
        self.use_counter = {}

    def put(self, key, item):
        '''this is a cache put method'''
        if key is None or item is None:
            return

        data = self.cache_data
        order = self.use_order
        counter = self.use_counter

        if len(data) >= BC.MAX_ITEMS:
            min_counter = min(counter.values())
            min_counter_key = [
                    k for k, v in counter.items()
                    if v == min_counter
                    ]
            if len(min_counter_key) > 1:
                lru = min(order, key=lambda k: order.index(k))
                discard = lru
            else:
                discard = min_counter_key[0]

            del data[discard]
            del counter[discard]
            order.remove(discard)

            print(f'DISCARD: {discard}')

        data[key] = item
        counter[key] = counter.get(key, 0) + 1
        order.append(key)

    def get(self, key):
        '''this method get cache key'''
        if key in self.cache_data:
            self.use_counter[key] += 1
            self.use_order.remove(key)
            self.use_order.append(key)

        return self.cache_data.get(key, None)
