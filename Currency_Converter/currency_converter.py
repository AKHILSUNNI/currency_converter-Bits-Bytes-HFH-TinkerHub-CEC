import requests
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image

root = Tk()

root.title("Currency Converter")

root.geometry("800x500")

photo = ImageTk.PhotoImage(Image.open("./bg.jpeg"))
img_label = Label(root,image=photo)
img_label.pack()

ip1 = StringVar(root)
ip2 = StringVar(root)

ip1.set("Select")
ip2.set("Select")


def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


def RealTimeCurrencyConversion() :
    
    if (output.get() == ""):
        
        from_currency = ip1.get()
        to_currency = ip2.get()

        if (value.get() ==""):
            tkinter.messagebox.showerror("Error","Amount Not Entered.\n")
        
        elif (from_currency == "Select" or to_currency == "Select"):
            tkinter.messagebox.showerror("Error","Currency Not Selected.\n")

        else :
            ak = requests.get(f"https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&apiKey=9b1ecf925bd17fc6153a")
            akh = ak.json()
            new_amt =  akh[f'{from_currency}_{to_currency}']*float(value.get())
            new_amount = float("{:.4f}".format(new_amt))
            output.insert(0, str(new_amount))
    else :
     tkinter.messagebox.showerror("Error","If you want to convert again, RESET and enter new amount.\n")


def clear():
    value.delete(0, END)
    output.delete(0, END)
    ip1.set("Select")
    ip2.set("Select")


CurrecyCode_list = ['USD','EUR','JPY','BGN','CZK','DKK','GBP','HUF','PLN','RON','SEK','CHF','ISK','NOK','HRK','RUB','TRY','AUD','BRL','CAD','CNY','HKD','IDR','INR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR']

label1 = Label(root,font=('Comic Sans MS',17,'bold'),text="Amount : ",fg="black",borderwidth=2,relief="solid")
label1.place(x=10, y=60)

label2 = Label(root,font=('Helvetica',15,'bold'),text="From : ",fg="black",bg="yellow",borderwidth=2,relief="solid")
label2.place(x=400, y=40)

label3 = Label(root,font=('Helvetica',15,'bold'),text="To : ",fg="black",borderwidth=2,relief="solid",bg="yellow")
label3.place(x=590, y=40)

label4 = Label(root,font=('Comic Sans MS',17,'bold'),text="Converted Amount : ",fg="black",borderwidth=2,relief="solid")
label4.place(x=10, y=250)

FromCurrency_option = OptionMenu(root,ip1, *CurrecyCode_list)
ToCurrency_option = OptionMenu(root,ip2, *CurrecyCode_list)

FromCurrency_option.place(x=490, y=40)
ToCurrency_option.place(x=650, y=40)


value = Entry(root,bd=4,font="Helvetica 15 bold")
value.place(x=130, y=60,width=150,height=35)

output = Entry(root,bd=4,font="Helvetica 15 bold")
output.place(x=250, y=250,width=150,height=35)


convert = Button(root,font=('arial',17,'bold'),text="Convert",fg="black",bg ="OliveDrab1",padx=2,pady=3,command= RealTimeCurrencyConversion,activeforeground="cornsilk3",activebackground="cornsilk2")
convert.place(x=50, y=150)
changeOnHover(convert, "cornsilk3", "OliveDrab1")

reset = Button(root,font=('arial',17,'bold'),text="Reset",fg="black",bg ="OliveDrab1",padx=2,pady=3,command= clear)
reset.place(x=250, y=150)
changeOnHover(reset, "cornsilk3", "OliveDrab1")

root.mainloop()