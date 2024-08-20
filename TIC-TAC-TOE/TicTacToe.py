import tkinter.messagebox
from  tkinter import *


root = Tk()     # creating instance of root 

root.title("TIC TAC TOE")   # title is used to make a home title 
root.geometry("1000x750+0+0")
root.configure(background="purple")  # To set the background color
root.iconbitmap("E:\PythonMaterial\ICONS\icon1.ico")



Tops= Frame(root,bg="Purple",pady=2,width=1350,height=100,relief="ridge")
Tops.grid(row=0,column=0)

lblTitle = Label(root,text="Advance Tic Tac Toe Game",font=("Helvtica", 26),bd=21,bg="Purple",fg="Cornsilk",justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame= Frame(root,bg="Powder Blue",pady=2,width=1350,height=600,relief="ridge")
MainFrame.grid(row=1,column=0)

LeftFrame= Frame(MainFrame,bg="Cadet Blue",bd=10,padx=2,pady=10,width=750,height=500,relief="ridge")
LeftFrame.pack(side=LEFT)

RightFrame= Frame(MainFrame,bg="Cadet Blue",bd=10,padx=2,pady=10,width=560,height=500,relief="ridge")
RightFrame.pack(side=RIGHT)

RightFrame1= Frame(RightFrame,bg="Cadet Blue",bd=10,padx=2,pady=10,width=560,height=200,relief="ridge")
RightFrame1.grid(row=0,column=0)

RightFrame2= Frame(RightFrame,bg="Cadet Blue",bd=10,padx=2,pady=10,width=560,height=200,relief="ridge")
RightFrame2.grid(row=1,column=0)

PlayerX= IntVar()
PlayerO= IntVar()

PlayerX.set(0)
PlayerO.set(0)

Player1= StringVar()     # is a variable for entering the player name ...
Player2= StringVar()

pa= StringVar()
pb= StringVar()


buttons= StringVar()
click = True

def check(buttons):                             
    global click
    if(buttons["text"]==" " and click == True):
        buttons["text"]="X"
        click = False
        scorekeeper()
    elif(buttons["text"]==" " and click == False):
        buttons["text"]="O"
        click = True 
        scorekeeper()
        
def reset():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    
    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")
    
def NewGame():
    global Player1 , Player2, pa,pb
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    Player1= StringVar()
    Player2= StringVar()
    
    nmPLayerX=Entry(RightFrame1,font=("Times",40,'bold'),bd=3,fg="black",textvariable= Player1,width=7,
                 justify=LEFT).grid(row=0,column=1)
    nmPlayerO=Entry(RightFrame1,font=("Times",40,'bold'),bd=3,fg="black",textvariable= Player2,width=7,
                 justify=LEFT).grid(row=1,column=1)
    
def scorekeeper():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" ):
        button1.configure(background="green")
        button2.configure(background="green")
        button3.configure(background="green")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa)
        reset()
        
        
    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" ):
        button4.configure(background="grey")
        button5.configure(background="grey")
        button6.configure(background="grey")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa)
        reset()
    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" ):
        button7.configure(background="light green")
        button8.configure(background="light green")
        button9.configure(background="light green")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa) 
        reset()
    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" ):
        button1.configure(background="green")
        button5.configure(background="green")
        button9.configure(background="green")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa)
        reset()
    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" ):
        button3.configure(background="grey")
        button5.configure(background="grey")
        button7.configure(background="grey")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa)
        reset()
    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" ):
        button1.configure(background="grey")
        button4.configure(background="grey")
        button7.configure(background="grey")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa)
        reset()
    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" ):
        button2.configure(background="grey")
        button5.configure(background="grey")
        button8.configure(background="grey")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa)
        reset()
    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" ):
        button3.configure(background="grey")
        button6.configure(background="grey")
        button9.configure(background="grey")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        pa= Player1.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pa)
        reset()
                                    
                                    
                                    
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" ):
        button1.configure(background="grey")
        button2.configure(background="grey")
        button3.configure(background="grey")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb)
        reset()
        
    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" ):
        button4.configure(background="green")
        button5.configure(background="green")
        button6.configure(background="green")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb)
        reset()
    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" ):
        button7.configure(background="light green")
        button8.configure(background="light green")
        button9.configure(background="light green")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb)
        reset()
    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" ):
        button1.configure(background="grey")
        button5.configure(background="grey")
        button9.configure(background="grey")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"                            
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb) 
        reset()
    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" ):
        button3.configure(background="green")
        button5.configure(background="green")
        button7.configure(background="green")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"  
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb)
        reset()
    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" ):
        button1.configure(background="grey")
        button4.configure(background="grey")
        button7.configure(background="grey")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb)
        reset()
    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" ):
        button2.configure(background="light green")
        button5.configure(background="light green")
        button8.configure(background="light green")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb)
        reset()
    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" ):
        button3.configure(background="grey")
        button6.configure(background="grey")
        button9.configure(background="grey")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        pb= Player2.get() + " Won the game!"
        tkinter.messagebox.showinfo("CONGRATES !YOU WON THE GAME",pb)
        reset()
                                    
            
# labelling the Rigt Frame 1 for player 1
lblPlayerX = Label(RightFrame1,font=("Times",40,'bold'),padx=2,pady=2,text="Player X:",bg="Cadet Blue")
lblPlayerX.grid(row=0,column=0,sticky=W)
nmPLayerX=Entry(RightFrame1,font=("Times",40,'bold'),bd=3,fg="black",bg="light blue",textvariable= Player1,width=7,
                 justify=LEFT).grid(row=0,column=1)
txtPLayerX = Entry(RightFrame1,font=("Times",26,'bold'),bd=2,fg="black",bg="light blue",textvariable=PlayerX,width=7,
                   justify=LEFT).grid(row=0,column=2)

# labelling the Rigt Frame 1 for player 2
lblPlayerO = Label(RightFrame1,font=("Times",40,'bold'),padx=2,pady=2,text="Player O:",bg="Cadet Blue")
lblPlayerO.grid(row=1,column=0,sticky=W)
nmPLayerO=Entry(RightFrame1,font=("Times",40,'bold'),bd=3,fg="black",bg="light green",textvariable= Player2,width=7,
                 justify=LEFT).grid(row=1,column=1)
txtPLayerO = Entry(RightFrame1,font=("Times",26,'bold'),bd=2,fg="black",bg="light green",textvariable=PlayerO,width=7,
                   justify=LEFT).grid(row=1,column=2)

# Button for Resetting the game
btnReset =Button(RightFrame2,text="RESET",font=("Times" ,26,"bold"),width=12,height=2,bg='gainsboro',command=reset)
btnReset.grid(row=0,column=0, padx=5,pady=10)

# Button for  the New  game
btnNewGame =Button(RightFrame2,text="New Game ",font=("Times" ,26,"bold"),width=12,height=2,bg='gainsboro',command=NewGame)
btnNewGame.grid(row=1,column=0,padx=5,pady=10)


button1 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 =Button(LeftFrame,text=" ",font=("Helvtica 26"),width=8,height=3,bg='gainsboro',command=lambda:check(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)



root.mainloop()  
