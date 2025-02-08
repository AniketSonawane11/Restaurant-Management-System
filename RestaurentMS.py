#import area
from tkinter import *
import time
from tkinter import filedialog,messagebox
import random as r
import requests

#Fuctions

def save():
    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data = textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your BILL Is Succesfully Saved')

   

def reset():
    textReceipt.delete(1.0,END)
    e_roti.set('0')
    e_dal.set('0')
    e_rise.set('0')
    e_sabji.set('0')
    e_kabab.set('0')
    e_fish.set('0')
    e_mutton.set('0')
    e_chicken.set('0')
    e_paneer.set('0')

    #Add value into Drinks entry
    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_roohafza.set('0')
    e_masalachai.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    #Add value into Cackes entry
    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    textroti.config(state=DISABLED)
    textdal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textkabab.config(state=DISABLED)
    textrise.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textmasalachai.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textcoldrinks.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblack.config(state=DISABLED)

    costofcakesvar.set('')    
    costofdrinksvar.set('')    
    costoffoodvar.set('')    
    subcostvar.set('')    
    servicecostvar.set('')    
    totalcostvar.set('')    
    
    
def send():

    def send_msg():
        message = textarea.get(1.0,END)
        number = numberfield.get()
        auth = 'x2VqFhWG1ROsdzl4XcA8u0CImZ7DLKtf6wMjviQbT3oYJkrUSaNGKQdLUFbiJP4Cj3XnMhDEfOsuYcrt'
        url = 'https://www.fast2sms.com/dev/bulk'

        params = {
            'authorization' : auth,
            'message' : message,
            'numbers' : number,
            'sender-id' : 'FSTSMS',
            'route' : 'p',
            'language' : 'english'
        }
        response = requests.get(url,params=params)
        dic = response.json()
        result = dic.get('return')
        print('jsons response',result)
        if result == True:
            messagebox.showinfo('Send Succesfully','Message Sent Succesfully')
        else :
            messagebox.showerror('Error','Somthing went wrong')
        




    root2= Toplevel()
    root2.config(bg = 'red4')
    root2.title('SEND BILL')
    root2.geometry('488x620+50+50')
    root2.grab_set()
    root2.resizable(0,0)


    logoImage = PhotoImage(file='messages.png')
    logoLabel = Label(root2,image=logoImage, bg = 'red4')
    logoLabel.pack(pady=10)

    numberLabel = Label(root2,text='  Mobile Number  ',font=('arial',18,'bold underline'),bg='red4',fg='snow')
    numberLabel.pack()

    numberfield = Entry(root2,font=('helvetica',22),width=15)
    numberfield.pack(pady=10)
    
    fieldLabel = Label(root2,text='  Bill Details ',font=('arial',18,'bold underline'),bg='red4',fg='snow')
    fieldLabel.pack()

    textarea = Text(root2,font=('arial',12,'bold'),bd = 3,width=42,height=14)
    textarea.pack(pady=10)

    sendButton = Button(root2,text='Send',font=('times new roman',14,'bold'),width=15,background='green',foreground='white',activebackground='green',activeforeground='white',cursor='hand2',command=send_msg)
    sendButton.pack()
    textarea.insert(END,'*'*63)
    textarea.insert(END,'Recipt Ref:\t\t' + billnum + '\t\t' + date +'\n')
    textarea.insert(END,'*'*63)
    if costoffoodvar.get() != '0 Rs':
        textarea.insert(END,f'Cost Of Foof\t\t{priseofFood} Rs\n')

    if costofdrinksvar.get() != '0 Rs':
        textarea.insert(END,f'Cost Of Drinks\t\t{priseofDrinks} Rs\n')

    if costofcakesvar.get() != '0 Rs':
        textarea.insert(END,f'Cost Of Cakes\t\t{priseofCakes} Rs\n')
           
    textarea.insert(END,f'Sub TotalCost\t\t{subtotalofItems} Rs\n')
    textarea.insert(END,f'Service Tax\t\t{50} Rs\n\n')
    textarea.insert(END,'*'*63)
    textarea.insert(END,f'Total Cost\t\t{subtotalofItems + 50} Rs\n')
    textarea.insert(END,'*'*63)



    root.mainloop()


