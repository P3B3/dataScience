<h1>Install this:</h1>
<h3>Python 3.6.x</h3>
<h3>Pandas 0.22.x</h3>
<h3>matplotlib 2.2.x</h3>

"""
def draw_percent_of_roles():
    # create data
    names = 'Web', 'Data Science', 'Mobile', 'Другое',
    size = [webPercent, dataPercent, mobPercent, 100 - (webPercent + dataPercent + mobPercent)]
    plt.title('Чем занимаются опрошенные:')
    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.pie(size, labels=names, wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
    fig = plt.gcf()
    fig.gca().add_artist(my_circle)
    plt.show()


def draw_RF_stud():
    # create data
    names = 'Студенты', 'Другое',
    size = [studPercent, 100 - studPercent]

    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.title('Число опрошенных программистов из России: ' + str(respondentsRF))
    plt.pie(size, labels=names, wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, autopct='%1.1f%%', startangle=90)
    fig = plt.gcf()
    fig.gca().add_artist(my_circle)
    plt.show()


def draw_true_answer():
    # create data
    names = 'Правильно', 'Не правильно'
    size = [answerTruePercent, 100 - answerTruePercent]

    # Create a circle for the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='white')

    plt.title('Ответили: ')
    plt.pie(size, labels=names, wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, autopct='%1.1f%%', startangle=90)
    fig = plt.gcf()
    fig.gca().add_artist(my_circle)
    plt.show()


draw_percent_of_roles()
draw_RF_stud()
draw_true_answer()

""""