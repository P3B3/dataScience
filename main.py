import numpy as np
import pandas as pd
import csv
from percent import percentage_of
from constValues import countryCode, surveyNumeric, \
    surveyCodebook, surveyNumericMapping, surveyValues

low_memory = False

numericFile = pd.read_csv(surveyNumeric)
valueFile = pd.read_csv(surveyValues)
respondentsRF = valueFile['CountryNumeric2'].value_counts().ix['Russian Federation'].astype(int)
print('Всего из РФ: ', respondentsRF)
studentsFromRF = (numericFile.loc[(numericFile['CountryNumeric2'] == 138) &
                                  (numericFile['q8Student'] == 1)])['q8Student'].value_counts().ix[1].astype(int)
print('Процент студентов из РФ: ', float('{:.2f}'.format(percentage_of(studentsFromRF, respondentsRF))))


# 138 код РФ
# q8Student = 1 значит студент

