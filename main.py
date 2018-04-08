import pandas as pd
import plotly.offline as offline
from percent import percentage_of
from formatNum import format_float_num
from constValues import survey_numeric, survey_codebook, survey_values

"""
.value_counts()
Returns object containing counts of unique values.
The resulting object will be in descending order so that the first element is 
the most frequently-occurring element. Excludes NA values by default.

.loc[]
Purely label-location based indexer for selection by label.

.astype()
Cast a pandas object to a specified type 

respondentsRF  - respondents from Russia
"""
numeric_file = pd.read_csv(survey_numeric, low_memory=False)
code_file = pd.read_csv(survey_codebook, low_memory=False)
values_file = pd.read_csv(survey_values, low_memory=False)
respondents_RF = numeric_file['CountryNumeric2'].value_counts().loc[138].astype(int)

# 138 RF country code
# q8Student = 1  => student
"""
students_RF - respondents from Russia which are students 
stud_RF_percent - percentage of respondents which are students from Russia
"""
students_RF = (numeric_file.loc[(numeric_file['CountryNumeric2'] == 138) &
                                (numeric_file['q8Student'] == 1)])['q8Student'].value_counts().loc[1].astype(int)
stud_RF_percent = format_float_num(percentage_of(students_RF, respondents_RF))

"""
.sum()
Return the sum of the values for the requested axis

respondents_roles - total number of roles 
web_dev_roles - number of web developers 
data_science_roles - number of data science developers 
mobile_dev_roles - number of mobile developers 
web_dev_percent - web developer's percentage of the total number of all respondents 
data_science_dev - data science developer's percentage of the total number of all respondents 
mobile_dev_percent - mobile developer's percentage of the total number of all respondents 
"""
respondents_roles = numeric_file['q9CurrentRole'].value_counts().sum()
web_dev_roles = numeric_file['q9CurrentRole'].value_counts().loc['1'].astype(int)
data_science_roles = numeric_file['q9CurrentRole'].value_counts().loc['6'].astype(int)
mobile_dev_roles = numeric_file['q9CurrentRole'].value_counts().loc['7'].astype(int)
web_dev_percent = format_float_num(percentage_of(web_dev_roles, respondents_roles))
data_science_dev = format_float_num(percentage_of(data_science_roles, respondents_roles))
mobile_dev_percent = format_float_num(percentage_of(mobile_dev_roles, respondents_roles))

"""
.isin(values)
Return boolean DataFrame showing whether each element in the DataFrame is contained in values.

true_answers_RF - number of respondents from Russia who answered all questions correctly 
answer_true_percent - percentage of respondents from Russia who answered all questions
correctly of the total number of Russian respondents  
"""
true_answers_RF = values_file.loc[values_file['CountryNumeric2'] == 'Russian Federation']\
    .index.isin(code_file.index).sum()
answer_true_percent = format_float_num(percentage_of(true_answers_RF, respondents_RF))


"""
draw_charts()
Use Plotly Python graphing library to make interactive pie charts
Visit tutorial: https://plot.ly/python/pie-charts/
"""


def draw_charts():
    offline.plot({
        'data': [{'labels': ['Web-разработка', 'Data Science', 'Мобильная разработка', 'Другое'],
                  "hole": .5,
                  'name':'Чем занимаются опрошенные',
                  'values': [web_dev_percent, data_science_dev, mobile_dev_percent,
                             100 - (web_dev_percent + data_science_dev + mobile_dev_percent)],
                  'type': 'pie',
                  "domain": {"x": [.52, 1],
                             "y": [.51, 1]},
                  "hoverinfo": "label+percent+name"
                  },
                 {
                     'labels': ['Правильно', 'Не правильно'],
                     'values': [answer_true_percent, 100 - answer_true_percent],
                     'type': 'pie',
                     "domain": {"x": [.52, 1],
                                "y": [0, .45]},
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

