import matplotlib.pyplot as plt
import numpy as np

# ����һЩ�������
x = np.linspace(0, 10, 100)
y = np.sin(x)

# ����ͼ��
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Generated Image")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# ����ͼƬ
plt.savefig("image.png") # ��ͼƬ����Ϊ image.png