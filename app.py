import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 頁面設定
st.set_page_config(page_title="Interactive Linear Regression", layout="wide")

# ===== 封面區塊 =====
st.title("📈 Interactive Linear Regression Visualizer")

st.markdown("""
### 📝 作者資訊  
- 系級：中興大學資工系碩一  
- 學號：7114056186  
- 姓名：陳鉦元  

---
""")

# ===== 側邊參數設定 =====
st.sidebar.header("Simulation Settings")
n_points = st.sidebar.slider("Number of data points", 20, 500, 100)
slope = st.sidebar.slider("Coefficient (slope)", -10.0, 10.0, 2.0)
intercept = st.sidebar.slider("Intercept", -10.0, 10.0, 5.0)
noise = st.sidebar.slider("Noise level", 0.0, 10.0, 2.0)

# ===== 產生模擬資料 =====
np.random.seed(42)
X = np.random.rand(n_points, 1) * 10
y = slope * X + intercept + np.random.randn(n_points, 1) * noise

# ===== 建立與訓練模型 =====
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# ===== 計算評估指標 =====
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# ===== 頁面佈局 =====
col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(X, y, alpha=0.7, label="Data points")
    ax.plot(X, y_pred, color="red", linewidth=2, label="Regression line")
    ax.set_xlabel("X")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Model Results")
    st.write(f"**Fitted slope:** {model.coef_[0][0]:.3f}")
    st.write(f"**Fitted intercept:** {model.intercept_[0]:.3f}")
    st.write(f"**Mean Squared Error (MSE):** {mse:.3f}")
    st.write(f"**R² Score:** {r2:.3f}")

# ===== 底部說明 =====
st.markdown("---")
st.markdown("🔧 調整左側參數，觀察回歸線與數據分布的變化！")
st.caption("製作人：資工系碩一 A1234567 陳鉦元")
