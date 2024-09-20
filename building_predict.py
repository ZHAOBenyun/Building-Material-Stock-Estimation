import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 扩展示例数据 (输入数据：楼高，俯视投影面积，整体体积)
X = np.array([
    [10, 200, 2000], [15, 300, 4500], [20, 400, 8000], [12, 250, 3000],
    [18, 350, 6000], [22, 450, 9000], [25, 500, 11000], [30, 550, 13000],
    [8, 180, 1600], [14, 280, 4200], [28, 530, 12500], [19, 360, 6800]
])

# 扩展输出数据：混凝土用量，钢筋用量，以及一个新的输出特征
y = np.array([
    [500, 50, 30], [900, 80, 40], [1600, 120, 60], [700, 60, 35],
    [1400, 100, 50], [1800, 140, 65], [2200, 160, 75], [2600, 180, 85],
    [450, 45, 28], [950, 85, 42], [2500, 175, 80], [1500, 110, 55]
])

# 数据集划分
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # 对训练集进行标准化
X_val = scaler.transform(X_val)  # 对验证集进行标准化
X_test = scaler.transform(X_test)  # 对测试集进行标准化

# 初始化和训练模型
model = MLPRegressor(hidden_layer_sizes=(12, 8, 5), activation='relu', solver='adam', alpha=0.001, 
                     learning_rate_init=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, max_iter=1000, random_state=42)

# 训练模型
model.fit(X_train, y_train)

# 评估模型
y_pred_val = model.predict(X_val)
mse_val = mean_squared_error(y_val, y_pred_val)
mae_val = mean_absolute_error(y_val, y_pred_val)
print(f'Validation MSE: {mse_val}, Validation MAE: {mae_val}')

# 测试模型
y_pred_test = model.predict(X_test)
mse_test = mean_squared_error(y_test, y_pred_test)
mae_test = mean_absolute_error(y_test, y_pred_test)
print(f'Test MSE: {mse_test}, Test MAE: {mae_test}')

# 新数据预测
new_data = np.array([[14, 280, 3800]])  # 新建筑物数据
new_data_scaled = scaler.transform(new_data)  # 对新数据进行标准化
predicted_output = model.predict(new_data_scaled)
print(f'Predicted Concrete, Steel Quantity, and New Feature (tons): {predicted_output}')