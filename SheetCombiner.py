import pandas as pd

main_csv = "Data/prb_data.csv"
hdi_csv = "Data/hdi_lookup.csv"
income_csv = "Data/income_groups_lookup.csv"
m49_csv = "Data/m49_lookup.csv"
output_csv = "Data/combined_data.csv"

df = pd.read_csv(main_csv)
m49_df = pd.read_csv(m49_csv)
income_df = pd.read_csv(income_csv)
hdi_df = pd.read_csv(hdi_csv)

m49_df["m49"] = (
    m49_df[["region", "subregion"]]
    .fillna("")
    .astype(str)
    .agg(",".join, axis=1)
)

df = df.merge(m49_df[["state", "m49"]], on="state", how="left")
df = df.merge(income_df[["state", "incomeGroup"]], on="state", how="left")
df = df.merge(hdi_df[["state", "hdiGroup"]], on="state", how="left")

df.to_csv(output_csv, sep="&", index=False)

print(f"Done! Output saved to {output_csv}")