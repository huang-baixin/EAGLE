import subprocess

# 定义要运行的命令
command = ["python3", "-m", "eagle.evaluation.gen_ea_answer_llama3chat"]

# 运行命令
result = subprocess.run(command, capture_output=True, text=True)

# 打印输出和错误信息
print("标准输出:")
print(result.stdout)
print("标准错误:")
print(result.stderr)

# 打印返回码
print(f"返回码: {result.returncode}")