def receipt():
    global date,billnum
    textReceipt.delete(1.0,END)
    x = r.randint(100,1000)
    billnum = 'BiILL ' + str(x)
    date = time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'Receipt Ref:\t\t    '+billnum+'\t\t'+date)
    textReceipt.insert(END,'\n')
    textReceipt.insert(END,'*'*63)
    textReceipt.insert(END,'\n')
    textReceipt.insert(END,'Items:\t\t    Cost Of Items(Rs)\n')
    textReceipt.insert(END,'*'*63)
    textReceipt.insert(END,'\n')


    if e_roti.get() != '0':
        textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')

    if e_dal.get() != '0':
        textReceipt.insert(END,f'Daal\t\t\t{int(e_dal.get())*60}\n\n')

    if e_fish.get() != '0':
        textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*10}\n\n')

    if e_sabji.get() != '0':
        textReceipt.insert(END,f'Sabji\t\t\t{int(e_sabji.get())*50}\n\n')

    if e_rise.get() != '0':
        textReceipt.insert(END,f'Rise\t\t\t{int(e_roti.get())*30}\n\n')

    if e_paneer.get() != '0':
        textReceipt.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*100}\n\n')

    if e_kabab.get() != '0':
        textReceipt.insert(END,f'Kabab\t\t\t{int(e_kabab.get())*40}\n\n')

    if e_chicken.get() != '0':
        textReceipt.insert(END,f'Chicke\t\t\t{int(e_chicken.get())*120}\n\n')
    
    if e_mutton.get() != '0':
        textReceipt.insert(END,f'Mutton\t\t\t{int(e_mutton.get())*120}\n\n')

    if e_lassi.get() != '0':
        textReceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*50}\n\n')

    if e_coffee.get() != '0':
        textReceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*40}\n\n')

    if e_faluda.get() != '0':
        textReceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*80}\n\n')

    if e_shikanji.get() != '0':
        textReceipt.insert(END,f'Shikanji\t\t\t{int(e_shikanji.get())*30}\n\n')
    
    if e_roohafza.get() != '0':
        textReceipt.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*40}\n\n')

    if e_jaljeera.get() != '0':
        textReceipt.insert(END,f'Jaljeere\t\t\t{int(e_jaljeera.get())*60}\n\n')

    if e_masalachai.get() != '0':
        textReceipt.insert(END,f'Masala Tea\t\t\t{int(e_masalachai.get())*20}\n\n')

    if e_badammilk.get() != '0':
        textReceipt.insert(END,f'Badam Milk\t\t\t{int(e_badammilk.get())*50}\n\n')

    if e_coldrinks.get() != '0':
        textReceipt.insert(END,f'Cold Drinks\t\t\t{int(e_coldrinks.get())*80}\n\n')

    if e_oreo.get() != '0':
        textReceipt.insert(END,f'ore_Oreo\t\t\t{int(e_oreo.get())*10}\n\n')

    if e_apple.get() != '0':
        textReceipt.insert(END,f'Apple\t\t\t{int(e_apple.get())*300}\n\n')
    
    if e_kitkat.get() != '0':
        textReceipt.insert(END,f'KitKat\t\t\t{int(e_kitkat.get())*500}\n\n')

    if e_banana.get() != '0':
        textReceipt.insert(END,f'Banana\t\t\t{int(e_banana.get())*450}\n\n')
    
    if e_brownie.get() != '0':
        textReceipt.insert(END,f'Brownie\t\t\t{int(e_brownie.get())*800}\n\n')


    if e_vanilla.get() != '0':
        textReceipt.insert(END,f'Vanilla\t\t\t{int(e_vanilla.get())*550}\n\n')

    if e_pineapple.get() != '0':
        textReceipt.insert(END,f'Pineapple\t\t\t{int(e_pineapple.get())*620}\n\n')

    if e_chocolate.get() != '0':
        textReceipt.insert(END,f'Chocolate\t\t\t{int(e_chocolate.get())*700}\n\n')

    if e_blackforest.get() != '0':
        textReceipt.insert(END,f'Back Forest\t\t\t{int(e_blackforest.get())*550}\n\n')

    textReceipt.insert(END,'*'*63)
    textReceipt.insert(END,'\n')

    if costoffoodvar.get() != '0 Rs':
        textReceipt.insert(END,f'Cost Of Foof\t\t\t{priseofFood} Rs\n\n')

    if costofdrinksvar.get() != '0 Rs':
        textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priseofDrinks} Rs\n\n')

    if costofcakesvar.get() != '0 Rs':
        textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priseofCakes} Rs\n\n')
           
    textReceipt.insert(END,f'Sub TotalCost\t\t\t{subtotalofItems} Rs\n\n')
    textReceipt.insert(END,f'Service Tax\t\t\t{50} Rs\n\n')
    textReceipt.insert(END,f'Total Cost\t\t\t{subtotalofItems + 50} Rs\n\n')
    textReceipt.insert(END,'*'*63)
    textReceipt.insert(END,'\n')



    







