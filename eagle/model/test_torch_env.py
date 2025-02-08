#!/usr/bin/env python
# coding=utf-8
import torch  

# 检查 PyTorch 是否安装  
is_installed = torch.__version__ if 'torch' in locals() else '未安装 PyTorch'  
print(f"PyTorch 版本: {is_installed}")  

# 检查是否支持 CUDA  
cuda_available = torch.cuda.is_available()  
print(f"支持 CUDA: {cuda_available}")  

if cuda_available:  
    cuda_version = torch.version.cuda  
    print(f"CUDA 版本: {cuda_version}")  
else:  
    print("CUDA 不可用")  
