import numpy as np
import pandas as pd
import csv
from percent import percentage_of
from formatNum import format_float_num
from constValues import countryCode, surveyNumeric, \
    surveyCodebook, surveyNumericMapping, surveyValues

low_memory = False
# 138 код РФ
# q8Student = 1 значит студент

numericFile = pd.read_csv(surveyNumeric)
respondentsRF = numericFile['CountryNumeric2'].value_counts().ix[138].astype(int)
print('Всего из РФ: ', respondentsRF)

studentsFromRF = (numericFile.loc[(numericFile['CountryNumeric2'] == 138) &
                                  (numericFile['q8Student'] == 1)])['q8Student'].value_counts().ix[1].astype(int)
print('Процент студентов из РФ: ', format_float_num(percentage_of(studentsFromRF, respondentsRF)))

respondentsRoles = numericFile['q9CurrentRole'].value_counts().sum()
webDeveloperRoles = numericFile['q9CurrentRole'].value_counts().ix['1'].astype(int)
dataScientistRoles = numericFile['q9CurrentRole'].value_counts().ix['6'].astype(int)
mobileDeveloperRoles = numericFile['q9CurrentRole'].value_counts().ix['7'].astype(int)
print('Процент веб разработчиков: ', format_float_num(percentage_of(webDeveloperRoles, respondentsRoles)))
print('Процент дата разработчиков: ', format_float_num(percentage_of(dataScientistRoles, respondentsRoles)))
print('Процент моб разработчиков: ', format_float_num(percentage_of(mobileDeveloperRoles, respondentsRoles)))

trueAnswersRF = numericFile.loc[numericFile['CountryNumeric2'] == 138].count(axis=1).min().astype(int)
print('Процент правильно ответивших из РФ: ', format_float_num(percentage_of(trueAnswersRF, respondentsRF)))
