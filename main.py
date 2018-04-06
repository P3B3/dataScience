import numpy as np
import pandas as pd
import csv
from constValues import countryCode, surveyNumeric, \
    surveyCodebook, surveyNumericMapping, surveyValues

low_memory = False

ValueFile = pd.read_csv(surveyValues)
newValueFile = ValueFile['CountryNumeric2'].value_counts()
print('Количество опрошенных из РФ:', newValueFile.ix['Russian Federation'])