def total():
    global priseofCakes,priseofDrinks,priseofFood,subtotalofItems,totalcost
    item1 = int(e_roti.get())
    item2 = int(e_dal.get())
    item3 = int(e_fish.get())
    item4 = int(e_sabji.get())
    item5 = int(e_kabab.get())
    item6 = int(e_rise.get())
    item7 = int(e_mutton.get())
    item8 = int(e_paneer.get())
    item9 = int(e_chicken.get())

    item10 = int(e_lassi.get())
    item11 = int(e_coffee.get())
    item12 = int(e_faluda.get())
    item13 = int(e_shikanji.get())
    item14 = int(e_roohafza.get())
    item15 = int(e_jaljeera.get())
    item16 = int(e_masalachai.get())
    item17 = int(e_badammilk.get())
    item18 = int(e_coldrinks.get())

    item19 = int(e_oreo.get())
    item20 = int(e_apple.get())
    item21 = int(e_kitkat.get())
    item22 = int(e_vanilla.get())
    item23 = int(e_banana.get())
    item24 = int(e_brownie.get())
    item25 = int(e_pineapple.get())
    item26 = int(e_chocolate.get())
    item27 = int(e_blackforest.get())

    priseofFood   = (item1 * 10) + (item2 * 60) +(item3 * 100) + (item4 * 50) + (item5 * 40) + (item6 * 30) + (item7 * 120) + (item8 * 100) + (item9 * 120)
    priseofDrinks = (item10 * 50) + (item11 * 40) + (item12 *80) +(item13 * 30) + (item14 * 40) + (item15 * 60) + (item16 * 20) + (item17 * 50) + (item18 * 80)
    priseofCakes  = (item19 * 400) + (item20 * 300) + (item21 * 500) + (item22 *550) +(item23 * 450) + (item24 * 800) + (item25 * 650) + (item26 * 700) + (item27 * 550) 

    costoffoodvar.set(str(priseofFood) + ' Rs')
    costofdrinksvar.set(str(priseofDrinks) + ' Rs')
    costofcakesvar.set(str(priseofCakes) + ' Rs')

    subtotalofItems = priseofCakes + priseofFood +priseofDrinks
    subcostvar.set(str(subtotalofItems) + ' Rs')

    servicecostvar.set('50 Rs')

    totalcost = subtotalofItems + 50
    totalcostvar.set(str(totalcost) + ' Rs')


def roti_ch():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def dal_ch():
    if var2.get() == 1:
        textdal.config(state=NORMAL)
        textdal.delete(0,END)
        textdal.focus()
    else:
        textdal.config(state=DISABLED)
        e_dal.set('0')    

def fish_ch():
    if var3.get() == 1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def sabli_ch():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kabab_ch():
    if var5.get() == 1:
        textkabab.config(state=NORMAL)
        textkabab.delete(0,END)
        textkabab.focus()
    else:
        textkabab.config(state=DISABLED)
        e_kabab.set('0')

