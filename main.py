import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
import socket
import pickle

def send_data(input_data,ip):
    s = socket.socket()
    host = ip
    port = 8080
    s.connect((host,port))

    #send
    X = input_data
    data=pickle.dumps(X)
    s.send(data)

    #recv
    received_data = s.recv(519168)
    received_data = pickle.loads(received_data)
    s.close()
    return received_data

def Day(s):
    month_day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, 12):
        month_day_list[i] += month_day_list[i - 1]
    d = s.split('/')
    #print(d)
    dd = int(d[1])
    mm = int(d[0])
    d = dd + month_day_list[mm-1]
    return d

class startpage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text='Please input \nserver ip address'))
        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        self.flu = Button(text = "Flu Suggestion")
        self.flu.bind(on_press=self.flu_suggestion_1)
        self.add_widget(self.flu )

        self.covid = Button(text = "Covid-19 Trend")
        self.covid.bind(on_press=self.covid_suggestion_1)
        self.add_widget(self.covid)

        self.flut = Button(text = "Flu Trend")
        self.flut.bind(on_press=self.flut_suggestion_1)
        self.add_widget(self.flut)

    def flu_suggestion_1(self, instance):
        suggestion_app.screen_manager.current = "F1"
        with open("ip.txt","w") as f:
            f.write(f"{self.ip.text}")

    def covid_suggestion_1(self, instance):
        suggestion_app.screen_manager.current = "C1"
        with open("ip.txt", "w") as f:
            f.write(f"{self.ip.text}")

    def flut_suggestion_1(self, instance):
        suggestion_app.screen_manager.current = "FT1"
        with open("ip.txt", "w") as f:
            f.write(f"{self.ip.text}")


        """
        # a= self.port.text
        a = self.q1.text
        b = self.q2.text
        d = send_data([b])
        # with open("data.txt","w") as f:
        # f.write(f"{a},{b},{c}")
        #info = f"{d}"
        #suggestion_app.info_page.update_info(info)
        suggestion_app.screen_manager.current = "F1"
        """
#Knowledge
class flu1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_1.txt"):
            with open("flu_1.txt","r") as f:
                d = f.read().split(",")
                prev_q1 = d[1]
                prev_q2 = d[2]
        else:
            prev_q1 = ''
            prev_q2 = ''

        #column
        self.add_widget(Label(text='h1n1 Question'))  # widget #1, top left
        self.add_widget(Label(text='Question Description'))  # widget #1, top left
        self.add_widget(Label(text='Answer, please\n'
                                   'input number'))  # widget #1, top left
        #h1n1_concern  0~3
        self.add_widget(Label(text='How about \n'
                                   'your concern\n'
                                   'about the h1n1?'))  # widget #1, top left
        self.add_widget(Label(text='please input a \n'
                                   'number 0-3;\n'
                                   '0 - not concern,\n'
                                   '1 - little concern,\n'
                                   '2 - concern,\n'
                                   '3 - very concern.'))
        self.q1 = TextInput(text=prev_q1,multiline=False)
        self.add_widget(self.q1)

        #h1n1_knowledge 0~2
        self.add_widget(Label(text='How about\n'
                                   'your knowledge\n'
                                   ' about h1n1?'))
        self.add_widget(Label(text='please input a\n'
                                   'number 0-2;\n' 
                                   '0 - Not know \n'
                                   'about h1n1,\n'
                                   '1 - know little\n'
                                   'about h1n1,\n'
                                   '2 - Know a lot\n'
                                   'about h1n1.'))
        self.q2 = TextInput(text=prev_q2,multiline=False)
        self.add_widget(self.q2)

        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_2)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_2(self, instance):
        suggestion_app.screen_manager.current = "F2"
        with open("flu_1.txt","w") as f:
            f.write(f"flu,{self.q1.text},{self.q2.text}")
