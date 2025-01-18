import  tkinter #GUI

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=320,height=100)
window.config(padx=65,pady=50)

def button_clicked1():
    print(mile_input.get())
    mile = float(mile_input.get())
    kilometer = mile * 1.60934
    km_result_label.config(text = f"{kilometer}")

#miles input
mile_input = tkinter.Entry(width = 7)
mile_input.grid(column = 1, row = 0)

#lable
mile_label = tkinter.Label(text="Miles")
mile_label.grid(column = 2, row = 0)

button = tkinter.Button(text="Calculate",command = button_clicked1)
button.grid(column = 1, row=2)

is_equal_label = tkinter.Label(text = 'is equal to')
is_equal_label.grid(column = 0,row =1)

km_result_label = tkinter.Label(text = '0')
km_result_label.grid(column = 1, row =1)

km_label = tkinter.Label(text="Km")
km_label.grid(column = 2, row = 1)


window.mainloop() #to keep running window