def rise_ch():
    if var6.get() == 1:
        textrise.config(state=NORMAL)
        textrise.delete(0,END)
        textrise.focus()
    else:
        textrise.config(state=DISABLED)
        e_rise.set('0')

def mutton_ch():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer_ch():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def chicken_ch():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def lassi_ch():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def coffee_ch():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def faluda_ch():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')        

def shikanji_ch():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')

def roohafza_ch():
    if var14.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()
    else:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')

def jaljeera_ch():
    if var15.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')

def masalachai_ch():
    if var16.get() == 1:
        textmasalachai.config(state=NORMAL)
        textmasalachai.delete(0,END)
        textmasalachai.focus()
    else:
        textmasalachai.config(state=DISABLED)
        e_masalachai.set('0')

def badammilk_ch():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()
    else:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')

def coldrinks_ch():
    if var18.get() == 1:
        textcoldrinks.config(state=NORMAL)
        textcoldrinks.delete(0,END)
        textcoldrinks.focus()
    else:
        textcoldrinks.config(state=DISABLED)
        e_coldrinks.set('0')        

def oreo_ch():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def apple_ch():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')

def kitkat_ch():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')

def vanilla_ch():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')

def banana_ch():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')

def brownie_ch():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')

def pineapple_ch():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textdal.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')

def chocolate_ch():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')

def black_ch():
    if var27.get() == 1:
        textblack.config(state=NORMAL)
        textblack.delete(0,END)
        textblack.focus()
    else:
        textblack.config(state=DISABLED)
        e_blackforest.set('0')



#Font 
f = ('times new',30)


#Main Window
root = Tk()
root.geometry('1275x690+0+0')
root.resizable(0,0)
root.title('RestaurantManagementSystem')
root.config(background='firebrick4')

#Creating Top frame 
topFrame = Frame(root,border=10,relief=RIDGE,background='firebrick4')
topFrame.pack(side = TOP)

#Title lable frame
lableTitle = Label(topFrame,text='Restaurant Management System',font = ('arial',30,'bold'),foreground='yellow',background='red4',width=52)
lableTitle.grid(row=0,column=0)

#Menu frame
menuFrame = Frame(root,border=10,relief=RIDGE,background='firebrick4')
menuFrame.pack(side=LEFT)

#cost frame
costFrame = Frame(menuFrame,border=10,relief=RIDGE,background='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

#Food leble
foodFrame = LabelFrame(menuFrame,text='Food',font = ('arial',19,'bold'),border=10,relief=RIDGE,foreground='firebrick4')
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame,text='Drinks',font = ('arial',19,'bold'),border=10,relief=RIDGE,foreground='firebrick4')
drinksFrame.pack(side=LEFT)

cakesFrame = LabelFrame(menuFrame,text='Cakes',font = ('arial',19,'bold'),border=10,relief=RIDGE,foreground='firebrick4')
cakesFrame.pack(side=LEFT)

rightFrame= Frame(root,border=15,relief=RIDGE,background='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame,border=1,relief=RIDGE,background='red4')
calculatorFrame.pack()

reciptFrame = Frame(rightFrame,border=4,relief=RIDGE,background='red4')
reciptFrame.pack()

buttonFrame = Frame(rightFrame,border=4,relief=RIDGE,background='red4')
buttonFrame.pack()

#Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti = StringVar()
e_dal = StringVar()
e_sabji = StringVar()
e_rise = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kabab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalachai = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_oreo = StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costofdrinksvar = StringVar()
costoffoodvar = StringVar()
costofcakesvar = StringVar()
subcostvar = StringVar()
totalcostvar = StringVar()
servicecostvar = StringVar()



#Food checked buttons

roti = Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti_ch)
roti.grid(row=0,column=0,sticky=W)