#Behavior 1
class flu2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_2.txt"):
            with open("flu_2.txt","r") as f:
                d = f.read().split(",")
                prev_q3 = d[0]
                prev_q4 = d[1]
                prev_q5 = d[2]
                prev_q6 = d[3]
        else:
            prev_q3 = ''
            prev_q4 = ''
            prev_q5 = ''
            prev_q6 = ''

        # column
        self.add_widget(Label(text='Behavior Question 1'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please\n'
                                   'input number'))
        # behavioral_antiviral_meds  0~1
        self.add_widget(Label(text='Do you \n'
                                   'believe in \n'
                                   'anti-vaccination?'))
        self.add_widget(Label(text='Please input a\n'
                                   'number 0-1;\n'
                                   '0 - No,\n'
                                   '1 - Yes.\n'))
        self.q3 = TextInput(text=prev_q3,multiline=False)
        self.add_widget(self.q3)

        # behavioral_avoidance 0~2
        self.add_widget(Label(text='Do you avoid\n'
                                   'roaming around\n'
                                   'in public?'))
        self.add_widget(Label(text='Please input a\n'
                                   'number 0-1;\n'
                                   '0 - No,\n'
                                   '1 - Yes.\n'))
        self.q4 = TextInput(text=prev_q4,multiline=False)
        self.add_widget(self.q4)

        # behavioral_face_mask
        self.add_widget(Label(text='Do you wear\n'
                                   'a face mask?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   '0 - No,\n'
                                   '1 - Yes.\n'))
        self.q5 = TextInput(text=prev_q5,multiline=False)
        self.add_widget(self.q5)

        # behavioral_wash_hands
        self.add_widget(Label(text='Do you \n'
                                   'regularly wash \n'
                                   'your hands?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                    '0 - No,\n'
                                    '1 - Yes.\n'))
        self.q6 = TextInput(text=prev_q6,multiline=False)
        self.add_widget(self.q6)

        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_3)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_3(self, instance):
        suggestion_app.screen_manager.current = "F3"
        with open("flu_2.txt","w") as f:
            f.write(f"{self.q3.text},{self.q4.text},{self.q5.text},{self.q6.text}")
#Behavior 2
class flu3(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_3.txt"):
            with open("flu_3.txt", "r") as f:
                d = f.read().split(",")
                prev_q7 = d[0]
                prev_q8 = d[1]
                prev_q9 = d[2]
        else:
            prev_q7 = ''
            prev_q8 = ''
            prev_q9 = ''

        # column
        self.add_widget(Label(text='Behavior Question 2'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please\n'
                                   ' input number'))
        # behavioral_large_gatherings  0~1
        self.add_widget(Label(text='Do you tend\n'
                                   'to be in \n'
                                   'large gatherings?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                    ' 0 - No,\n'
                                    ' 1 - Yes.\n'))
        self.q7 = TextInput(text=prev_q7, multiline=False)
        self.add_widget(self.q7)

        # behavioral_outside_home 0~1
        self.add_widget(Label(text='Do you tend \n'
                                   'to be outdoors \n'
                                   'a lot?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                    ' 0 - No,\n'
                                    ' 1 - Yes.\n'))
        self.q8 = TextInput(text=prev_q8, multiline=False)
        self.add_widget(self.q8)

        # behavioral_touch_face 0-1
        self.add_widget(Label(text='Do you touch \n'
                                   'their faces \n'
                                   'often?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                    ' 0 - No,\n'
                                    ' 1 - Yes.\n'))
        self.q9 = TextInput(text=prev_q9, multiline=False)
        self.add_widget(self.q9)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_4)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_4(self, instance):
        suggestion_app.screen_manager.current = "F4"
        with open("flu_3.txt", "w") as f:
            f.write(f"{self.q7.text},{self.q8.text},{self.q9.text}")
#Doctor
class flu4(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_4.txt"):
            with open("flu_4.txt", "r") as f:
                d = f.read().split(",")
                prev_q10 = d[0]
                prev_q11 = d[1]
                prev_q12 = d[2]
        else:
            prev_q10 = ''
            prev_q11 = ''
            prev_q12 = ''

        # column
        self.add_widget(Label(text='Medical Question '))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please \n'
                                   'input number'))
        # doctor_recc_h1n1  0~1
        self.add_widget(Label(text='Do your doctor \n'
                                   'recommend you take\n'
                                   ' h1n1 flu shot?'))
        self.add_widget(Label(text='Please input\n'
                                   'a number 0-1;\n'
                                   ' 0 - No,\n'
                                   ' 1 - Yes.\n'))
        self.q10 = TextInput(text=prev_q10, multiline=False)
        self.add_widget(self.q10)

        # doctor_recc_seasonal 0~1
        self.add_widget(Label(text='Do your doctor \n'
                                   'recommend you take\n'
                                   'seasonal flu shot?'))
        self.add_widget(Label(text='Please input \n'
                                   'a number 0-1;\n'
                                   ' 0 - No,\n'
                                   ' 1 - Yes.\n'))
        self.q11 = TextInput(text=prev_q11, multiline=False)
        self.add_widget(self.q11)

        # chronic_med_condition 0-1
        self.add_widget(Label(text='Are you i \n'
                                   'chronic medical \n'
                                   'condition?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   ' 0 - No,\n'
                                   ' 1 - Yes.\n'))
        self.q12 = TextInput(text=prev_q12, multiline=False)
        self.add_widget(self.q12)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_5)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_5(self, instance):
        suggestion_app.screen_manager.current = "F5"
        with open("flu_4.txt", "w") as f:
            f.write(f"{self.q10.text},{self.q11.text},{self.q12.text}")
