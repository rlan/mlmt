
try:
  import torch
  import torch.nn as nn
except ImportError as e:
  raise ImportError(
      "Could not import PyTorch! "
      "`pip install torch`."
  )


"""
Mixin's for PyTorch
"""
class NnModuleMixin:
  """Mixin for torch.nn.Module
  """

  def param_count(self, trainable=False):
    """Return total parameter count.
    """
    if trainable:
      total = sum(p.numel() for p in self.parameters() if p.requires_grad)
    else:
      total = sum(p.numel() for p in self.parameters())
    return total



class MlpLayer(nn.Module, NnModuleMixin):

  def __init__(self, input: int, output: int, activation: str = 'relu'):
    """A programmable multilayer perceptron (MLP) layer

    Parameters
    ----------
    input : int
        Size of each input sample.
    output : int
        Size of each output sample.
    activation : str
        Activation function. Choices: 'relu' (default), 'logsoftmax', 'sigmoid'.
    """
    super().__init__()
    self.layer = nn.Linear(input, output)
    self.bn = nn.BatchNorm1d(output)
    assert activation in ['relu', 'logsoftmax', 'sigmoid']
    if activation == 'relu':
      self.activation = nn.ReLU(inplace=True)
    elif activation == 'logsoftmax':
      self.activation = nn.LogSoftmax(dim=1)
    elif activation == 'sigmoid':
      self.activation = nn.Sigmoid()

  def forward(self, x):
    x = self.layer(x)
    x = self.bn(x)
    return self.activation(x)


class Mlp(nn.Module, NnModuleMixin):
  def __init__(self, 
      features: list,
      activation: str = 'relu',
      out_activation: str = 'logsoftmax',
  ):
    """A MLP network with programmable number of layers and activation functions.
    Batch norm and ReLU.

    Parameters
    ----------
    features : list[int]
        A variable-length list: [in, layer1_out, layer2_out, ..., , out]
    activation : str
        Activation function for non-output layer. Choices: 'relu' (default), 'logsoftmax', 'sigmoid'.
    out_activation : str
        Activation function for output layer. Choices: 'relu', 'logsoftmax' (default), 'sigmoid'.
    """
    super().__init__()
    assert len(features) >= 4, f"4 features is minimum (3 layers total and 1 hidden)."
    layers = []
    for ii in range(len(features)-2):
      layers.append(MlpLayer(features[ii], features[ii+1], activation=activation))
    self.features = nn.Sequential(*layers)
    self.output = MlpLayer(features[-2], features[-1], activation=out_activation)

  def forward(self, x):
    x = x.view(x.size(0), -1)
    x = self.features(x)
    return self.output(x)


if __name__ == "__main__":
  mlp = Mlp([784, 512, 256, 10], out_activation='logsoftmax')
  print(mlp)
  print(mlp.param_count())
