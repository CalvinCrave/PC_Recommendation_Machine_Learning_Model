import pandas as pd

alpha = pd.read_json (r'E:\BANGKIT\AIRO\DATASET JSON\power-supply.json')
beta = alpha.to_csv(r'E:\BANGKIT\AIRO\DATASET CSV\powerSupplyParts.csv', index=0)

print(alpha)