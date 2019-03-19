#!/usr/bin/python
# -*- coding: utf-8 -*-
"""validation.py - extended utils

This module is used to validate data before start using it

Example:
  Simply import it to access these functions::
      from modules.flatten import *

Attributes:
  no global attribute

Todo:
  * Add more validation functions
  * Add a convertion/merge module
"""

import unittest
import sys

def VALIDATE_LIST(uncheckedList):
  """Validate list format type

  Args:
    uncheckedList (list): a list parameter

  Raises:
    TypeError: If `uncheckedList` is not a list type.

  Returns:
    The provided `uncheckedList`
  """
  if type(uncheckedList) is not list:
    raise TypeError("Variable is not a list")

  return uncheckedList

def VALIDATE_INTEGER(uncheckedInt):
  """Validate int format type

  Args:
    uncheckedInt (int): a int parameter

  Raises:
    TypeError: If `uncheckedInt` is not a int type.

  Returns:
    The provided `uncheckedInt`
  """
  if type(uncheckedInt) is not int:
    raise TypeError("Variable is not a int")

  return uncheckedInt

def VALIDATE_FLOAT(uncheckedFloat):
  """Validate float format type

  Args:
    uncheckedFloat (float): a float parameter

  Raises:
    TypeError: If `uncheckedFloat` is not a float type.

  Returns:
    The provided `uncheckedFloat`
  """
  if type(uncheckedFloat) is not float:
    raise TypeError("Variable is not a float")

  return uncheckedFloat
