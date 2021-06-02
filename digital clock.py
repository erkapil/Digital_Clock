from tkinter import*
import time
dclock = Tk()
dclock.title("digital clock")
dclock.configure(bg="light green")
dclock.resizable(width=True, height=True)
#define Label

hl = Label(dclock, bg="#000000", fg="#EB00FF", font="Roboto 16 bold")
hs = Label(dclock, text=":",  bg="#000000", fg="#EB00FF", font="Roboto 16 bold")
ml = Label(dclock, bg="#000000", fg="#EB00FF", font="Roboto 16 bold")
ms = Label(dclock, text=":", bg="#000000", fg="#EB00FF", font="Roboto 16 bold")
ql = Label(dclock, bg="#000000", fg="#EB00FF", font="Roboto 16 bold")

# define grid
hl.grid(row=1, column=1, padx=5, pady=5)
hs.grid(row=1, column=2, padx=5, pady=5)
ml.grid(row=1, column=3, padx=5, pady=5)
ms.grid(row=1, column=4, padx=5, pady=5)
ql.grid(row=1, column=5, padx=5, pady=5)

# craete loop :

while True:
    seconds = time.time()
    c_time = time.localtime(seconds)

    #define hours :
    if c_time.tm_hour < 00:

        hl.config(text="fO{c_time.tm_hour}")
        hl.update()
    else:
        hl.config(text=c_time.tm_hour)
        hl.update()

    # define minuts :
    if c_time.tm_min < 00:

        ml.config(text="fO{c_time.tm_min}")
        ml.update()
    else:
        ml.config(text=c_time.tm_min)
        ml.update()

        # define seconds :
    if c_time.tm_sec < 00:

        ql.config(text=c_time.tm_sec)
        ql.update()
    else:
        ql.configure(text=c_time.tm_sec)
        ql.update()
dclock.mainloop()