#Personal Infomation #1
class flu5(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_5.txt"):
            with open("flu_5.txt", "r") as f:
                d = f.read().split(",")
                prev_q13 = d[0]
                prev_q14 = d[1]
                prev_q15 = d[2]
        else:
            prev_q13 = ''
            prev_q14 = ''
            prev_q15 = ''

        # column
        self.add_widget(Label(text='Other Question 1 '))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please\n'
                                   ' input number'))
        # child_under_6_months  0~1
        self.add_widget(Label(text='Do your have \n'
                                   'children under \n'
                                   '6 month?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   ' 0 - No,\n'
                                   ' 1 - Yes.\n'))
        self.q13 = TextInput(text=prev_q13, multiline=False)
        self.add_widget(self.q13)

        # health_worker 0~1
        self.add_widget(Label(text='Are you a\n'
                                   'health worker?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   ' 0 - No,\n'
                                   ' 1 - Yes.\n'))
        self.q14 = TextInput(text=prev_q14, multiline=False)
        self.add_widget(self.q14)

        # health_insurance 0-1
        self.add_widget(Label(text='Do you have\n'
                                   'health insurance?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   ' 0 - No,\n'
                                   ' 1 - Yes.\n'))
        self.q15 = TextInput(text=prev_q15, multiline=False)
        self.add_widget(self.q15)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_6)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_6(self, instance):
        suggestion_app.screen_manager.current = "F6"
        with open("flu_5.txt", "w") as f:
            f.write(f"{self.q13.text},{self.q14.text},{self.q15.text}")
#h1n1 idea
class flu6(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_6.txt"):
            with open("flu_6.txt", "r") as f:
                d = f.read().split(",")
                prev_q16 = d[0]
                prev_q17 = d[1]
                prev_q18 = d[2]
        else:
            prev_q16 = ''
            prev_q17 = ''
            prev_q18 = ''

        # column
        self.add_widget(Label(text='h1n1 Question'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please\n'
                                   'input number'))
        # opinion_h1n1_vacc_effective  1~5
        self.add_widget(Label(text='Do you agree\n'
                                   ' h1n1 vaccine \n'
                                   'is effective?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 1-5;\n'
                                   ' 1 - Not Agree,\n'
                                   ' 5 - Agree.\n'))
        self.q16 = TextInput(text=prev_q16, multiline=False)
        self.add_widget(self.q16)

        # opinion_h1n1_risk 1~5
        self.add_widget(Label(text='Do you agree \n'
                                   'h1n1 is a risk?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 1-5;\n'
                                   ' 1 - Not Agree,\n'
                                   ' 5 - Agree.\n'))
        self.q17 = TextInput(text=prev_q17, multiline=False)
        self.add_widget(self.q17)

        # opinion_h1n1_sick_from_vacc 1-5
        self.add_widget(Label(text='Do you agree \n'
                                   'h1n1 vaccine \n'
                                   'will make you \n'
                                   'sick?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 1-5;\n'
                                   ' 1 - Not Agree,\n'
                                   ' 5 - Agree.\n'))
        self.q18 = TextInput(text=prev_q18, multiline=False)
        self.add_widget(self.q18)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_7)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_7(self, instance):
        suggestion_app.screen_manager.current = "F7"
        with open("flu_6.txt", "w") as f:
            f.write(f"{self.q16.text},{self.q17.text},{self.q18.text}")
