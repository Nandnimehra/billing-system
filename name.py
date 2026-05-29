from tkinter import *
from tkinter import messagebox,END
import random,os
#functionality part

def search_bill():
    bill_no = billnumberEntry.get().strip()   # remove spaces
    found = False

    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_no:        # exact match with filename (without extension)
            with open(os.path.join('bills', i), 'r') as f:   # safe path join
                textarea.delete('1.0', END)
                textarea.insert(END, f.read())
            found = True
            break

    if not found:
        messagebox.showerror('Error', 'Invalid Bill Number')

# def search_bill():
#     for i in os.listdir('bills/'):
#         if i.split('.')[0]==billnumberEntry.get():
#             f=open(f'bills/{i}','r')
#             textarea.delete('1.0',END)
#             for data in f:
#                 textarea.insert(END,data)
#             f.close()
#             break
#     else:
#         messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')




def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        fill=open(f'bills/ {billnumber}.txt','w')
        fill.write(bill_content)
        fill.close()
        messagebox.showinfo('Success', f'bill number{billnumber} is saved successfully')
        billnumber=random.randint(500,1000)







billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkpriceEntry.get() == '':
        messagebox.showerror('Error', 'No Products are selected')
    elif cosmeticpriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and drinkpriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No Products are selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f'Bill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number:{phoneEntry.get()}\n')
        textarea.insert(END, '\n=======================================================')
        textarea.insert(END, 'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        if bathsoapEntry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get() != '0':
            textarea.insert(END, f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'\nFace wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'\nFace cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')

        # grocery
        if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if daalEntry.get() != '0':
            textarea.insert(END, f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if oilEntry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if sugarEntry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if teaEntry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')

        # drink
        if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if dewEntry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if cococolaEntry.get() != '0':
            textarea.insert(END, f'\nCococola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs')
        textarea.insert(END, '\n-------------------------------------------------------')

        if cosmetictaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get() != '0.0Rs':
            textarea.insert(END, f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if drinktaxEntry.get() != '0.0Rs':
            textarea.insert(END, f'\nDrink Tax\t\t\t\t{drinktaxEntry.get()}')
        textarea.insert(END, f'\n\nTotal Bill\t\t\t\t{totalbill}')
        textarea.insert(END, '\n-------------------------------------------------------')
        save_bill()




def total():
    global soapprice,hairsprayprice,hairgelprice,facewashprice,facecreamprice,bodylotionprice
    global riceprice,daalprice,oilprice,sugarprice,wheatprice,teaprice
    global maazaprice,frootiprice,dewprice,pepsiprice,spriteprice,cococolaprice
    global totalbill
    #cosmericprice
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax) + ' Rs')


    #grocery price calculation
    riceprice=int(riceEntry.get())*30
    oilprice=int(oilEntry.get())*100
    daalprice = int(daalEntry.get())*120
    wheatprice=int(wheatEntry.get())*50
    sugarprice=int(sugarEntry.get())*140
    teaprice=int(teaEntry.get())*80

    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax = totalgroceryprice * 0.5
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + ' Rs')

    #drink price calculation
    maazaprice=int(maazaEntry.get())*50
    frootiprice=int(frootiEntry.get())*20
    dewprice=int(dewEntry.get())*30
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spriteEntry.get())*45
    cococolaprice=int(cococolaEntry.get())*90

    totaldrinkprice=maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cococolaprice
    drinkpriceEntry.delete(0,END)
    drinkpriceEntry.insert(0,f'{totaldrinkprice} Rs')
    drinktax=totaldrinkprice*0.08
    drinktaxEntry.delete(0, END)
    drinktaxEntry.insert(0,str(drinktax) + ' Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinkprice+cosmetictax+grocerytax+drinktax









#GUI part

root= Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold')
                     ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_detail_frame=LabelFrame(root,text='Customer Details',font=('times new roman', 15, 'bold')
                                 ,fg='gold',bd=12,relief=GROOVE,bg='gray20')
customer_detail_frame.pack(fill=X)

nameLabel=Label(customer_detail_frame,text='Name',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_detail_frame,font=('times new roman', 15, 'bold'),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_detail_frame,text='Phone Number',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_detail_frame,font=('times new roman', 15, 'bold'),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_detail_frame,text='Bill Number',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_detail_frame,font=('times new roman', 15, 'bold'),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_detail_frame,text='SEARCH',
                    font=('arial',15,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)


productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman', 15, 'bold'),fg='gold'
                          ,bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)


hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)


hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)


bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)


groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman', 15, 'bold'),fg='gold'
                          ,bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)


oilLabel=Label(groceryFrame,text='Oil',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)



wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)


sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)


teaLabel=Label(groceryFrame,text='Tea',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)


drinkFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman', 15, 'bold'),fg='gold'
                          ,bd=8,relief=GROOVE,bg='gray20')
drinkFrame.grid(row=0,column=2)

maazaLabel=Label(drinkFrame,text='Maaza',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(drinkFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(drinkFrame,text='Pepsi',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(drinkFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)


spriteLabel=Label(drinkFrame,text='Sprite',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinkFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(drinkFrame,text='Dew',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(drinkFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(drinkFrame,text='Frooti',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinkFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLabel=Label(drinkFrame,text='Coca Cola',font=('times new roman', 15, 'bold'),bg='gray20'
                ,fg='white')
cococolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cococolaEntry=Entry(drinkFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)


billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman', 15, 'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman', 15, 'bold'),fg='gold'
                          ,bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman', 14, 'bold'),bg='gray20'
                ,fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman', 14, 'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)


grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman', 14, 'bold'),bg='gray20'
                ,fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman', 14, 'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkpriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman', 14, 'bold'),bg='gray20'
                ,fg='white')
drinkpriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkpriceEntry=Entry(billmenuFrame,font=('times new roman', 14, 'bold'),width=10,bd=5)
drinkpriceEntry.grid(row=2,column=1,pady=6,padx=10)


cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman', 14, 'bold'),bg='gray20'
                ,fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman', 14, 'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)


grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman', 14, 'bold'),bg='gray20'
                ,fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman', 14, 'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinktaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman', 14, 'bold'),bg='gray20'
                ,fg='white')
drinktaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinktaxEntry=Entry(billmenuFrame,font=('times new roman', 14, 'bold'),width=10,bd=5)
drinktaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)


billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=5)


printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=5)

















root.mainloop()
