import pandas as pd
from unidecode import unidecode

INPUT_FILE = "Data/Raw/hdi_lookup.csv"
OUTPUT_FILE = "Data/hdi_lookup.csv"

COLUMN_RENAMES = {
    "country": "state",
    "tier_hdi": "hdiGroup",
}
COLUMNS_TO_KEEP = [
    "state",
    "hdiGroup",
]

df = pd.read_csv(INPUT_FILE, dtype=str, encoding="utf-8").fillna("")

df = df.apply(lambda col: col.map(lambda x: unidecode(str(x))))
df = df.rename(columns=COLUMN_RENAMES)
df = df[[col for col in COLUMNS_TO_KEEP if col in df.columns]]

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print("Sanitised ", INPUT_FILE, "to ", OUTPUT_FILE)