from pathlib import Path
import pandas as pd

carspath = Path(__file__).resolve().parent.parent / "data" / "cars.csv"
burnpath = Path(__file__).resolve().parent.parent / "data" / "burn.csv"



cs1 = pd.read_csv(carspath)
cs2 = pd.read_csv(burnpath)

print(cs1)
print("----------------------------------\n-------------------------------------------\n----------------------------------------")
print(cs2.describe())