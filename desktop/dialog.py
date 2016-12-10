import tkinter.messagebox as mb

ans = mb.askquestion("question","are you leke japanese sushi?")

if ans == True:
    mb.showinfo("agree", "me too")
else:
    mb.showinfo("really?", "oh, you hate japanese sushi!")
