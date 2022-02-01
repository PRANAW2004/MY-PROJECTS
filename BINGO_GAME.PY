from tkinter import *
import tkinter.messagebox
import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

root = Tk()
root.geometry("1350x1350+0+0")
root.title("BINGO")
root.configure(background = 'DARK BLUE')

#=======================================================================================================================
def StartGame():
    button1['command'] = ScoreKeeper1
    button2['command'] = ScoreKeeper6
    button3['command'] = ScoreKeeper11
    button4['command'] = ScoreKeeper16
    button5['command'] = ScoreKeeper21
    button6['command'] = ScoreKeeper2
    button7['command'] = ScoreKeeper7
    button8['command'] = ScoreKeeper12
    button9['command'] = ScoreKeeper17
    button10['command'] = ScoreKeeper22
    button11['command'] = ScoreKeeper3
    button12['command'] = ScoreKeeper8
    button13['command'] = ScoreKeeper13
    button14['command'] = ScoreKeeper18
    button15['command'] = ScoreKeeper23
    button16['command'] = ScoreKeeper4
    button17['command'] = ScoreKeeper9
    button18['command'] = ScoreKeeper14
    button19['command'] = ScoreKeeper19
    button20['command'] = ScoreKeeper24
    button21['command'] = ScoreKeeper5
    button22['command'] = ScoreKeeper10
    button23['command'] = ScoreKeeper15
    button24['command'] = ScoreKeeper20
    button25['command'] = ScoreKeeper25
    button26['command'] = ScoreKeeper26
    button27['command'] = ScoreKeeper27
    button28['command'] = ScoreKeeper28
    button29['command'] = ScoreKeeper29
    button30['command'] = ScoreKeeper30
    speak("Game Started")