#seasonal idea
class flu7(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_7.txt"):
            with open("flu_7.txt", "r") as f:
                d = f.read().split(",")
                prev_q19 = d[0]
                prev_q20 = d[1]
                prev_q21 = d[2]
        else:
            prev_q19 = ''
            prev_q20 = ''
            prev_q21 = ''

        # column
        self.add_widget(Label(text='Seasonal flu Question'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please \n'
                                   'input number'))
        # opinion_seas_vacc_effective  1~5
        self.add_widget(Label(text='Do you agree \n'
                                   'seasonal flu \n'
                                   'vaccine \n'
                                   'is effective?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 1-5;\n'
                                   ' 1 - Not Agree,\n'
                                   ' 5 - Agree.'))
        self.q19 = TextInput(text=prev_q19, multiline=False)
        self.add_widget(self.q19)

        # opinion_h1n1_risk 1~5
        self.add_widget(Label(text='Do you agree \n'
                                   'seasonal flu \n'
                                   'is a risk?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 1-5;\n'
                                   ' 1 - Not Agree,\n'
                                   ' 5 - Agree.'))
        self.q20 = TextInput(text=prev_q20, multiline=False)
        self.add_widget(self.q20)

        # opinion_h1n1_sick_from_vacc 1-5
        self.add_widget(Label(text='Do you agree \n'
                                   'seasonal flu \n'
                                   'vaccine will \n'
                                   'make you sick?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 1-5;\n'
                                   ' 1 - Not Agree,\n'
                                   ' 5 - Agree.'))
        self.q21 = TextInput(text=prev_q21, multiline=False)
        self.add_widget(self.q21)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_8)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_8(self, instance):
        suggestion_app.screen_manager.current = "F8"
        with open("flu_7.txt", "w") as f:
            f.write(f"{self.q19.text},{self.q20.text},{self.q21.text}")
#Other Question 1
class flu8(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_8.txt"):
            with open("flu_8.txt", "r") as f:
                d = f.read().split(",")
                prev_q22 = d[0]
                prev_q23 = d[1]
        else:
            prev_q22 = ''
            prev_q23 = ''

        # column
        self.add_widget(Label(text='Other Question 1'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please \n'
                                   'input number'))

        # age_group
        self.add_widget(Label(text='Please input \n'
                                   'your age group'))
        self.add_widget(Label(text='Please input \n'
                                   'a number 0-4;\n'
                                   '0 - 18 ~ 34 Years,\n'
                                   '1 - 35 ~ 44 Years,\n'
                                   '2 - 45 ~ 54 Years,\n'
                                   '3 - 55 ~ 64 Years,\n'
                                   '4 - 65+ Years.'))
        self.q22 = TextInput(text=prev_q22, multiline=False)
        self.add_widget(self.q22)

        self.add_widget(Label(text='Please input your \n'
                                   'education experience?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-3;\n'
                                   ' 0 - < 12 Years,\n'
                                   ' 1 - 12 Years,\n'
                                   ' 2 - Some College,\n'
                                   ' 3 - College Graduate.'))
        self.q23 = TextInput(text=prev_q23, multiline=False)
        self.add_widget(self.q23)


        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_9)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_9(self, instance):
        suggestion_app.screen_manager.current = "F9"
        with open("flu_8.txt", "w") as f:
            f.write(f"{self.q22.text},{self.q23.text}")
#Other Question 2
class flu9(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_9.txt"):
            with open("flu_9.txt", "r") as f:
                d = f.read().split(",")
                prev_q24 = d[0]
                prev_q25 = d[1]
                prev_q26 = d[2]
        else:
            prev_q24 = ''
            prev_q25 = ''
            prev_q26 = ''

        # column
        self.add_widget(Label(text='Other Question 2'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please \n'
                                   'input number'))
        # race
        self.add_widget(Label(text='Please input \n'
                                   'your race'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-3;\n'
                                   ' 0 - Black,\n'
                                   ' 1 - Hispanic,\n'
                                   ' 2 - White,\n'
                                   ' 3 - Other or Multiple.'))
        self.q24 = TextInput(text=prev_q24, multiline=False)
        self.add_widget(self.q24)

        #sex
        self.add_widget(Label(text='Please input your sex'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   ' 0 - Female,\n'
                                   ' 1 - Male.'))
        self.q25 = TextInput(text=prev_q25, multiline=False)
        self.add_widget(self.q25)

        #income_poverty
        self.add_widget(Label(text='Please input your income'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-2;\n'
                                   ' 0 - >$75000,\n'
                                   ' 1 - <$75000, \n'
                                   ' above Poverty,\n'
                                   ' 2 - Below Poverty.'))
        self.q26 = TextInput(text=prev_q26, multiline=False)
        self.add_widget(self.q26)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_10)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_10(self, instance):
        suggestion_app.screen_manager.current = "F10"
        with open("flu_9.txt", "w") as f:
            f.write(f"{self.q24.text},{self.q25.text},{self.q26.text}")
