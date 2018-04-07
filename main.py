import pandas as pd
import plotly.offline as offline
from percent import percentage_of
from formatNum import format_float_num
from constValues import survey_numeric

"""
respondentsRF  - количество опрошенных из РФ

.value_counts()
Returns object containing counts of unique values.
The resulting object will be in descending order so that the first element is 
the most frequently-occurring element. Excludes NA values by default.

.loc[]
Purely label-location based indexer for selection by label.

.astype()
Cast a pandas object to a specified type 
"""
numeric_file = pd.read_csv(survey_numeric, low_memory=False)
respondents_RF = numeric_file['CountryNumeric2'].value_counts().loc[138].astype(int)

# 138 RF country code
# q8Student = 1  => student
students_RF = (numeric_file.loc[(numeric_file['CountryNumeric2'] == 138) &
                                (numeric_file['q8Student'] == 1)])['q8Student'].value_counts().loc[1].astype(int)
stud_RF_percent = format_float_num(percentage_of(students_RF, respondents_RF))

"""
.sum()
Return the sum of the values for the requested axis
"""
respondents_roles = numeric_file['q9CurrentRole'].value_counts().sum()
web_dev_roles = numeric_file['q9CurrentRole'].value_counts().loc['1'].astype(int)
data_science_roles = numeric_file['q9CurrentRole'].value_counts().loc['6'].astype(int)
mobile_dev_roles = numeric_file['q9CurrentRole'].value_counts().loc['7'].astype(int)
web_dev_percent = format_float_num(percentage_of(web_dev_roles, respondents_roles))
data_science_dev = format_float_num(percentage_of(data_science_roles, respondents_roles))
mobile_dev_percent = format_float_num(percentage_of(mobile_dev_roles, respondents_roles))

"""
.count(axis=0)
Return Series with number of non-NA/null observations over requested axis. 
Works with non-floating point data as well (detects NaN and None)
    axis : {0 or ‘index’, 1 or ‘columns’}, default 0
        0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise
"""
true_answers_RF = numeric_file.loc[numeric_file['CountryNumeric2'] == 138].count(axis=1).min().astype(int)
answer_true_percent = format_float_num(percentage_of(true_answers_RF, respondents_RF))

"""
draw_charts()
Use Plotly Python graphing library to make interactive pie charts
Visit tutorial: https://plot.ly/python/pie-charts/
"""


def draw_charts():
    offline.plot({
        'data': [{'labels': ['Web-разработка', 'Data Science', 'Мобильная разработка', 'Другое'],
                  'values': [web_dev_percent, data_science_dev, mobile_dev_percent,
                             100 - (web_dev_percent + data_science_dev + mobile_dev_percent)],
                  'type': 'pie',
                  "domain": {"x": [.52, 1],
                             "y": [.51, 1]},
                  "hole": .5,
                  'name': 'Чем занимаются опрошенные',
                  "hoverinfo": "label+percent+name"
                  },
                 {
                     'labels': ['Правильно', 'Не правильно'],
                     'values': [answer_true_percent, 100 - answer_true_percent],
                     'type': 'pie',
                     "domain": {"x": [.52, 1],
                                "y": [0, .49]},
                     "hole": .5,
                     'name': 'Ответы на все вопросы участников из России',
                     "hoverinfo": "label+percent+name"
                 },
                 {
                     'labels': ['Студенты', 'Другое'],
                     'values': [stud_RF_percent, 100 - stud_RF_percent],
                     'type': 'pie',
                     "domain": {"x": [0, .48],
                                "y": [.51, 1]},
                     "hole": .5,
                     'name': str(respondents_RF) + ' участников опроса из России',
                     "hoverinfo": "label+percent+name"
                 }],
        'layout': {'title': 'Data Science'}
    })


draw_charts()