dal = Checkbutton(foodFrame,text='Dal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=dal_ch)
dal.grid(row=1,column=0,sticky=W)

fish = Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=fish_ch)
fish.grid(row=2,column=0,sticky=W)

sabji= Checkbutton(foodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=sabli_ch)
sabji.grid(row=3,column=0,sticky=W)

kabab = Checkbutton(foodFrame,text='Kabab',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=kabab_ch)
kabab.grid(row=4,column=0,sticky=W)

rise = Checkbutton(foodFrame,text='Rise',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=rise_ch)
rise.grid(row=5,column=0,sticky=W)

mutton = Checkbutton(foodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=mutton_ch)
mutton.grid(row=6,column=0,sticky=W)

paneer = Checkbutton(foodFrame,text='Panner',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=paneer_ch)
paneer.grid(row=7,column=0,sticky=W)

chicken = Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=chicken_ch)
chicken.grid(row=8,column=0,sticky=W)

#Entry text

textroti = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdal = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_dal)
textdal.grid(row=1,column=1)

textfish = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=3,column=1)

textkabab = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_kabab)
textkabab.grid(row=4,column=1)

textrise = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_rise)
textrise.grid(row=5,column=1)

textmutton = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=6,column=1)

textpaneer = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=7,column=1)

textchicken = Entry(foodFrame,font=('arial',18,),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=8,column=1)



#Drinks

lassi = Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi_ch)
lassi.grid(row=0,column=0,sticky=W)

coffee = Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee_ch)
coffee.grid(row=1,column=0,sticky=W)

faluda = Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=faluda_ch)
faluda.grid(row=2,column=0,sticky=W)

shikanji = Checkbutton(drinksFrame,text='Shikanji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=shikanji_ch)
shikanji.grid(row=3,column=0,sticky=W)

roohafza= Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=roohafza_ch)
roohafza.grid(row=4,column=0,sticky=W)

jaljeera = Checkbutton(drinksFrame,text='Jaljeera',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=jaljeera_ch)
jaljeera.grid(row=5,column=0,sticky=W)

masalatea = Checkbutton(drinksFrame,text='Masala Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=masalachai_ch)
masalatea.grid(row=6,column=0,sticky=W)

badammilk = Checkbutton(drinksFrame,text='Badam Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=badammilk_ch)
badammilk.grid(row=7,column=0,sticky=W)

coldrink = Checkbutton(drinksFrame,text='Cold Drink',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=coldrinks_ch)
coldrink.grid(row=8,column=0,sticky=W)



#Drinks Entry

textlassi = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textfaluda = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=2,column=1)

textshikanji = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_shikanji)
textshikanji.grid(row=3,column=1)

textroohafza = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=4,column=1)

textjaljeera = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=5,column=1)

textmasalachai = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_masalachai)
textmasalachai.grid(row=6,column=1)

textbadammilk = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_badammilk)
textbadammilk.grid(row=7,column=1)

textcoldrinks = Entry(drinksFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_coldrinks)
textcoldrinks.grid(row=8,column=1)


#Cakes

oreocake = Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreo_ch)
oreocake.grid(row=0,column=0,sticky=W)

applecake = Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=apple_ch)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake = Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=kitkat_ch)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake = Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanilla_ch)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake = Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=banana_ch)
bananacake.grid(row=4,column=0,sticky=W)

browniecake = Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=brownie_ch)
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake = Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=pineapple_ch)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake = Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=chocolate_ch)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake = Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=black_ch)
blackforestcake.grid(row=8,column=0,sticky=W)


#Cakes Entry

textoreo = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textkitkat = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)

textbrownie = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5,column=1)

textpineapple = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)

textchocolate = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)

textblack = Entry(cakesFrame,font=('arial',18),bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblack.grid(row=8,column=1)


#Add value into Food entry
e_roti.set('0')
e_dal.set('0')
e_rise.set('0')
e_sabji.set('0')
e_kabab.set('0')
e_fish.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

#Add value into Drinks entry
e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_roohafza.set('0')
e_masalachai.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

#Add value into Cackes entry
e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')
e_blackforest.set('0')

#Costlabel and entry fields

labelCostofFood = Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),background='firebrick4',foreground='white')
labelCostofFood.grid(row=0,column=0)

