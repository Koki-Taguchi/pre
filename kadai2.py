import numpy as np

# 座標aと座標b
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])

# ユークリッド距離を計算
dist = np.linalg.norm(a - b)

print(dist)
