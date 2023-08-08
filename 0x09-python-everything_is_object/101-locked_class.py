#!/usr/bin/python3
"""classs defination"""


class LockedClass:
    """allows only new instance attribute called first_name"""
    __slots__ = [first_name]
