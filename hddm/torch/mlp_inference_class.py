import torch
from .torch_config import TorchConfig
import hddm

class LoadTorchMLPInfer:
    def __init__(self, 
                 model_file_path = None,
                 network_config = None,
                 input_dim = None):
        
        torch.backends.cudnn.benchmark = True
        self.dev = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        self.model_file_path = model_file_path
        self.network_config = network_config
        self.input_dim = input_dim
        
        self.net = TorchMLP(network_config = self.network_config,
                            input_shape = self.input_dim,
                            generative_model_id = None)
        self.net.load_state_dict(torch.load(self.model_file_path))
        self.net.to(self.dev)
        self.net.eval()
    
    @torch.no_grad()
    def predict_on_batch(self, x = None):
        return self.net(torch.from_numpy(x).to(self.dev)).cpu().numpy()

def load_torch_mlp(model = model):
    cfg = TorchConfig(model = model)
    infer_model  = LoadTorchMLPInfer(model_file_path  = cfg.network_path,
                                     network_config = cfg.network_config,
                                     input_dim = len(hddm.model_config.model_config[model]['params']) + 2, 
                                    )
    return infer_model