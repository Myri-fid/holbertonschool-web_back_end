#!/usr/bin/env python3
"""sum_mixed_list which takes a list mxd_lst of integers and floats"""
from typing import List
from typing import Union, Optional


def sum_mixed_list(mxd_lst: List[Union[int, str]]) -> float:
    """sum_mixed_list which takes a list mxd_lst of integers and floats"""

    return sum(mxd_lst)
