from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QGroupBox, QHBoxLayout, QButtonGroup


from random import shuffle


app = QApplication([])
main_win = QWidget()
text = QLabel('Какой национальности не существует?')
main_win.move(900, 70)
main_win.resize(600, 400)
main_win.setWindowTitle('Memory Card')
RadioGroupBox = QGroupBox('Варианты ответов')
line = QVBoxLayout()
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
itog = QLabel('Тут будет верный ответ')
layout_ans3 = QVBoxLayout()



layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



def show_result():
    RadioGroupBox.hide() #временное скрытие окна
    
    button.setText('Следующий вопрос')
    AnsGroupBox.show()
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide() #временное скрытие окна
    button.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

    


def show_correct(res):
    result.setText(res)
    show_result()

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask (q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1) 
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    itog.setText(q.right_answer)
    show_question()

def check_answer(): #проверка ответа
    if answer[0].isChecked():
        show_correct('Правильно')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked:
            show_correct('Неверно')



# RadioGroupBox.hide() временное скрытие окна 


layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog, Qt.AlignCenter | Qt.AlignVCenter)
AnsGroupBox.setLayout(layout_res)

line1 = QHBoxLayout()
line1.addWidget(text, alignment =(Qt.AlignCenter | Qt.AlignVCenter))
line2 = QHBoxLayout()
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3 = QHBoxLayout()
button = QPushButton('Ответить')
line3.addWidget(button, alignment =(Qt.AlignCenter | Qt.AlignVCenter))




glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)

main_win.setLayout(glav)



questions_list = []
questions_list.append(Question('Какое животное из перечисленных состоит в красной книге?', 'амурский тигр', 'кролик', 'ястреб', 'корова'))
questions_list.append(Question('Какого знака зодиака не существует?', 'змееносец', 'рак', 'водолей', 'близнецы'))
questions_list.append(Question('Какая страна в Европе не была тронута третьим рейхом во время Второй Мировой Войны?', 'Швейцария', 'Франция', 'Польша', 'Люксембург'))
questions_list.append(Question('У кого из актёров голливуда наибольшее количество номинаций на Оскар?', 'Мерил Стрип', 'Лоуренс Оливье', 'Пол Ньюман', 'Аль Пачино'))
questions_list.append(Question('Что связывает многих известных русских писателей из 16-20 веков?', 'смерть родителей', 'талант', 'малый рост', 'день рождения весной'))
questions_list.append(Question('Что убило динозавров?', 'метеорит', 'рождение человека', 'солнце', 'холод'))
questions_list.append(Question('Из скольки % воды состоит наша планета?', '71%', '50%', '32%', '99%'))
questions_list.append(Question('Как зовут актёра игравшего человека паука в самом первом фильме?', 'Тоби Магуйар', 'Том Холланд', 'Эндрю Гарфилд', 'Уиллем Дефо'))
questions_list.append(Question('В каком году произошёл распад СССР?', '1991', '2000', '1954', '1968'))
questions_list.append(Question('От чего Умер Напалеон Бонапарт?', 'отрава', 'старость', 'утонул', 'убили'))

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)


def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


main_win.cur_question = -1
next_question()

button.clicked.connect(click_ok)
main_win.show()
app.exec_()