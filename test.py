from tkinter import *
window=Tk()
window.title("My Calculator")
display=Entry(window, width=56,bg='yellow')
display.grid(row=0,column=0,columnspan=5)

button_list=['7','8','9','/','C','4','5','6','*','','1','2','3','-','','0','.','=','+','']

row_ind=1
col_ind=0

for dis_text in button_list:
    
    def cal(t=dis_text):
        if t =='=':
            result=eval(display.get())
            display.insert(END, "=" + str(result))
        elif t == "C":
            display.delete(0, END)
        else:
            display.insert(END, t)
            
    Button(window,text=dis_text,width=10, command = cal).grid(row=row_ind,column=col_ind)
    col_ind+=1
    if col_ind>4:
        row_ind+=1
        col_ind=0
