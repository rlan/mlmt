class RunningStats:
  """Compute running mean and variance using Welford's online algorithm

  https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance

  Example
  -------

  >>> from running_stats import RunningStats
  >>> s = RunningStats()

  Initial values
  >>> s.count()
  0
  >>> s.mean()
  nan
  >>> s.variance()
  nan
  >>> s.sampleVariance()
  nan

  Update with some values
  >>> data = [1.0, 2.0, 3.0, 4.0, 5, 6, 7, 8, 9]
  >>> isinstance(s(data), RunningStats)
  True
  >>> s.count()
  9
  >>> s.mean()
  5.0
  >>> s.variance()
  6.666666666666667
  >>> s.sampleVariance()
  7.5

  Clear
  >>> isinstance(s.clear(), RunningStats)
  True
  >>> s.count()
  0
  >>> s.mean()
  nan
  >>> s.variance()
  nan
  
  """

  def __init__(self):
    self.clear()

  def __call__(self, input):
    try:
      for scalar in input:
        self.update(scalar)
    except TypeError:
      self.update(input)
    return self

  def clear(self):
    self.count_ = 0
    self.mean_ = 0.0
    self.M2_ = 0.0
    return self
    
  def update(self, input):
    self.count_ += 1
    delta = input - self.mean_
    self.mean_ = self.mean_ + delta / self.count_
    delta2 = input - self.mean_
    self.M2_ = self.M2_ + delta * delta2
    return self

  def count(self):
    return self.count_

  def mean(self):
    if self.count_ < 2:
      return float('nan')
    else:
      return self.mean_

  def variance(self):
    if self.count_ < 1:
      return float('nan')
    else:
      return self.M2_ / self.count_

  def sampleVariance(self):
    if self.count_ < 2:
      return float('nan')
    else:
      return self.M2_ / (self.count_ - 1)
    
  

if __name__ == "__main__":
  import doctest 
  import sys 
  (failure_count, test_count) = doctest.testmod() 
  sys.exit(failure_count) 
