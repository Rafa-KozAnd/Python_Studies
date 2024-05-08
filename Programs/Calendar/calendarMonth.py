from tkinter import *
import calendar

def initCalendar():
    newWindow = Tk()
    newWindow.config(background="white")
    newWindow.title("Calendário em Python")
    newWindow.geometry("575x575")

    fetch_year = int(year_field.get())
    calendar_content = calendar.calendar(fetch_year)
    calendar_year = Label(newWindow, text=calendar_content, font=("Comic Sans", 10 ,"bold"))
    calendar_year.grid(row=5, column=1, padx=20)
    newWindow.mainloop()

if __name__ == "__main__":
    window = Tk()
    window.config(background="Light gray")
    window.title("Calendário em Python")
    window.geometry("300x190")

    cal = Label(window, text="Calendário", bg="Light gray", font=("Comic Sans", 40, "bold"))
    year = Label(window, text="Digite o ano desejado para ver os meses:", bg="white", font = 35)
    year_field = Entry(window, font=20)
    Show = Button(window, text="Iniciar Calendário", fg="black", bg="Light Blue", font = 30, command = initCalendar)
    Exit = Button(window, text="Sair", fg="black", bg="Red", font=20, command=exit)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
   
    window.mainloop()