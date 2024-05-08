#!/usr/bin/env python3
''' Define the BasicCache class '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' Represents an object that caches items using a dictionary '''
    def put(self, key, item):
        ''' Add an item to the cache '''
        if (key is not None and item is not None):
            self.cache_data.update({key: item})

    def get(self, key):
        ''' Retriece an item from the cache '''
        return self.cache_data.get(key, None)
