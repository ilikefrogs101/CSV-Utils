import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv("Data/FilteredData/High.csv", sep="&")

df["familyPlanning"] = pd.to_numeric(df["familyPlanning"], errors="coerce")
df["tfr"] = pd.to_numeric(df["tfr"], errors="coerce")

clean_df = df.dropna(subset=["familyPlanning", "tfr"])

l1 = clean_df["familyPlanning"]
l2 = clean_df["tfr"]
r, p_value = pearsonr(l1, l2)

print(f"Correlation: {r}")
print(f"P-value: {p_value}\n")