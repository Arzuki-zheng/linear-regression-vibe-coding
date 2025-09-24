# linear-regression-vibe-coding
使用ChatGPT實做一個線性迴歸程式並部署
# Interactive Linear Regression Visualizer

## 專案簡介
這是一個使用 Streamlit 開發的 Web 應用程式，能讓使用者互動式地視覺化線性回歸。  
使用者可以調整以下參數：
- 資料點數量
- 線性關係係數 (斜率)
- 雜訊量

並即時觀察這些變化如何影響回歸線與離群點辨識。

Demo 網站: [[https://aiotda.streamlit.app/](https://aiotda.streamlit.app/)](https://arzuki-zheng-linear-regression-vibe-coding-app-i3zznb.streamlit.app/)

---

## 開發過程
- 初始設定 (`0_devLog.md`, `Todo.md`)
- 修改並驗證專案計畫
- 建立 `app.py` 作為 Streamlit 主程式
- 設定虛擬環境與 `requirements.txt`
- 成功執行並部署至 Streamlit Cloud

---

## 線性回歸實作流程
1. **Data Preparation**
   - 載入資料集（CSV / NumPy array）
   - 處理缺失值
   - 拆分訓練 / 測試資料集
   - 特徵縮放（如需）

2. **Model Implementation**
   - 初始化權重與偏差
   - 定義假設函數 \( h(x) = wx + b \)
   - 定義成本函數（MSE）
   - 實作梯度下降（Gradient Descent）

3. **Training**
   - 使用訓練集訓練模型
   - 監控收斂（成本函數圖）

4. **Evaluation**
   - 測試集預測
   - 評估指標：MSE、R² Score
   - 視覺化預測 vs. 真實值

5. **Prediction**
   - 建立新資料預測函式

6. **Documentation and Reporting**
   - 撰寫程式文件
   - 撰寫報告：實作、結果與結論