#=======================================================================================================================
def iExit():
    iExit = tkinter.messagebox.askyesno("BINGO", "confirn you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Speak():
    speak("BINGO STOP")

def NewGame():
    button1['command'] = " "
    button2['command'] = " "
    button3['command'] = " "
    button4['command'] = " "
    button5['command'] = " "
    button6['command'] = " "
    button7['command'] = " "
    button8['command'] = " "
    button9['command'] = " "
    button10['command'] = " "
    button11['command'] = " "
    button12['command'] = " "
    button13['command'] = " "
    button14['command'] = " "
    button15['command'] = " "
    button16['command'] = " "
    button17['command'] = " "
    button18['command'] = " "
    button19['command'] = " "
    button20['command'] = " "
    button21['command'] = " "
    button22['command'] = " "
    button23['command'] = " "
    button24['command'] = " "
    button25['command'] = " "
    button26['command'] = " "
    button27['command'] = " "
    button28['command'] = " "
    button29['command'] = " "
    button30['command'] = " "

    button1.configure(background="white")
    button2.configure(background="white")
    button3.configure(background="white")
    button4.configure(background="white")
    button5.configure(background="white")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")
    button10.configure(background="gainsboro")
    button11.configure(background="gainsboro")
    button12.configure(background="gainsboro")
    button13.configure(background="gainsboro")
    button14.configure(background="gainsboro")
    button15.configure(background="gainsboro")
    button16.configure(background="gainsboro")
    button17.configure(background="gainsboro")
    button18.configure(background="gainsboro")
    button19.configure(background="gainsboro")
    button20.configure(background="gainsboro")
    button21.configure(background="gainsboro")
    button22.configure(background="gainsboro")
    button23.configure(background="gainsboro")
    button24.configure(background="gainsboro")
    button25.configure(background="gainsboro")
    button26.configure(background="gainsboro")
    button27.configure(background="gainsboro")
    button28.configure(background="gainsboro")
    button29.configure(background="gainsboro")
    button30.configure(background="gainsboro")
#=======================================================================================================================



#=======================================================================================================================

def ScoreKeeper1():
    if button1 :
        button1.configure(background="BLUE")
def ScoreKeeper2():
    if button6:
        button6.configure(background="RED")
def ScoreKeeper3():
    if button11:
        button11.configure(background="RED")
def ScoreKeeper4():
    if button16:
        button16.configure(background="RED")
def ScoreKeeper5():
    if button21:
        button21.configure(background="RED")


def ScoreKeeper6():
    if button2:
        button2.configure(background="BLUE")
def ScoreKeeper7():
    if button7:
        button7.configure(background="RED")
def ScoreKeeper8():
    if button12:
        button12.configure(background="RED")
def ScoreKeeper9():
    if button17:
        button17.configure(background="RED")
def ScoreKeeper10():
    if button22:
        button22.configure(background="RED")


def ScoreKeeper11():
    if button3:
        button3.configure(background="BLUE")
def ScoreKeeper12():
    if button8:
        button8.configure(background="RED")
def ScoreKeeper13():
    if button13:
        button13.configure(background="RED")
def ScoreKeeper14():
    if button18:
        button18.configure(background="RED")
def ScoreKeeper15():
    if button23:
        button23.configure(background="RED")


def ScoreKeeper16():
    if button4:
        button4.configure(background="BLUE")
def ScoreKeeper17():
    if button9:
        button9.configure(background="RED")
def ScoreKeeper18():
    if button14:
        button14.configure(background="RED")
def ScoreKeeper19():
    if button19:
        button19.configure(background="RED")
def ScoreKeeper20():
    if button24:
        button24.configure(background="RED")


def ScoreKeeper21():
    if button5:
        button5.configure(background="BLUE")
def ScoreKeeper22():
    if button10:
        button10.configure(background="RED")
def ScoreKeeper23():
    if button15:
        button15.configure(background="RED")
def ScoreKeeper24():
    if button20:
        button20.configure(background="RED")
def ScoreKeeper25():
    if button25:
        button25.configure(background="RED")


def ScoreKeeper26():
    if button26:
        button26.configure(background="RED")
def ScoreKeeper27():
    if button27:
        button27.configure(background="RED")
def ScoreKeeper28():
    if button28:
        button28.configure(background="RED")
def ScoreKeeper29():
    if button29:
        button29.configure(background="RED")
def ScoreKeeper30():
    if button30:
        button30.configure(background="RED")


#=======================================================================================================================

LeftFrame = Frame(root, bd=10, width=750, height=500, pady=2, padx=10, bg="BLACK", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(root, bd=10, width=750, height=500, pady=2, padx=10, bg="BLACK", relief=RIDGE)
RightFrame.pack(side=RIGHT)

#=======================================================================================================================


button1 = Button(LeftFrame, text="B", font=('Times 26 bold'), height = 2, width = 5, bg='WHITE',command=ScoreKeeper1)
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(LeftFrame, text="I", font=('Times 26 bold'), height = 2, width = 5, bg='WHITE',command=ScoreKeeper6)
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(LeftFrame, text="N", font=('Times 26 bold'), height = 2, width = 5, bg='WHITE',command=ScoreKeeper11)
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(LeftFrame, text="G", font=('Times 26 bold'), height = 2, width = 5, bg='WHITE',command=ScoreKeeper16)
button4.grid(row=1, column=3, sticky=S+N+E+W)

button5 = Button(LeftFrame, text="O", font=('Times 26 bold'), height = 2, width = 5, bg='WHITE',command=ScoreKeeper21)
button5.grid(row=1, column=4, sticky=S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper2)
button6.grid(row=2, column=0, sticky=S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper7)
button7.grid(row=2, column=1, sticky=S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper12)
button8.grid(row=2, column=2, sticky=S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper17)
button9.grid(row=2, column=3, sticky=S+N+E+W)

button10 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper22)
button10.grid(row=2, column=4, sticky=S+N+E+W)

button11 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper3)
button11.grid(row=3, column=0, sticky=S+N+E+W)

button12 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper8)
button12.grid(row=3, column=1, sticky=S+N+E+W)

button13 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper13)
button13.grid(row=3, column=2, sticky=S+N+E+W)

button14 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper18)
button14.grid(row=3, column=3, sticky=S+N+E+W)

button15 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper23)
button15.grid(row=3, column=4, sticky=S+N+E+W)

