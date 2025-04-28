#!/usr/bin/env python3
""" return a tuple of size two containing a start index and an end index"""


def index_range(page: int, page_size: int):
    """ return a tuple of size two containing a start index and an end index"""

    indexSize = page * page_size
    indexStart = indexSize - page_size
    indexEnd = indexStart + page_size
    return indexStart, indexEnd
