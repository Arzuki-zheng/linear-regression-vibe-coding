import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Interactive Linear Regression", layout="wide")

st.title("📈 Interactive Linear Regression Visualizer")

# Sidebar controls
st.sidebar.header("Simulation Settings")
n_points = st.sidebar.slider("Number of data points", 20, 500, 100)
slope = st.sidebar.slider("Coefficient (slope)", -10.0, 10.0, 2.0)
intercept = st.sidebar.slider("Intercept", -10.0, 10.0, 5.0)
noise = st.sidebar.slider("Noise level", 0.0, 10.0, 2.0)

# Generate synthetic data
np.random.seed(42)
X = np.random.rand(n_points, 1) * 10
y = slope * X + intercept + np.random.randn(n_points, 1) * noise

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Layout
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

st.markdown("---")
st.markdown("Adjust the parameters in the sidebar to see how the regression line changes!")