#Other Question 3
class flu10(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_10.txt"):
            with open("flu_10.txt", "r") as f:
                d = f.read().split(",")
                prev_q27 = d[0]
                prev_q28 = d[1]
                prev_q29 = d[2]
        else:
            prev_q27 = ''
            prev_q28 = ''
            prev_q29 = ''


        # column
        self.add_widget(Label(text='Other Question 3'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please\n'
                                   'input number'))

        # marital_status
        self.add_widget(Label(text='Do you have \n'
                                   'married?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   ' 0 - Married,\n'
                                   ' 1 - Not Married.'))
        self.q27 = TextInput(text=prev_q27, multiline=False)
        self.add_widget(self.q27)

        # rent_or_own
        self.add_widget(Label(text='Is your house \n'
                                   'rent or own?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number 0-1;\n'
                                   ' 0 - Own,\n'
                                   ' 1 - Rent.'))
        self.q28 = TextInput(text=prev_q28, multiline=False)
        self.add_widget(self.q28)

        # employment_status
        self.add_widget(Label(text='How about your \n'
                                   'employment status?'))
        self.add_widget(Label(text='Please input a\n'
                                   ' number 0-2;\n'
                                   ' 0 - Employed,\n'
                                   ' 1 - Not in Labor Force,\n'
                                   ' 2 - Unemployed.'))
        self.q29 = TextInput(text=prev_q29, multiline=False)
        self.add_widget(self.q29)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_11)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_11(self, instance):
        suggestion_app.screen_manager.current = "F11"
        with open("flu_10.txt", "w") as f:
            f.write(f"{self.q27.text},{self.q28.text},{self.q29.text}")
#Other Question 4
class flu11(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_9.txt"):
            with open("flu_9.txt", "r") as f:
                d = f.read().split(",")
                prev_q30 = d[0]
                prev_q31 = d[1]
                prev_q32 = d[2]
        else:

            prev_q30 = ''
            prev_q31 = ''
            prev_q32 = ''

        # column
        self.add_widget(Label(text='Other Question 4'))
        self.add_widget(Label(text='Question Description'))
        self.add_widget(Label(text='Answer, please\n'
                                   ' input number'))


        #census_msa
        self.add_widget(Label(text='Do you live \n'
                                   'in Metropolitan\n'
                                   ' Statistical Area?'))
        self.add_widget(Label(text='Please input a\n'
                                   ' number 0-2;\n'
                                   ' 0 - MSA, Not \n'
                                   'Principle  City,\n'
                                   ' 1 - MSA, \n'
                                   'Principle City,\n'
                                   ' 2 - Non-MSA.'))
        self.q30 = TextInput(text=prev_q30, multiline=False)
        self.add_widget(self.q30)

        #household_adults
        self.add_widget(Label(text='How many adults \n'
                                   'in your household?'))
        self.add_widget(Label(text='Please input a\n'
                                   ' number;'))
        self.q31 = TextInput(text=prev_q31, multiline=False)
        self.add_widget(self.q31)
        #household_children
        self.add_widget(Label(text='How many children \n'
                                   'in your household?'))
        self.add_widget(Label(text='Please input a \n'
                                   'number;'))
        self.q32 = TextInput(text=prev_q32, multiline=False)
        self.add_widget(self.q32)

        # Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_s)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_s(self, instance):

        with open("flu_11.txt", "w") as f:
            f.write(f"{self.q30.text},{self.q31.text},{self.q32.text}")

        with open("ip.txt", "r") as f:
            ip = f.read().split(",")
            ip = ip[0]


        with open("flu_1.txt", "r") as f:
            d1 = f.read().split(",")
        with open("flu_2.txt", "r") as f:
            d2 = f.read().split(",")
        with open("flu_3.txt", "r") as f:
            d3 = f.read().split(",")
        with open("flu_4.txt", "r") as f:
            d4 = f.read().split(",")
        with open("flu_5.txt", "r") as f:
            d5 = f.read().split(",")
        with open("flu_6.txt", "r") as f:
            d6 = f.read().split(",")
        with open("flu_7.txt", "r") as f:
            d7 = f.read().split(",")
        with open("flu_8.txt", "r") as f:
            d8 = f.read().split(",")
        with open("flu_9.txt", "r") as f:
            d9 = f.read().split(",")
        with open("flu_10.txt", "r") as f:
            d10 = f.read().split(",")
        with open("flu_11.txt", "r") as f:
            d11 = f.read().split(",")
        data = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11

        recv_suggestion = send_data(data,ip)
        info = f"{recv_suggestion}"
        suggestion_app.fs.update_info(info)
        suggestion_app.screen_manager.current = "FS"
#Flu Suggestion
class flus(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign = "center", valign = "middle", font_size = 20)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)
#Covid_Q1
class covid1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("covid_1.txt"):
            with open("covid_1.txt","r") as f:
                d = f.read().split(",")
                prev_q1 = d[1]
                prev_q2 = d[2]
        else:
            prev_q1 = ''
            prev_q2 = ''

        #column
        self.add_widget(Label(text='Covid Question 1'))  # widget #1, top left
        self.add_widget(Label(text='Question Description'))  # widget #1, top left
        self.add_widget(Label(text='Answer,\n'
                                   'please input\n'
                                   'As Description'))  # widget #1, top left
        #yesterday_new_case
        self.add_widget(Label(text='How many new cases in\n'
                                   'your county yesterday?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'))
        self.q1 = TextInput(text=prev_q1,multiline=False)
        self.add_widget(self.q1)

        #first_case_time
        self.add_widget(Label(text='When did your county\n '
                                   'find first case?'))
        self.add_widget(Label(text='please input date\n' 
                                   'mm/dd:\n'))
        self.q2 = TextInput(text=prev_q2,multiline=False)
        self.add_widget(self.q2)

        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.covid_suggestion_2)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def covid_suggestion_2(self, instance):
        suggestion_app.screen_manager.current = "C2"
        with open("covid_1.txt","w") as f:
            f.write(f"covid,{self.q1.text},{self.q2.text}")
