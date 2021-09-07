import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_excel('Pinch_data/streams.xlsx')
df["CP"] = (df["Cpin_especifico [kJ/kg.K]"]+df["Cpout_especifico [kJ/kg.K]"])/2

df_PyPinch = DataFrame()

df_PyPinch["CP"] = df["CP"]*df["caudal_masico [kg/hr]"]*0.278/1000
df_PyPinch["TSUPPLY"] = df["Tin [°C]"]
df_PyPinch["TTARGET"] = df["Tout [°C]"]
df_PyPinch.to_csv("Pinch_data/pypinch_input.csv", index=False)

with open("Pinch_data/pypinch_input.csv", "r") as f:
    prev_text = f.readlines()
with open("Pinch_data/pypinch_input.csv", "w+") as f:
    f.write("Tmin, 10, \n")
    f.writelines(prev_text)
