# 📊 Student Stress Analyzer

A simple, practical data project to explore **student stress** using Python. It covers:
- Clean EDA (summary, missing values, top anxiety students)
- Clear visuals (distributions + correlations with stress)
- Optional starter ML (linear regression)
- Reproducible outputs (saved to `outputs/`)

## 🚀 Tech
Python, Pandas, Matplotlib, Seaborn, (optional) scikit-learn.

## 📊 Visualizations

Here are the key graphs from the analysis:

1. **Stress Level Distribution**
   ![Stress Distribution](## 📊 Visualizations

Here are the key graphs from the analysis:

1. **Stress Level Distribution**
   ![Stress Distribution](outputs/anxiety_level_distribution.png)

2. **Stress by Gender**
   ![Stress by Gender](outputs/graph2_gender.png)

3. **Correlation Heatmap**
   ![Correlation Heatmap](outputs/graph3_corr.png)

4. **Sleep vs Stress**
   ![Sleep vs Stress](outputs/graph4_sleep.png)

5. **Study Hours vs Stress**
   ![Study Hours vs Stress](outputs/graph5_study.png)
)

2. **Stress by Gender**
   ![Stress by Gender](outputs/graph2_gender.png)

3. **Correlation Heatmap**
   ![Correlation Heatmap](outputs/graph3_corr.png)

4. **Sleep vs Stress**
   ![Sleep vs Stress](outputs/graph4_sleep.png)

5. **Study Hours vs Stress**
   ![Study Hours vs Stress](outputs/graph5_study.png)


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
