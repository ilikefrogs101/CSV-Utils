import pandas as pd

file_path = "Data/FilteredData/High.csv"
columns_to_analyze = ["familyPlanning", "tfr"]
group_column = "state" 

df = pd.read_csv(file_path,sep='&')

for col in columns_to_analyze:
    series = df[col]

    mean = series.mean()
    median = series.median()
    mode = series.mode().iloc[0] if not series.mode().empty else None
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    std = series.std()
    min_val = series.min()
    max_val = series.max()

    range_val = max_val - min_val

    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = df[(series < lower) | (series > upper)][[group_column, col]]

    print(f"\n================ {col} ================\n")
    print(f"Mean: {mean}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std}")
    print(f"Min: {min_val}")
    print(f"Q1: {q1}")
    print(f"Median: {median}")
    print(f"Q3: {q3}")
    print(f"Max: {max_val}")

    print("\nOutliers:")
    if outliers.empty:
        print("None")
    else:
        print(outliers.to_string(index=False))