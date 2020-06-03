#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataclasses import dataclass

# https://docs.python.org/3/library/dataclasses.html#module-dataclasses
"""
This module provides a decorator and functions for automatically
adding generated special methods such as __init__() and __repr__() to user-defined classes.
It was originally described in PEP 557.
"""

@dataclass()
class InventoryItem():
    '''Class for keeping track of an item in inventory.

    @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
    Si la clase define debajo __init__, __repr__, __eq__ es ignorado y no genera automaticamente
    '''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

# añade.
"""
def __init__(self, name: str, unit_price: float, quantity_on_hand: int=0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
"""