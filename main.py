import pandas as pd
import matplotlib.pyplot as plt
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


def draw_percent_of_roles():
    # create data
    names = 'web', 'data', 'mob', 'other',
    size = [webPercent, dataPercent, mobPercent, 100 - (webPercent + dataPercent + mobPercent)]

    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.pie(size, labels=names, wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
    fig = plt.gcf()
    fig.gca().add_artist(my_circle)
    plt.show()


def draw_RF_stud():
    # create data
    names = 'students', 'other',
    size = [studPercent, 100 - studPercent]

    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.title('Всего из РФ: ')
    plt.title(respondentsRF)
    plt.pie(size, labels=names, wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, autopct='%1.1f%%', startangle=90)
    fig = plt.gcf()
    fig.gca().add_artist(my_circle)
    plt.show()


def draw_true_answer():
    # create data
    names = 'Answ true', 'other',
    size = [answerTruePercent, 100 - answerTruePercent]

    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.title('Ответили правильно: ')
    plt.pie(size, labels=names, wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, autopct='%1.1f%%', startangle=90)
    fig = plt.gcf()
    fig.gca().add_artist(my_circle)
    plt.show()


draw_percent_of_roles()
draw_RF_stud()
draw_true_answer()
