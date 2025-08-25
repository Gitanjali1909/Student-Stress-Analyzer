import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


class StudentStressAnalyzer:
    def __init__(self, file_path: str):
        """Initialize with dataset"""
        self.df = pd.read_csv(file_path)

    def show_summary(self):
        """Return summary statistics of numeric columns"""
        return self.df.describe()

    def check_missing_values(self):
        """Check for missing/null values"""
        return self.df.isnull().sum()

    def top_anxiety_students(self, n: int = 5):
        """Return top n students with the highest anxiety_level"""
        if "anxiety_level" not in self.df.columns:
            raise ValueError("Column 'anxiety_level' not found in dataset.")
        return self.df.nlargest(n, "anxiety_level")

    def plot_column_distribution(self, column_name: str, save: bool = False):
        """Plot and (optionally) save a bar chart for a column's distribution"""
        if column_name not in self.df.columns:
            raise ValueError(f"Column '{column_name}' not found in dataset.")

        fig, ax = plt.subplots(figsize=(6, 4))

        counts = self.df[column_name].value_counts().sort_index()
        counts.plot(kind="bar", color="#3498db", ax=ax)

        ax.set_title(f"{column_name} Distribution")
        ax.set_ylabel("Count")
        ax.set_xlabel(column_name)

        # Make x-axis labels vertical
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

        plt.tight_layout()

        if save:
            plt.savefig(f"outputs/{column_name}_distribution.png")
        plt.show()
        plt.close(fig)

    def plot_correlation_with_stress(self, save: bool = False):
        """Plot correlation of all features with stress_level"""
        if "stress_level" not in self.df.columns:
            raise ValueError("Column 'stress_level' not found in dataset.")

        corr = self.df.corr(numeric_only=True)["stress_level"].drop("stress_level")

        fig, ax = plt.subplots(figsize=(8, 5))
        corr.sort_values().plot(kind="bar", color="#e74c3c", ax=ax)

        ax.set_title("Correlation of Features with Stress Level")
        ax.set_ylabel("Correlation Coefficient")

        # x-axis labels vertical
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

        plt.tight_layout()

        if save:
            plt.savefig("outputs/stress_correlation.png")
        plt.show()
        plt.close(fig)

    def train_linear_regression(self, features, target="stress_level"):
        """Train a simple linear regression model and return metrics"""
        if target not in self.df.columns:
            raise ValueError(f"Target '{target}' not found in dataset.")

        X = self.df[features]
        y = self.df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Save predictions
        results = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
        results.to_csv("outputs/predictions.csv", index=False)

        return {"MAE": mae, "R2 Score": r2}

    def save_results(self, path: str = "outputs/analysis_results.csv"):
        """Save the current dataframe to CSV"""
        self.df.to_csv(path, index=False)
