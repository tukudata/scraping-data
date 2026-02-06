import pandas as pd

df_raw = pd.read_csv(
    "prs-25-12-hke1.csv",
    header=None,
    dtype=str,
    keep_default_na=False
)

# data rows start at row 5 until row 10 (adjust if needed)
df_data = df_raw.iloc[5:11]

df = pd.DataFrame({
    "Nama Mitra": df_data[1],
    "Omset": df_data[4],
    "% Target": df_data[24],
})

print(df)
