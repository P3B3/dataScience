import numpy as np
import pandas as pd
import csv
from constValues import countryCode, surveyNumeric, \
    surveyCodebook, surveyNumericMapping, surveyValues

low_memory = False
"""
ValueFile = pd.read_csv(surveyValues)
newValueFile = ValueFile['CountryNumeric2'].value_counts()
print(ValueFile)
print('Количество опрошенных из РФ:', newValueFile.ix['Russian Federation'])
"""
numericFile = pd.read_csv(surveyNumeric)
valueFile = pd.read_csv(surveyValues)
respondentsRF = valueFile['CountryNumeric2'].value_counts().ix['Russian Federation']
print('Всего из РФ: ', respondentsRF)
studentsFromRF = numericFile.loc[(numericFile['CountryNumeric2'] == 138) & (numericFile['q8Student'] == 1)]
print('Процент студентов из РФ: ', ((studentsFromRF['q8Student'].value_counts().ix[1]) / respondentsRF) * 100)
# 138 код РФ
# q8Student = 1 значит студент
