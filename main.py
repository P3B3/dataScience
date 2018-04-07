import pandas as pd
import plotly.offline as offline
from percent import percentage_of
from formatNum import format_float_num
from constValues import survey_numeric

# 138 код РФ
# q8Student = 1 значит студент
"""
respondentsRF  - количество опрошенных из РФ
"""
numeric_file = pd.read_csv(survey_numeric, low_memory=False)
respondents_RF = numeric_file['CountryNumeric2'].value_counts().ix[138].astype(int)
"""

"""
students_RF = (numeric_file.loc[(numeric_file['CountryNumeric2'] == 138) &
                                (numeric_file['q8Student'] == 1)])['q8Student'].value_counts().ix[1].astype(int)
stud_RF_percent = format_float_num(percentage_of(students_RF, respondents_RF))
"""

"""
respondents_roles = numeric_file['q9CurrentRole'].value_counts().sum()
web_dev_roles = numeric_file['q9CurrentRole'].value_counts().ix['1'].astype(int)
data_science_roles = numeric_file['q9CurrentRole'].value_counts().ix['6'].astype(int)
mobile_dev_roles = numeric_file['q9CurrentRole'].value_counts().ix['7'].astype(int)
web_dev_percent = format_float_num(percentage_of(web_dev_roles, respondents_roles))
data_science_dev = format_float_num(percentage_of(data_science_roles, respondents_roles))
mobile_dev_percent = format_float_num(percentage_of(mobile_dev_roles, respondents_roles))
"""

"""
trueAnswersRF = numeric_file.loc[numeric_file['CountryNumeric2'] == 138].count(axis=1).min().astype(int)
answerTruePercent = format_float_num(percentage_of(trueAnswersRF, respondents_RF))

"""

"""


def draw_charts():
    offline.plot({
        'data': [{'labels': ['Web-разработка', 'Data Science', 'Мобильная разработка', 'Другое'],
                  'values': [web_dev_percent, data_science_dev, mobile_dev_percent, 100 - (web_dev_percent + data_science_dev + mobile_dev_percent)],
                  'type': 'pie',
                  "domain": {"x": [.52, 1],
                             "y":[.51, 1]},
                  "hole": .5,
                  'name':'Чем занимаются опрошенные',
                  "hoverinfo": "label+percent+name"
                  },
                 {
                     'labels': ['Правильно', 'Не правильно'],
                     'values': [answerTruePercent, 100 - answerTruePercent],
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

