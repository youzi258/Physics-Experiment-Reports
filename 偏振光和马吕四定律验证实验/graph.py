import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（以黑体为例，确保系统已安装）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 实验数据
theta = np.array([0, 15, 30, 45, 60, 75, 90])  # 角度 / °
cos2 = np.array([1.000, 0.933, 0.750, 0.500, 0.250, 0.067, 0.000])  # cos²θ
P = np.array([3.110, 2.820, 2.250, 1.570, 0.730, 0.180, 0.004])  # 光强 / mW
Pmin = 0.002  # 最小光强
P_corrected = P - Pmin  # 修正后的光强

# 拟合
coef = np.polyfit(cos2, P_corrected, 1)  # 线性拟合
fit_line = np.poly1d(coef)

# 绘图
plt.figure(figsize=(12, 9))
plt.scatter(cos2, P_corrected, color='red', marker='o', s=80, label='实验数据点')  # 数据点
plt.plot(cos2, fit_line(cos2), color='blue', linestyle='-', linewidth=2, label='最小二乘拟合')  # 拟合直线

# 在图中添加拟合方程文本
eq_text = f'$P = {coef[0]:.3f} * cos^2(θ) + {coef[1]:.3f}$'
plt.text(0.95, 0.95, eq_text, transform=plt.gca().transAxes,
         fontsize=14, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 坐标轴标签和标题
plt.xlabel('$cos^2(θ)$', fontsize=16)
plt.ylabel('P - Pmin (mW)', fontsize=16)
plt.title('马吕斯定律验证实验', fontsize=18, fontweight='bold')

# 添加实验数据来源标注
info_text  = '偏振光鉴别与麻吕斯定律验证实验\n姓名: ****\n班级:*********\n日期: 26-03-17'
plt.text(0.05, 0.85, info_text, transform=plt.gca().transAxes,
         fontsize=14, verticalalignment='top', horizontalalignment='left',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# 绘制网格和图例
plt.legend(loc='upper left', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# 显示图像
plt.show()

print("拟合结果：P = {:.3f} * cos²(θ) + {:.3f}".format(coef[0], coef[1]))
