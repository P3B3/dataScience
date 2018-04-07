import pandas as pd
import plotly
import plotly.offline as offline
from percent import percentage_of
from formatNum import format_float_num
from constValues import surveyNumeric

# 138 код РФ
# q8Student = 1 значит студент

numericFile = pd.read_csv(surveyNumeric, low_memory=False)
respondentsRF = numericFile['CountryNumeric2'].value_counts().ix[138].astype(int)
print('Всего из РФ: ', respondentsRF)

studentsFromRF = (numericFile.loc[(numericFile['CountryNumeric2'] == 138) &
                                  (numericFile['q8Student'] == 1)])['q8Student'].value_counts().ix[1].astype(int)
studPercent = format_float_num(percentage_of(studentsFromRF, respondentsRF))
print('Процент студентов из РФ: ', studPercent)

respondentsRoles = numericFile['q9CurrentRole'].value_counts().sum()
webDeveloperRoles = numericFile['q9CurrentRole'].value_counts().ix['1'].astype(int)
dataScientistRoles = numericFile['q9CurrentRole'].value_counts().ix['6'].astype(int)
mobileDeveloperRoles = numericFile['q9CurrentRole'].value_counts().ix['7'].astype(int)
webPercent = format_float_num(percentage_of(webDeveloperRoles, respondentsRoles))
dataPercent = format_float_num(percentage_of(dataScientistRoles, respondentsRoles))
mobPercent = format_float_num(percentage_of(mobileDeveloperRoles, respondentsRoles))
print('Процент веб разработчиков: ', webPercent)
print('Процент дата разработчиков: ', dataPercent)
print('Процент моб разработчиков: ', mobPercent)

trueAnswersRF = numericFile.loc[numericFile['CountryNumeric2'] == 138].count(axis=1).min().astype(int)
answerTruePercent = format_float_num(percentage_of(trueAnswersRF, respondentsRF))
print('Процент правильно ответивших из РФ: ', answerTruePercent)


def draw_charts():
    offline.plot({
        'data': [{'labels': ['Web-разработка', 'Data Science', 'Мобильная разработка', 'Другое'],
                  'values': [webPercent, dataPercent, mobPercent, 100 - (webPercent + dataPercent + mobPercent)],
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
                     'values': [studPercent, 100 - studPercent],
                     'type': 'pie',
                     "domain": {"x": [0, .48],
                                "y": [.51, 1]},
                     "hole": .5,
                     'name': str(respondentsRF) + ' участников опроса из России',
                     "hoverinfo": "label+percent+name"
                 }],
        'layout': {'title': 'Data Science'}
    })


draw_charts()

