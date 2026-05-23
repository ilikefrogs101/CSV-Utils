import pandas as pd

EXACT_MATCH = True
SEPARATOR = "&"

COLUMN = "hdiGroup"
VALUE = "Low"

df = pd.read_csv("Data/combined_data.csv", sep=SEPARATOR)

if EXACT_MATCH:
    df = df[df[COLUMN] == VALUE]
else:
    df = df[df[COLUMN].str.contains(VALUE, na=False)]

df.to_csv(f"Data/FilteredData/{VALUE}.csv", sep=SEPARATOR, index=False)