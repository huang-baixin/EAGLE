# pip install safetensors transformers 
from safetensors.torch import load_file
import torch

# 加载 .safetensors 文件
safetensors_file_path = "path/to/your/model.safetensors"
state_dict = load_file(safetensors_file_path)

# 保存为 .bin 文件
bin_file_path = "path/to/save/model.bin"
torch.save(state_dict, bin_file_path)