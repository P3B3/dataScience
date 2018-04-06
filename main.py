import numpy as np
import pandas as pd
import csv


countryCode = 'Country-Code-Mapping.csv'

printFile = pd.read_csv(countryCode)

print(printFile)
