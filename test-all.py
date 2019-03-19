#!/usr/bin/python
"""test-all.py - main testing file

This will trigger the unit test on all functionalities

Example:
    Simply import it to access these functions::
        $ python test-all.py

Todo:
    * Mock data must be implemented
    * Mock data must be re-used
    * Separate all test and aglomerate them in a testing module
"""

import unittest
import sys
from modules.flatten import *
from models.TempTracker import *

class FlattenTest(unittest.TestCase):
  def test_FlattenList_WithValidBaseType_ShouldBeValid(self):
    self.assertEqual(flattenList([['1', 2, [3]], 4]), ['1', 2, 3, 4])
    
  def test_FlattenList_WithValidBaseType_WithDifferemtInnerType_ShouldBeValid(self):
    self.assertEqual(flattenList([[{"key":"value"}, 2, [3]], 4]), [{"key":"value"}, 2, 3, 4])

class TrackerTest(unittest.TestCase):
  def test_Insert_WithValidEntry_ShouldBeValid(self):
    tracker = Tracker()
    tracker.insert(2)

    self.assertEqual(tracker.data[0], 2)

  def test_Insert_WithValidEntry_ShouldBeInvalid(self):
    tracker = Tracker()
    tracker.insert(2)

    self.assertNotEqual(tracker.data[0], 4)

  def test_GetMax_WithoutData_ShouldBeValid(self):
    tracker = Tracker()
    tracker.data = []

    self.assertEqual(tracker.get_max(), 0)

  def test_GetMax_WithoutData_ShouldBeInvalid(self):
    tracker = Tracker()
    tracker.data = []

    self.assertNotEqual(tracker.get_max(), 1)

  def test_GetMax_WithData_ShouldBeValid(self):
    tracker = Tracker()
    tracker.data = [0, 25, 40, 2, 90, 32, 11, 74]

    self.assertEqual(tracker.get_max(), 90)

  def test_GetMax_WithData_ShouldBeInvalid(self):
    tracker = Tracker()
    tracker.data = [0, 25, 40, 2, 90, 32, 11, 74]

    self.assertNotEqual(tracker.get_max(), 2)

  def test_GetMin_WithoutData_ShouldBeValid(self):
    tracker = Tracker()
    tracker.data = []

    self.assertEqual(tracker.get_min(), 0)

  def test_GetMin_WithoutData_ShouldBeInvalid(self):
    tracker = Tracker()
    tracker.data = []

    self.assertNotEqual(tracker.get_min(), 1)

  def test_GetMin_WithData_ShouldBeValid(self):
    tracker = Tracker()
    tracker.data = [0, 25, 40, 2, 90, 32, 11, 74]

    self.assertEqual(tracker.get_min(), 0)

  def test_GetMin_WithData_ShouldBeInvalid(self):
    tracker = Tracker()
    tracker.data = [0, 25, 40, 2, 90, 32, 11, 74]

    self.assertNotEqual(tracker.get_min(), 33)

class TempTrackerTest(unittest.TestCase):
  def test_GetMean_WithoutData_ShouldBeFloatAndValid(self):
    temperatureTracker = TempTracker()
    temperatureTracker.data = []

    self.assertEqual(temperatureTracker.get_mean(), 0.0)

  def test_GetMean_WithoutData_ShouldBeFloatAndInvalid(self):
    temperatureTracker = TempTracker()
    temperatureTracker.data = []

    self.assertNotEqual(temperatureTracker.get_mean(), 1.2)

  def test_GetMean_WithData_ShouldBeFloatAndValid(self):
    temperatureTracker = TempTracker()
    temperatureTracker.data = [0, 25, 40, 2, 90, 32, 11, 74]

    self.assertEqual(temperatureTracker.get_mean(), 34.25)

  def test_GetMean_WithData_ShouldBeFloatAndInvalid(self):
    temperatureTracker = TempTracker()
    temperatureTracker.data = [0, 25, 40, 2, 90, 32, 11, 74]

    self.assertNotEqual(temperatureTracker.get_mean(), 2.25)

if __name__ == "__main__":
  unittest.main()