button16 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper4)
button16.grid(row=4, column=0, sticky=S+N+E+W)

button17 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper9)
button17.grid(row=4, column=1, sticky=S+N+E+W)

button18 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper14)
button18.grid(row=4, column=2, sticky=S+N+E+W)

button19 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper19)
button19.grid(row=4, column=3, sticky=S+N+E+W)

button20 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper24)
button20.grid(row=4, column=4, sticky=S+N+E+W)

button21 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper5)
button21.grid(row=5, column=0, sticky=S+N+E+W)

button22 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper10)
button22.grid(row=5, column=1, sticky=S+N+E+W)

button23 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper15)
button23.grid(row=5, column=2, sticky=S+N+E+W)

button24 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper20)
button24.grid(row=5, column=3, sticky=S+N+E+W)

button25 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper25)
button25.grid(row=5, column=4, sticky=S+N+E+W)

button26 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper26)
button26.grid(row=6, column=0, sticky=S+N+E+W)

button27 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper27)
button27.grid(row=6, column=1, sticky=S+N+E+W)

button28 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper28)
button28.grid(row=6, column=2, sticky=S+N+E+W)

button29 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper29)
button29.grid(row=6, column=3, sticky=S+N+E+W)

button30 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height = 2, width = 5, bg='gainsboro',command=ScoreKeeper30)
button30.grid(row=6, column=4, sticky=S+N+E+W)

butlist = [button6, button7, button8, button9, button10,
           button11, button12, button13, button14, button15,
           button16, button17, button18, button19, button20,
           button21, button22, button23, button24, button25,
           button26,button27,button28,button29,button30]
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(l)
for i in range(25):
    butlist[i]['text']=l[i]

def butlist():
    butlist = [button6, button7, button8, button9, button10,
           button11, button12, button13, button14, button15,
           button16, button17, button18, button19, button20,
           button21, button22, button23, button24, button25,
           button26,button27,button28,button29,button30]
    l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    random.shuffle(l)
    for i in range(25):
        butlist[i]['text']=l[i]

btnNewGame = Button(RightFrame, text="New Game", font=('arial',40,'bold'), height = 2, width = 10, bg="YELLOW", command=NewGame)
btnNewGame.grid(row=0, column=0, padx=6, pady=10)

btnExit = Button(RightFrame, text="Exit", font=('arial',40,'bold'), height = 2, width = 10, bg="GREEN", command=iExit)
btnExit.grid(row=0, column=1, padx=6, pady=11)

btnStart= Button(RightFrame, text="Start Game", font=('arial',40,'bold'), height = 2, width = 10, bg="BLUE", command=StartGame)
btnStart.grid(row=1, column=0, padx=10, pady=15)

btnSpeak= Button(RightFrame, text="BINGO", font=('arial',40,'bold'), height = 2, width = 10, bg="ORANGE", command=Speak)
btnSpeak.grid(row=1, column=1, padx=10, pady=15)

btnSpeak= Button(RightFrame, text="SHUFFLE", font=('arial',40,'bold'), height = 2, width = 10, bg="PINK", command=butlist)
btnSpeak.grid(row=2, column=0, padx=10, pady=15)

btnlabel = Label(RightFrame,text="BINGO",font=('arial',40,'bold'), height=2, width=10,bg="magenta")
btnlabel.grid(row=2, column=1, padx=10, pady=15)
#=======================================================================================================================

#=======================================================================================================================
def how_to_play():
    tkinter.messagebox.showinfo("HELP BOX","TAP ON START GAME AND ENJOY YOUR GAME AFTER FINISHING THE GAME TAP ON NEW GAME AND AGAIN TAP ON START GAME.IF YOU GET BINGO FIRST THEN TAP ON BINGO BUTTON QUICKLY AND IT WILL SAY BINGO STOP")

menubar = Menu(root)

filemenu = Menu(root, tearoff=0)
menubar.add_cascade(label="help",menu=filemenu)
filemenu.add_command(label="HOW TO PLAY", command=how_to_play)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command=iExit)

root.config(menu = menubar)
root.mainloop()
