import tkinter as mk

def get_values():
    num_1 = int(number1_entry.get())
    num_2 = int(number2_entry.get())
    return num_1, num_2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num_1, num_2 = get_values()
    res = num_1 + num_2
    insert_values(res)

def sub():
    num_1, num_2 = get_values()
    res = num_1 - num_2
    insert_values(res)

def div():
    num_1, num_2 = get_values()
    res = num_1 / num_2
    insert_values(res)

def mul():
    num_1, num_2 = get_values()
    res = num_1 * num_2
    insert_values(res)

window = mk.Tk()
window.title('Калькулятор Максилятор')
window.geometry("400x400")
window.resizable(False, False)
button_add = mk.Button(window, text="+", width=7, height=3, command=add)
button_add.place(x=40, y=250)
button_sub = mk.Button(window, text="-", width=7, heaight=3, command=sub)
button_sub.place(x=130, y=250)
button_div = mk.Button(window, text="/", width=7, height=3, command=div)
button_div.place(x=220, y=250)
button_mul = mk.Button(window, text="*", width=7, height=3, command=mul)
button_mul.place(x=310, y=250)
number1_entry = mk.Entry(window, width=40)
number1_entry.place(x=60, y=70)
number2_entry = mk.Entry(window, width=40)
number2_entry.place(x=60, y=140)
answer_entry = mk.Entry(window, width=40)
answer_entry.place(x=60, y=360)
number_1 = mk.Label(window, text="Введите первое число" )
number_1.place(x=60, y=40)
number_2 = mk.Label(window, text="Введите второе число" )
number_2.place(x=60, y=110)
answer_ = mk.Label(window, text="Ответ" )
answer_.place(x=60, y=330)
window.mainloop()