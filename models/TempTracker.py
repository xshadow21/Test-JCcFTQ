#!/usr/bin/python
# -*- coding: utf-8 -*-
"""TempTracker.py - temperature tracker model

This model represent a temperature tracker

Example:
    Simply import it to access these functions::
        from models.TempTracker import *

Attributes:
    data (list): list of recorded temperature as integer.

Todo:
    * Can have more functionalities
"""

import sys
from models.Tracker import *
from modules.validation import *

class TempTracker(Tracker):
  def __init__(self):
    super().__init__()

  def get_mean(self):
    """Get the average of all recorded temperatures

    Returns:
      A float value of the average
    """
    if len(self.data) == 0:
      return 0.0

    return VALIDATE_FLOAT(float(sum(self.data) / len(self.data)))