#Covid_Q2
class covid2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("covid_2.txt"):
            with open("covid_2.txt","r") as f:
                d = f.read().split(",")
                prev_q3 = d[0]
                prev_q4 = d[1]
                prev_q5 = d[2]
        else:
            prev_q3 = ''
            prev_q4 = ''
            prev_q5 = ''

        #column
        self.add_widget(Label(text='Covid Question 2'))  # widget #1, top left
        self.add_widget(Label(text='Question Description'))  # widget #1, top left
        self.add_widget(Label(text='Answer, please\n'
                                   'input as\n'
                                   'Description'))  # widget #1, top left
        #date
        self.add_widget(Label(text='What is the\n'
                                   'date today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'mm/dd\n'))
        self.q3 = TextInput(text=prev_q3,multiline=False)
        self.add_widget(self.q3)

        #case
        self.add_widget(Label(text='How many cases in\n '
                                   'your county today'))
        self.add_widget(Label(text='please input\n' 
                                   'a number\n'))
        self.q4 = TextInput(text=prev_q4,multiline=False)
        self.add_widget(self.q4)

        #population
        self.add_widget(Label(text='How many population\n '
                                   'in your county'))
        self.add_widget(Label(text='please input\n' 
                                   'a number\n'))
        self.q5 = TextInput(text=prev_q5,multiline=False)
        self.add_widget(self.q5)

        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.covid_suggestion_3)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def covid_suggestion_3(self, instance):
        suggestion_app.screen_manager.current = "C3"
        with open("covid_2.txt","w") as f:
            f.write(f"{self.q3.text},{self.q4.text},{self.q5.text}")
#Local Policy 1
class covid3(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("covid_3.txt"):
            with open("covid_3.txt","r") as f:
                d = f.read().split(",")
                prev_q6 = d[0]
                prev_q7 = d[1]
                prev_q8 = d[2]
        else:
            prev_q6 = ''
            prev_q7 = ''
            prev_q8 = ''

        #column
        self.add_widget(Label(text='Covid Question 3'))  # widget #1, top left
        self.add_widget(Label(text='Question Description'))  # widget #1, top left
        self.add_widget(Label(text='Answer, please\n'
                                   'input as\n'
                                   'Description'))  # widget #1, top left
        #stay_at_home
        self.add_widget(Label(text='Ask to stay at\n'
                                   'home today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q6 = TextInput(text=prev_q6,multiline=False)
        self.add_widget(self.q6)

        self.add_widget(Label(text='limit you gather\n'
                                   '>50 today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q7 = TextInput(text=prev_q7,multiline=False)
        self.add_widget(self.q7)

        self.add_widget(Label(text='limit you gather\n'
                                   '>500 today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q8 = TextInput(text=prev_q8,multiline=False)
        self.add_widget(self.q8)


        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.covid_suggestion_4)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def covid_suggestion_4(self, instance):
        suggestion_app.screen_manager.current = "C4"
        with open("covid_3.txt","w") as f:
            f.write(f"{self.q6.text},{self.q7.text},{self.q8.text}")
#Local Policy 2
class covid4(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("covid_4.txt"):
            with open("covid_4.txt","r") as f:
                d = f.read().split(",")
                prev_q9 = d[0]
                prev_q10 = d[1]
                prev_q11 = d[2]
        else:
            prev_q9 = ''
            prev_q10 = ''
            prev_q11 = ''

        #column
        self.add_widget(Label(text='Covid Question 4'))  # widget #1, top left
        self.add_widget(Label(text='Question Description'))  # widget #1, top left
        self.add_widget(Label(text='Answer, please\n'
                                   'input as\n'
                                   'Description'))  # widget #1, top left
        #stay_at_home
        self.add_widget(Label(text='Is public school\n'
                                   'close today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q9 = TextInput(text=prev_q9,multiline=False)
        self.add_widget(self.q9)

        self.add_widget(Label(text='Is restaurant\n'
                                   'close today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q10 = TextInput(text=prev_q10,multiline=False)
        self.add_widget(self.q10)

        self.add_widget(Label(text='Is entertainment\n'
                                   '&gem close today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q11 = TextInput(text=prev_q11,multiline=False)
        self.add_widget(self.q11)


        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.covid_suggestion_4)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def covid_suggestion_4(self, instance):
        suggestion_app.screen_manager.current = "C5"
        with open("covid_4.txt","w") as f:
            f.write(f"{self.q9.text},{self.q10.text},{self.q11.text}")
#Local Policy 3
class covid5(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("covid_5.txt"):
            with open("covid_5.txt","r") as f:
                d = f.read().split(",")
                prev_q12 = d[0]
                prev_q13 = d[1]
        else:
            prev_q12 = ''
            prev_q13 = ''

        #column
        self.add_widget(Label(text='Covid Question 4'))  # widget #1, top left
        self.add_widget(Label(text='Question Description'))  # widget #1, top left
        self.add_widget(Label(text='Answer, please\n'
                                   'input as\n'
                                   'Description'))  # widget #1, top left
        #stay_at_home
        self.add_widget(Label(text='Is there federal\n'
                                   'guideline today?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q12 = TextInput(text=prev_q12,multiline=False)
        self.add_widget(self.q12)

        self.add_widget(Label(text='Is foreign\n'
                                   'travel ban?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '0 - No\n'
                                   '1 - Yes\n'))
        self.q13 = TextInput(text=prev_q13,multiline=False)
        self.add_widget(self.q13)


        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.covid_suggestion_s)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def covid_suggestion_s(self, instance):
        with open("covid_5.txt", "w") as f:
            f.write(f"{self.q12.text},{self.q13.text}")

        with open("ip.txt", "r") as f:
            ip = f.read().split(",")
            ip = ip[0]

        with open("covid_1.txt", "r") as f:
            d1 = f.read().split(",")
        d1[2] = Day(d1[2])
        with open("covid_2.txt", "r") as f:
            d2 = f.read().split(",")
        d2[0] = Day(d2[0])
        with open("covid_3.txt", "r") as f:
            d3 = f.read().split(",")
        with open("covid_4.txt", "r") as f:
            d4 = f.read().split(",")
        with open("covid_5.txt", "r") as f:
            d5 = f.read().split(",")
        data = d1+d2+d3+d4+d5
        recv_suggestion = send_data(data,ip)
        info = f"{recv_suggestion}"
        suggestion_app.cf.update_info(info)
        suggestion_app.screen_manager.current = "CF"
#Covid Forecast
class covidf(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign = "center", valign = "middle", font_size = 20)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)
#flu data collect
class flut1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("flu_trend.txt"):
            with open("flu_trend.txt","r") as f:
                d = f.read().split(",")
                prev_q1 = d[1]
                prev_q2 = d[2]
                prev_q3 = d[3]
        else:
            prev_q1 = ''
            prev_q2 = ''
            prev_q3 = ''

        #column
        self.add_widget(Label(text='Flu Trend Question'))  # widget #1, top left
        self.add_widget(Label(text='Question Description'))  # widget #1, top left
        self.add_widget(Label(text='Answer, please\n'
                                   'input as\n'
                                   'Description'))  # widget #1, top left
        #Date
        self.add_widget(Label(text='What is the date \n'
                                   'of this Friday?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'mm/dd\n'))
        self.q1 = TextInput(text=prev_q1,multiline=False)
        self.add_widget(self.q1)
        #Local population
        self.add_widget(Label(text='How much people\n'
                                   'live here?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'))
        self.q2 = TextInput(text=prev_q2,multiline=False)
        self.add_widget(self.q2)
        #Age Group
        self.add_widget(Label(text='What is your\n'
                                   'age group?'))  # widget #1, top left
        self.add_widget(Label(text='Please input\n'
                                   'a number\n'
                                   '1 - 0~9 yrs\n'
                                   '2 - 10~19 yrs\n'
                                   '3 - 20~39 yrs\n'
                                   '4 - 40~54 yrs\n'
                                   '5 - 55+ yrs\n'))
        self.q3 = TextInput(text=prev_q3,multiline=False)
        self.add_widget(self.q3)


        #Next Button
        self.next_p = Button(text="Next")
        self.next_p.bind(on_press=self.flu_suggestion_f)
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(self.next_p)

    def flu_suggestion_f(self, instance):
        with open("flu_trend.txt", "w") as f:
            f.write(f"fluf,{self.q1.text},{self.q2.text},{self.q3.text}")

        with open("ip.txt", "r") as f:
            ip = f.read().split(",")
            ip = ip[0]

        with open("flu_trend.txt", "r") as f:
            d1 = f.read().split(",")
        d1[1] = Day(d1[1])
        data = d1
        recv_suggestion = send_data(data,ip)
        info = f"{recv_suggestion}"
        suggestion_app.ff.update_info(info)
        suggestion_app.screen_manager.current = "FF"

#Flu Forecast
class fluf(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign = "center", valign = "middle", font_size = 20)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)
"""
class
    
        #connection button
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.next = Button(text = "Next")
        self.next.bind(on_press=self.join_button)
        self.add_widget(self.next )

    def join_button(self, instance):
        #a= self.port.text
        a = self.q1.text
        b = self.q2.text
        d = send_data([b])
        #with open("data.txt","w") as f:
            #f.write(f"{a},{b},{c}")
        info = f"{d}"
        suggestion_app.info_page.update_info(info)
        suggestion_app.screen_manager.current = "Info"
"""
"""
class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign = "center", valign = "middle", font_size = 30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)
"""

class suggestionapp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.start_page = startpage()
        screen = Screen(name="start")
        screen.add_widget(self.start_page)
        self.screen_manager.add_widget(screen)

        self.f1 = flu1()
        screen = Screen(name="F1")
        screen.add_widget(self.f1)
        self.screen_manager.add_widget(screen)

        self.f2 = flu2()
        screen = Screen(name="F2")
        screen.add_widget(self.f2)
        self.screen_manager.add_widget(screen)

        self.f3 = flu3()
        screen = Screen(name="F3")
        screen.add_widget(self.f3)
        self.screen_manager.add_widget(screen)

        self.f4 = flu4()
        screen = Screen(name="F4")
        screen.add_widget(self.f4)
        self.screen_manager.add_widget(screen)

        self.f5 = flu5()
        screen = Screen(name="F5")
        screen.add_widget(self.f5)
        self.screen_manager.add_widget(screen)

        self.f6 = flu6()
        screen = Screen(name="F6")
        screen.add_widget(self.f6)
        self.screen_manager.add_widget(screen)

        self.f7 = flu7()
        screen = Screen(name="F7")
        screen.add_widget(self.f7)
        self.screen_manager.add_widget(screen)

        self.f8 = flu8()
        screen = Screen(name="F8")
        screen.add_widget(self.f8)
        self.screen_manager.add_widget(screen)

        self.f9 = flu9()
        screen = Screen(name="F9")
        screen.add_widget(self.f9)
        self.screen_manager.add_widget(screen)

        self.f10 = flu10()
        screen = Screen(name="F10")
        screen.add_widget(self.f10)
        self.screen_manager.add_widget(screen)

        self.f11 = flu11()
        screen = Screen(name="F11")
        screen.add_widget(self.f11)
        self.screen_manager.add_widget(screen)

        self.fs = flus()
        screen = Screen(name="FS")
        screen.add_widget(self.fs)
        self.screen_manager.add_widget(screen)

        self.c1 = covid1()
        screen = Screen(name="C1")
        screen.add_widget(self.c1)
        self.screen_manager.add_widget(screen)

        self.c2 = covid2()
        screen = Screen(name="C2")
        screen.add_widget(self.c2)
        self.screen_manager.add_widget(screen)

        self.c3 = covid3()
        screen = Screen(name="C3")
        screen.add_widget(self.c3)
        self.screen_manager.add_widget(screen)

        self.c4 = covid4()
        screen = Screen(name="C4")
        screen.add_widget(self.c4)
        self.screen_manager.add_widget(screen)

        self.c5 = covid5()
        screen = Screen(name="C5")
        screen.add_widget(self.c5)
        self.screen_manager.add_widget(screen)

        self.cf = covidf()
        screen = Screen(name="CF")
        screen.add_widget(self.cf)
        self.screen_manager.add_widget(screen)

        self.ft1 = flut1()
        screen = Screen(name="FT1")
        screen.add_widget(self.ft1)
        self.screen_manager.add_widget(screen)

        self.ff = fluf()
        screen = Screen(name="FF")
        screen.add_widget(self.ff)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    suggestion_app = suggestionapp()
    suggestion_app.run()