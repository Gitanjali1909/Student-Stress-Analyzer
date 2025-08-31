# 📊 Student Stress Analyzer

A simple, practical data project to explore **student stress** using Python. It covers:
- Clean EDA (summary, missing values, top anxiety students)
- Clear visuals (distributions + correlations with stress)
- Reproducible outputs (saved to `outputs/`)

## 🚀 Tech
Python, Pandas, Matplotlib, Seaborn, (optional) scikit-learn.
Kaggle: [https://www.kaggle.com/code/gitanjalisoni/stress-analyzer]

## 📊 Visualizations

Here are the key graphs from the analysis:

1. **Stress Level Distribution**
   ## 📊 Visualizations

Here are the key graphs from the analysis:

1. **Stress Level Distribution**
   ![Stress Distribution](outputs/anxiety_level_distribution.png)

2. **Self Esteem Distribution**
   ![Self Esteem Distribution](outputs/self_esteem_distribution.png)

3. **Depression Distribution**
   ![Depression Distribution](outputs/depression_distribution.png)

4. **Sleep Quality**
   ![Sleep Quality](outputs/sleep_quality_distribution.png)

5. **Stress Correlation**
   ![Stress Correlation](outputs/stress_correlation.png)
   
## 📑 Dataset
- **Student Stress Level Dataset** (Kaggle). [https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets].

## ⚙️ Setup
```bash
1) create & activate venv
python -m venv .venv
# Windows
.venv\Scripts\activate

# 2) install deps
pip install -r requirements.txt

▶️ Run
python main.py
