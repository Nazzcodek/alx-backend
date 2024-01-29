#!/usr/bin/env python3
"""the pagination module"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """the index helper function"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
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
        """this methode get a page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()

        if self.dataset() is None:
            return []

        page_index = index_range(page, page_size)
        correct_page = data[page_index[0]:page_index[1]]
        return correct_page
