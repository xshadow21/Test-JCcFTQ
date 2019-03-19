#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tracker.py - base tracker model

This model represent a base tracker

Example:
    Simply import it to access these functions::
        from models.Tracker import *

Attributes:
    data (list): list of recorded integer.

Todo:
    * Add a delete and update function
    * Can have more flexibility in the data manipulation
"""

import sys
from modules.validation import *

class Tracker:
  def __init__(self):
    self.data = []

  def insert(self, entry):
    """Insert a new integer in the dataset

    Args:
      entry (int): A new integer entry
    """
    self.data.append(VALIDATE_INTEGER(entry))

  def get_max(self):
    """Get the highest value of the dataset

    Returns:
      An integer representing the highest value of the dataset
    """
    if len(self.data) == 0:
      return 0

    return max(self.data)

  def get_min(self):
    """Get the lowest value of the dataset

    Returns:
      An integer representing the lowest value of the dataset
    """
    if len(self.data) == 0:
      return 0

    return min(self.data)
