from tkinter import *
from tkinter import ttk as t
from tkinter import messagebox
import json
import urllib.request


root = Tk()
root.geometry('220x340+540+200')
root.title('С.С.')
root.resizable(False, False)


def reverse():
    x = float(entry.get())
    y = float(JSON_object[0]['buy'])
    result = x * y
    entry.insert(0, result)


def reset():
    entry.delete(0, END)

def exchange_usd():
    entry.insert(0, round(float(entry.get()) / float(JSON_object[0]['sale']), 2))

def exchange_eur():
    entry.insert(0, round(float(entry.get()) / float(JSON_object[1]['sale']), 2))


def exchange_rub():
    entry.insert(0, round(float(entry.get()) / float(JSON_object[2]['sale']), 2))
    

def exchange_btc():
    entry.insert(0, round(float(entry.get()) / float(JSON_object[3]['sale']), 2))

try:
    html = urllib.request.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showinfo('Error', 'Error getting exchange rates')


label = Label(root)
label.pack(expand=1)

# CURRENCY
t_currency = Label(label, text="Currency", bg="#778899", font="Arial 12")
t_currency.grid(row=0, column=0, sticky=EW)
usd_currency = Label(label, text="USD", bg="#FFFAFA", font="Arial 12")
usd_currency.grid(row=1, column=0, sticky=EW)
eur_currency = Label(label, text="EUR", bg="#FFFAFA", font="Arial 12")
eur_currency.grid(row=2, column=0, sticky=EW)
rub_currency = Label(label, text="RUB", bg="#FFFAFA", font="Arial 12")
rub_currency.grid(row=3, column=0, sticky=EW)
btc_currency = Label(label, text="BTC", bg="#FFFAFA", font="Arial 10")
btc_currency.grid(row=4, column=0, sticky=EW)


#BUY
t_buy = Label(label, text="Buy", bg="#778899", font="Arial 12")
t_buy.grid(row=0, column=1, sticky=EW)
t_buy_usd = Label(label, text=JSON_object[0]['buy'], bg="#FFFAFA", font="Arial 12")
t_buy_usd.grid(row=1, column=1, sticky=EW)
t_buy_eur = Label(label, text=JSON_object[1]['buy'], bg="#FFFAFA", font="Arial 12")
t_buy_eur.grid(row=2, column=1, sticky=EW)
t_buy_rub = Label(label, text=JSON_object[2]['buy'], bg="#FFFAFA", font="Arial 12")
t_buy_rub.grid(row=3, column=1, sticky=EW)
t_buy_btc = Label(label, text=JSON_object[3]['buy'], bg="#FFFAFA", font="Arial 10")
t_buy_btc.grid(row=4, column=1, sticky=EW)


#SALE
t_sale = Label(label, text="Sale", bg="#778899", font="Arial 12")
t_sale.grid(row=0, column=2, sticky=EW)
t_sale_usd = Label(label, text=JSON_object[0]['sale'], bg="#FFFAFA", font="Arial 12")
t_sale_usd.grid(row=1, column=2, sticky=EW)
t_sale_eur = Label(label, text=JSON_object[1]['sale'], bg="#FFFAFA", font="Arial 12")
t_sale_eur.grid(row=2, column=2, sticky=EW)
t_sale_rub = Label(label, text=JSON_object[2]['sale'], bg="#FFFAFA", font="Arial 12")
t_sale_rub.grid(row=3, column=2, sticky=EW)
t_sale_btc = Label(label, text=JSON_object[3]['sale'], bg="#FFFAFA", font="Arial 10")
t_sale_btc.grid(row=4, column=2, sticky=EW)      



scale1 = Scale(root, orient=HORIZONTAL, from_=0, to=10000, bg='#FFFAFA', fg='maroon')
scale1.pack(fill=X)

def getV(root):
    a = scale1.get()
    entry.delete(0, END)
    entry.insert(0, a)


scale1.bind("<Button-1>", getV)

entry = Entry(root)
entry.pack(fill=X)

s = t.Style()
s.configure('Kim.TButton', foreground='maroon')

#ALL BUTTON
frame2 = Frame(root, bg='#FFFAFA')
frame2.pack(fill=X, expand=1, side=RIGHT)

s2 = t.Style()
s2.configure('RES.TButton', background='red', foreground='tomato')


btn_reverse_usd = t.Button(frame2, text='REVERSE USD', style='RES.TButton', command=reverse)
btn_reverse_usd.pack(fill=X, expand=True, side=TOP)

btn_reset = t.Button(frame2, text='RESET', style='RES.TButton', command=reset)
btn_reset.pack(fill=X, expand=True, side=TOP)

btn_usd = t.Button(frame2, text='USD', style='Kim.TButton', command=exchange_usd)
btn_usd.pack(fill=X, expand=True, side=TOP)

btn_eur = t.Button(frame2, text='EUR', style='Kim.TButton', command=exchange_eur)
btn_eur.pack(fill=X, expand=True, side=TOP)

btn_rub = t.Button(frame2, text='RUB', style='Kim.TButton', command=exchange_rub)
btn_rub.pack(fill=X, expand=True, side=TOP)

btn_btc = t.Button(frame2, text='BTC', style='Kim.TButton', command=exchange_btc)
btn_btc.pack(fill=X, expand=True, side=TOP)


root.mainloop()