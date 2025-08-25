from analyzer.analyzer import StudentStressAnalyzer


def main():
    file_path = "data/StressLevelDataset.csv"
    analyzer = StudentStressAnalyzer(file_path)

    print("\n--- Dataset Summary ---")
    print(analyzer.show_summary())

    print("\n--- Missing Values Check ---")
    print(analyzer.check_missing_values())

    print("\n--- Top 5 Students by Anxiety Level ---")
    print(analyzer.top_anxiety_students())

    print("\n--- Plotting Distributions ---")
    for col in ["anxiety_level", "self_esteem", "depression", "sleep_quality"]:
        analyzer.plot_column_distribution(col, save=True)

    print("\n--- Correlation with Stress Level ---")
    analyzer.plot_correlation_with_stress(save=True)

    print("\n--- Training Linear Regression Model ---")
    metrics = analyzer.train_linear_regression(
        features=["study_hours", "sleep_quality", "self_esteem", "depression"]
    )
    print("Model Performance:", metrics)

    analyzer.save_results()
    print("\n✅ Analysis complete. Results & plots saved in outputs/")


if __name__ == "__main__":
    main()
