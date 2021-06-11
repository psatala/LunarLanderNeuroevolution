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


    def get_params(self):
        state_dict = self.state_dict()
        flat_param_array = torch.cat([
            state_dict["linear1.weight"].flatten(), 
            state_dict["linear1.bias"].flatten(), 
            state_dict["linear2.weight"].flatten(), 
            state_dict["linear2.bias"].flatten()]).detach().numpy()
        return flat_param_array


    def set_params(self, flat_param_array):
        state_dict = self.state_dict()
        
        state_dict["linear1.weight"] = torch.from_numpy(flat_param_array[
            : constants.IN_FEATURES * constants.N_HIDDEN]).reshape(
            constants.N_HIDDEN, constants.IN_FEATURES) 
        flat_param_array = flat_param_array[
            constants.IN_FEATURES * constants.N_HIDDEN :]
        
        state_dict["linear1.bias"] = torch.from_numpy(flat_param_array[
            : constants.N_HIDDEN])
        flat_param_array = flat_param_array[constants.N_HIDDEN :]

        state_dict["linear2.weight"] = torch.from_numpy(flat_param_array[
            : constants.N_HIDDEN * constants.OUT_FEATURES]).reshape(
            constants.OUT_FEATURES, constants.N_HIDDEN) 
        flat_param_array = flat_param_array[
            constants.N_HIDDEN * constants.OUT_FEATURES :]
        
        state_dict["linear2.bias"] = torch.from_numpy(flat_param_array[
            : constants.OUT_FEATURES])
        flat_param_array = flat_param_array[constants.OUT_FEATURES :]

        self.load_state_dict(state_dict)


    # helper function to check if get_params and set_params work correctly    
    def __eq__(self, other: object) -> bool:
        for i, j in zip(self.state_dict().items(), other.state_dict().items()):
            if i[0] != j[0] or not torch.equal(i[1], j[1]):
                return False
        return True
