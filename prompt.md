# Prompt 記錄

## 專案名稱
**Interactive Linear Regression Visualizer**  
這是一個使用 Streamlit 開發的 Web 應用程式，能讓使用者互動式地視覺化線性回歸。使用者可以調整參數（資料點數量、線性關係係數、雜訊量），並即時觀察這些變化如何影響回歸線與離群點的辨識。

## Demo Site
應用程式已部署在 Streamlit Cloud：  
🔗 https://aiotda.streamlit.app/

## Project Summary
此專案的開發目標是提供一個互動式工具來理解線性回歸。  
主要步驟：
- 建立 Streamlit 應用程式  
- 創建虛擬環境  
- 安裝依賴套件  
- 實作核心功能  
- 最後部署至 Streamlit Cloud  

## Development Log （依據 0_devLog.md）
- **1.0–2.0**: 初始化設定，建立 `0_devLog.md` 與 `Todo.md`  
- **3.0–4.0**: 修改與驗證專案計畫  
- **5.0**: 執行計畫，建立 `app.py` (Streamlit 應用程式)  
- **6.0–11.0**: 解決執行問題，建立 `requirements.txt`、設置虛擬環境、安裝依賴  
- **12.0–13.0**: 成功執行 Streamlit 應用程式  

## To-Do List for Linear Regression Implementation （依據 Todo.md）

### 1. Data Preparation
- 載入資料集（CSV / NumPy array）  
- 處理缺失值（若有）  
- 拆分訓練 / 測試資料集  
- 特徵縮放（如需，例：StandardScaler）  

### 2. Model Implementation
- 從零實作 Linear Regression（如需要）  
- 初始化權重與偏差  
- 定義假設函數 \( h(x) = wx + b \)  
- 定義成本函數（MSE）  
- 使用梯度下降法（Gradient Descent）最佳化  
  - 計算梯度  
  - 更新權重與偏差  

### 3. Training
- 使用訓練集訓練模型  
- 監控收斂情況（例：繪製成本函數變化圖）  

### 4. Evaluation
- 在測試集上做預測  
- 計算評估指標：  
  - MSE  
  - R² Score  
- 視覺化預測 vs. 真實值  

### 5. Prediction
- 建立函式，能對新資料做預測  

### 6. Documentation and Reporting
- 撰寫程式文件  
- 撰寫報告：總結實作、結果與結論