textCostFood = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostFood.grid(row=0,column=1,padx =40)


labelCostofDrinks = Label(costFrame,text=' Cost of Drinks',font=('arial',16,'bold'),background='firebrick4',foreground='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx =40)


labelCostofCakes = Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),background='firebrick4',foreground='white')
labelCostofCakes.grid(row=2,column=0)

textCostCakes = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostCakes.grid(row=2,column=1,padx =40)


labelSubTotal = Label(costFrame,text='Sub Total',font=('arial',16,'bold'),background='firebrick4',foreground='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subcostvar)
textSubTotal.grid(row=0,column=3,padx =40)


labelServiceTax = Label(costFrame,text='Service Tax',font=('arial',16,'bold'),background='firebrick4',foreground='white')
labelServiceTax.grid(row=1,column=2)

textServieTax = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicecostvar)
textServieTax.grid(row=1,column=3,padx =40)


labelTotalCost = Label(costFrame,text='Total Cost',font=('arial',16,'bold'),background='firebrick4',foreground='white')
labelTotalCost.grid(row=2,column=2)

texTotalCost = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
texTotalCost.grid(row=2,column=3,padx =40)


#Buttons

buttonTotal =Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='white',command=total)
buttonTotal.grid(row=0,column=0)

buttonReceipt =Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='white',command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave =Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='white',command=save)
buttonSave.grid(row=0,column=2)

buttonSend =Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='white',command=send)
buttonSend.grid(row=0,column=3)

buttonReset =Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='white',command=reset)
buttonReset.grid(row=0,column=4)

#Text area for receipt
f = ('arial',12,'bold')
textReceipt = Text(reciptFrame,font=f,bd=3,width=42,height=16)
textReceipt.grid(row=0,column=0)

#Calculator
f = ('arial',16)

operator = ''
def buttonClick(number):
    global operator
    operator = operator + number
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    calculatorField.delete(0,END)
    operator=''

def ans():
    global operator
    result =eval(operator)
    calculatorField.delete(0,END)
    operator=''
    calculatorField.insert(0,result)




calculatorField = Entry(calculatorFrame,font=f,width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7 =Button(calculatorFrame,text='7',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8 =Button(calculatorFrame,text='8',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=7,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9 =Button(calculatorFrame,text='9',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=7,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonplus =Button(calculatorFrame,text='+',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

button4 =Button(calculatorFrame,text='4',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5 =Button(calculatorFrame,text='5',font=('arial',14,'bold'),fg='red4',bg='white',bd=3,padx=5,activebackground='white',activeforeground='red4',width=7,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6 =Button(calculatorFrame,text='6',font=('arial',14,'bold'),fg='red4',bg='white',bd=3,padx=5,activebackground='white',activeforeground='red4',width=7,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonminus =Button(calculatorFrame,text='-',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)

button1 =Button(calculatorFrame,text='1',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2 =Button(calculatorFrame,text='2',font=('arial',14,'bold'),fg='red4',bg='white',bd=3,padx=5,activebackground='white',activeforeground='red4',width=7,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3 =Button(calculatorFrame,text='3',font=('arial',14,'bold'),fg='red4',bg='white',bd=3,padx=5,activebackground='white',activeforeground='red4',width=7,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonmul =Button(calculatorFrame,text='x',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:buttonClick('*'))
buttonmul.grid(row=3,column=3)

buttonans =Button(calculatorFrame,text='Ans',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:ans())
buttonans.grid(row=4,column=0)

buttonclear =Button(calculatorFrame,text='Clear',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=7,command=lambda:clear())
buttonclear.grid(row=4,column=1)

button0 =Button(calculatorFrame,text='0',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=7,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttondiv =Button(calculatorFrame,text='/',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=3,padx=5,activebackground='red4',activeforeground='yellow',width=6,command=lambda:buttonClick('/'))
buttondiv.grid(row=4,column=3)

root.mainloop()