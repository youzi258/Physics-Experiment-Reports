import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（以黑体为例，确保系统已安装）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 实验数据
t = np.array([10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0])  # 温度 / °C
L = np.array([1.003, 1.005, 1.008, 1.010, 1.014, 1.016, 1.018, 1.021])  # 长度 / mm

# 最小二乘法拟合 y = a + b*x
x_mean = np.mean(t)
y_mean = np.mean(L)
xy_mean = np.mean(t * L)
x2_mean = np.mean(t ** 2)

b = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2)
a = y_mean - b * x_mean

# 计算相关系数 r
y2_mean = np.mean(L ** 2)
r_numer = xy_mean - x_mean * y_mean
r_denom = np.sqrt((x2_mean - x_mean ** 2) * (y2_mean - y_mean ** 2))
r = r_numer / r_denom

print(f"拟合结果：L = {a:.4f} + {b:.6f} * t")
print(f"相关系数 r = {r:.4f}")

# 生成拟合直线
t_fit = np.linspace(5, 50, 100)
L_fit = a + b * t_fit

# 绘图
plt.figure(figsize=(12, 9))
plt.scatter(t, L, color='red', marker='o', s=80, label='实验数据点')
plt.plot(t_fit, L_fit, color='blue', linestyle='-', linewidth=2, label='最小二乘拟合')

# 左上角添加个人信息文本框
info_text = '物理实验绪论作业曲线\n姓名: ***\n班级: ********\n日期: 26-03-13'
plt.text(0.05, 0.85, info_text, transform=plt.gca().transAxes,
         fontsize=14, verticalalignment='top', horizontalalignment='left',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# 原拟合方程框下移（从 y=0.95 移至 y=0.80）
eq_text = f'$L = {a:.4f} + {b:.6f}\,t$\n$r = {r:.4f}$'
plt.text(0.95, 0.80, eq_text, transform=plt.gca().transAxes,
         fontsize=14, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 坐标轴标签
plt.xlabel('$t$ / °C', fontsize=16)
plt.ylabel('$L$ / mm', fontsize=16)
plt.title('金属丝长度与温度关系', fontsize=18, fontweight='bold')

plt.legend(loc='upper left', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()