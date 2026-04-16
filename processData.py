import pandas as pd
import glob

# need to load all 3 csv files, set the colum names, keep only pink morsels
# string the data and calculate sales. keep only the columns we need
# and finally save the data to our output file

files = glob.glob("data/*.csv")
df = pd.concat([
    pd.read_csv(f, header=None, names=["product", "price", "quantity", "date", "region"])
    for f in files
], ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["quantity"] = df["quantity"].astype(int)

df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv("data/output.csv", index=False)

print("Done! output.csv created.")
