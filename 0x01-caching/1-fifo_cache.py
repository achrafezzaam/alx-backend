#!/usr/bin/env python3
''' Define the BasicCache class '''
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' Represents an object that caches items using a dictionary '''
    def __init__(self):
        ''' Initiate the FIFOCache Object '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Add an item to the cache '''
        if (key is not None and item is not None):
            self.cache_data.update({key: item})
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            pop_key, val = self.cache_data.popitem(False)
            print("DISCARD:", pop_key)

    def get(self, key):
        ''' Retrieve an item from the cache '''
        return self.cache_data.get(key, None)
