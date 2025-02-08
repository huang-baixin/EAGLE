
# pip install modelscope
# modelscope download --model LLM-Research/Llama-3.2-1B

#模型下载
from modelscope.hub.snapshot_download import snapshot_download

# 指定模型的名称
model_name = "LLM-Research/Llama-3.2-1B"

# 下载模型到指定路径
output_dir = "./"
snapshot_download(model_name)

print(f"模型已下载")

# 下载单个文件
# modelscope download --model LLM-Research/Llama-3.2-1B model.safetensors --local_dir ./

# from safetensors.torch import load_file
# import torch

# # 加载 .safetensors 文件
# safetensors_file_path = "./downloaded_model/model.safetensors"
# state_dict = load_file(safetensors_file_path)

# # 保存为 .bin 文件
# bin_file_path = "./downloaded_model/model.bin"
# torch.save(state_dict, bin_file_path)
