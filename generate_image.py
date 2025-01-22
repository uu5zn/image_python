import matplotlib.pyplot as plt
import numpy as np

# 生成一些随机数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图表
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Generated Image")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 保存图片
plt.savefig("image.png") # 将图片保存为 image.png