from tkinter import *

window = Tk()
window.geometry('350x200')
window.title("Primtals beregner")

lbl = Label(window, text="Indtast et tal og find ud af om det er et primtal")
lbl.grid(column=0, row=0)

txt = Entry(window, width=20)
txt.grid(column=0, row=1)

#functions
def er_primtal(n):
    if n < 2:
        return False
    if n in (2, 3):  # 2 og 3 er primtal
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def Primtal():
    try:
        tal = int(txt.get())
        if er_primtal(tal):
            lbl.configure(text=f"{tal} er et primal.  prøv et nyt tal")
        else:
            lbl.configure(text=f"{tal} er IKKE et primal. prøv et nyt tal")
    except ValueError:
        lbl.configure(text="Indtast et gyldigt tal")

btn = Button(window, text="Go", width=10, command=Primtal)
btn.grid(column=1, row=1)

window.mainloop()

