from tkinter import*
window = Tk()
window.title("addition")
window.geometry("400x400")
window.configure(bg="white")

heading_lbl=Label(window,text = "addition",fg ="red",font =("arial",20) )
heading_lbl.place(x=200,y=40,anchor=CENTER)

num1=Label(window,text = "enter first number")
num1.place(x=100,y=100,anchor=CENTER)

num2=Label(window,text = "enter second number")
num2.place(x=100,y=140,anchor= CENTER)

N1=Entry(window)
N1.place(x=300,y=100,anchor=CENTER)

N2=Entry(window)
N2.place(x=300,y=140,anchor=CENTER)

result_frame=LabelFrame(window,text="result")
result_frame.pack(padx=20,pady=30)
result_frame.place(x=200,y=300,anchor=CENTER)

result_lbl=Label(window)
result_lbl.place(x=200,y=350,anchor=CENTER )
result_lbl.pack()

def add():
    n1=int(N1.get())
    n2=int(N2.get())
    sum=n1+n2
    result_lbl.destroy()
    final_result=Label(result_frame,text="answer = "+str(sum))
    final_result.place(x=200,y=350,anchor = CENTER)
    final_result.pack()

btn=Button(window,text = "show result",command=add)
btn.place(x=200,y=200,anchor=CENTER)

window.mainloop()