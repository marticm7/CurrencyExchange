from tkinter import *
def promeni1():
    unos_din = int(entry1.get())
    unos_din = unos_din/117.3235
    output_label.configure(text='Konvertovano: {:.1f}'.format(unos_din))
    entry1.delete(0,END)

def promeni2():
    unos_evro = int(entry2.get())
    unos_evro = unos_evro*117.3235
    output_label.configure(text='Konvertovano: {:.1f}'.format(unos_evro))

    entry2.delete(0,END)


root=Tk()

message_label1 = Label(text='Unesite iznos u dinarima',font=('Garamond', 14))
output_label = Label(font=('Garamond', 14))
entry1 = Entry(font=('Garamond', 14), width=10)
calc_button = Button(text='Promeni', bg='red', font=('Garamond', 14),command=promeni1)
message_label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1,column=0,columnspan=3)

message_label = Label(text='Unesite iznos u evrima',font=('Garamond', 14))
output_label = Label(font=('Garamond', 14))
entry2 = Entry(font=('Garamond', 14), width=10)
calc_button = Button(text='Promeni', bg='red', font=('Garamond', 14),command=promeni2)
message_label.grid(row=1, column=0)
entry2.grid(row=1, column=1)
calc_button.grid(row=1, column=2)
output_label.grid(row=2,column=1,columnspan=4)


mainloop()