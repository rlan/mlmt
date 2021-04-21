import numpy as np


def as_string(data: any) -> str:
  """Inspect data based on type
  """

  ret = "type {}".format(type(data))
  if isinstance(data, list):
    ret += " len {}".format(len(data))
  elif isinstance(data, tuple):
    ret += " len {}".format(len(data))
  elif isinstance(data, dict):
    ret += " keys len {} {}".format(len(data.keys()), data.keys())
  elif isinstance(data, np.ndarray):
    ret += " shape {} dtype {}".format(data.shape, data.dtype)

  return ret
