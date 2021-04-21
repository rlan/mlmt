import numpy as np
import pandas as pd

#https://github.com/mverleg/array_storage_benchmark/
def np_save(data : np.ndarray, file_name : str) -> None:
  """Save numpy data to file

  See also: np_load
  """
  with open(file_name, 'wb+') as fh:
    np.save(fh, data, allow_pickle=False)

#https://github.com/mverleg/array_storage_benchmark/
def np_load(file_name : str) -> np.ndarray:
  """Load numpy data from file

  See also: np_save
  """
  return np.load(file_name)


def pd_save(data : pd.DataFrame, file_name : str) -> None:
  """Save Pandas DataFrame to hdf file

  See also: pd_load
  """
  data.to_hdf(file_name, key='df', mode='w')

def pd_load(file_name : str) -> pd.DataFrame:
  """Load Pandas DAtaFrame from hdf file.

  See also: pd_save
  """
  return pd.read_hdf(file_name, 'df')
