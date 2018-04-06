import numpy as np
import pandas as pd
import csv
from percent import percentage_of
from constValues import countryCode, surveyNumeric, \
    surveyCodebook, surveyNumericMapping, surveyValues

low_memory = False

numericFile = pd.read_csv(surveyNumeric)
respondentsRF = numericFile['CountryNumeric2'].value_counts().ix[138].astype(int)

print('Всего из РФ: ', respondentsRF)

studentsFromRF = (numericFile.loc[(numericFile['CountryNumeric2'] == 138) &
                                  (numericFile['q8Student'] == 1)])['q8Student'].value_counts().ix[1].astype(int)
print('Процент студентов из РФ: ', float('{:.2f}'.format(percentage_of(studentsFromRF, respondentsRF))))

# 138 код РФ
# q8Student = 1 значит студент

respondentsRoles = numericFile['q9CurrentRole'].value_counts().sum()
webDeveloperRoles = numericFile['q9CurrentRole'].value_counts().ix['1'].astype(int)
dataScientistRoles = numericFile['q9CurrentRole'].value_counts().ix['6'].astype(int)
mobileDeveloperRoles = numericFile['q9CurrentRole'].value_counts().ix['7'].astype(int)

print('Процент веб разработчиков: ', float('{:.2f}'.format(percentage_of(webDeveloperRoles, respondentsRoles))))
print('Процент дата разработчиков: ', float('{:.2f}'.format(percentage_of(dataScientistRoles, respondentsRoles))))
print('Процент моб разработчиков: ', float('{:.2f}'.format(percentage_of(mobileDeveloperRoles, respondentsRoles))))

print(numericFile['CountryNumeric2'].value_counts().ix[138])
