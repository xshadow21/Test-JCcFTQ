#!/usr/bin/python
# -*- coding: utf-8 -*-
"""flatten.py - extended utils

This module is used to flat information in its respectve format type

Example:
    Simply import it to access these functions::
        from modules.flatten import *

Attributes:
    no global attribute

Todo:
    * Improve flatten function to take any types as parameter
    * Add other flatten types such as: dictionaries, tuple, files data
"""

import sys
from copy import deepcopy
from modules.validation import *

def flatten(nestedList):
  """Create a flatten generator object from the nested data

  Flatten an arbitrarily nested list, without recursion (to avoid
  stack overflows: `RecursionError: maximum recursion depth exceeded`)

  Args:
    nestedList (list): A nested list on any levels with any data type

  Yields:
    type: The next value of the list or nested list regardless of its type
  """
  nestedList = deepcopy(nestedList)
  
  while nestedList:
    sublist = nestedList.pop(0)

    if isinstance(sublist, list):
      nestedList = sublist + nestedList
    else:
      yield sublist

def flattenList(nestedList):
  """Flat a nested list with any depth levels

  Args:
    nestedList (list): A nested list parameter

  Returns:
    A flatten list of the provided `nestedList`
  
  Examples:
    >>> flattenList([['1', 2, [3]], 4])
    ['1', 2, 3, 4]

    >>> flattenList(['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]])
    ['1', 2, 3, 4, 5]
  """
  flatList = flatten(VALIDATE_LIST(nestedList))
  return [x for x in flatList]
