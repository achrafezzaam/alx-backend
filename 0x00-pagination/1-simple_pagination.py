#!/usr/bin/env python3
''' Define the Server class '''
import csv
import math
from typing import List, Tuple


class Server:
    '''Server class to paginate a database of popular baby names'''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Instantiate the Server object '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        ''' Return a tuple of size two containing a start index
        and an end index corresponding to the range of indexes
        to return in a list '''
        return (page_size * (page - 1), page_size * page)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Retrieve a page'''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        first, last = self.index_range(page, page_size)
        data = self.dataset()
        if first > len(data):
            return []
        return data[first:last]
