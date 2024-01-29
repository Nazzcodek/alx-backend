#!/usr/bin/env python3
"""the pagination module"""


def index_range(page: int, page_size: int) -> tuple:
    """the index function"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
