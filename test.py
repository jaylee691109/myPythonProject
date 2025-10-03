# 회귀: 주택 크기 → 가격 (scikit-learn)
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[30],[50],[80],[120]])   # m²  
y = np.array([200, 320, 520, 760])     # 가격(예시)
model = LinearRegression().fit(X, y)
print("예측(100m²):", model.predict([[100]])[0])