from mlmt import TimeStamp

import unittest

class TimeStampTestCase(unittest.TestCase):
  def setUp(self):
    self.ts = TimeStamp()

  def test_str(self):
    self.assertEqual(len(str(self.ts)), 15)
    self.assertTrue("-" in str(self.ts))

  def test_elapsed(self):
    self.assertIsInstance(self.ts.elapsed(), float)
