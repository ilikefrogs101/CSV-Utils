import subprocess
import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv("Data/FilteredData/Low.csv", sep="&")

df["familyPlanning"] = pd.to_numeric(df["familyPlanning"], errors="coerce")
df["tfr"] = pd.to_numeric(df["tfr"], errors="coerce")

clean_df = df.dropna(subset=["familyPlanning", "tfr"])

l1 = clean_df["familyPlanning"]
l2 = clean_df["tfr"]

r, p_value = pearsonr(l1, l2)

n = len(clean_df)

if p_value < .001:
    p_text = "p < .001"
else:
    p_text = f"p = {p_value:.3f}"

r_text = f"r({n - 2}) = {r:.2f}, {p_text}.".replace("0.", ".")

print(r_text)