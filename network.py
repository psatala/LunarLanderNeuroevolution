import torch
import constants

class Network(torch.nn.Module):
    def __init__(self) -> None:
        super(Network, self).__init__()
        self.linear1 = torch.nn.Linear(constants.IN_FEATURES, 
            constants.N_HIDDEN)
        self.linear2 = torch.nn.Linear(constants.N_HIDDEN, 
            constants.OUT_FEATURES)

    def forward(self, x):
        h_relu = self.linear1(x).clamp(min=0)
        y_pred = self.linear2(h_relu)
        return y_pred
