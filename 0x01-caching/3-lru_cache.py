#!/usr/bin/env python3
''' Define the BasicCache class '''
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' Represents an object that caches items using a dictionary '''
    def __init__(self):
        ''' Initiate the LRUCache object '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Add an item to the cache '''
        if (key is None or item is None):
            return
        if key not in self.cache_data:
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS - 1):
                pop_key, val = self.cache_data.popitem()
                print("DISCARD:", pop_key)
            self.cache_data.update({key: item})
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data.update({key: item})

    def get(self, key):
        ''' Retrieve an item from the cache '''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
