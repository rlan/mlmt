from mlmt.tool import as_string

import unittest
import numpy as np

class ListTestCase(unittest.TestCase):
  def test_list(self):
    str = as_string([1, 2, 3])
    self.assertTrue("type" in str)
    self.assertTrue("list" in str)
    self.assertTrue("len 3" in str)

class TupleTestCase(unittest.TestCase):
  def test_tuple(self):
    str = as_string((1, 2))
    self.assertTrue("type" in str)
    self.assertTrue("tuple" in str)
    self.assertTrue("len 2" in str)

class DictTestCase(unittest.TestCase):
  def test_dict(self):
    str = as_string({"hello": 1, "world": 2})
    self.assertTrue("type" in str)
    self.assertTrue("dict" in str)
    self.assertTrue("len 2" in str)
    self.assertTrue("hello" in str)
    self.assertTrue("world" in str)

class NdArrayTestCase(unittest.TestCase):
  def test_ndarray(self):
    str = as_string(np.array([1,2,3], dtype=np.uint8))
    self.assertTrue("type" in str)
    self.assertTrue("numpy.ndarray" in str)
    self.assertTrue("shape" in str)
    self.assertTrue("dtype uint8" in str)
