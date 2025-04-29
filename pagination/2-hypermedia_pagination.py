#!/usr/bin/env python3
""" return a tuple of size two containing a start index and an end index"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """ return a tuple of size two containing a start index and an end index"""

    indexSize = page * page_size
    indexStart = indexSize - page_size
    indexEnd = indexStart + page_size
    return indexStart, indexEnd


class Server:
    """Server class to paginate a database
    of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Server class to paginate a database of popular baby names.
    """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Server class to paginate a database of popular baby names.
    """
        data = self.get_page(page, page_size)
        page_size = len(data)
        if page_size <= 0:
            return {
                'page_size': 0,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': 0,
            }
        total_count = len(self.dataset())
        total_pages = math.ceil(total_count / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
