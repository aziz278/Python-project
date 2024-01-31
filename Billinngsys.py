from tkinter import *
#functionality part
def total():
    soapprice = int(bathsoapEntry.get()) * 20
    facecreamprice = int(facecreamEntry.get()) * 20
    facewashprice = int(facewashEntry.get()) * 20
    hairsprayprice = int(hairsprayEntry.get()) * 20
    hairgelprice = int(hairgelEntry.get()) * 20

    totalcosmeticprice = soapprice + facewashprice + facecreamprice + hairgelprice + hairsprayprice
    cosmeticpriceEntry.insert(0,totalcosmeticprice)
#grocery price calculation
# Function to calculate total for grocery
def total_grocery():
    rice_price = int(riceEntry.get()) * 30
    daal_price = int(daalEntry.get()) * 100
    oil_price = int(oilEntry.get()) * 120
    sugar_price = int(sugarEntry.get()) * 50
    tea_price = int(teaEntry.get()) * 140
    wheat_price = int(wheatEntry.get()) * 80

    total_grocery_price = rice_price + daal_price + sugar_price + tea_price + wheat_price
    grocerypriceEntry.delete(0, END)  # Clear the entry before inserting new value
    grocerypriceEntry.insert(0, total_grocery_price)
#GUI Part
root = Tk()
root.title('Retail Billing System')
root.geometry('1278x685')

headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold'), bg='gray20', fg='gold', bd=12, relief=RIDGE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), bg='gold', bd=8, relief=GROOVE)
customer_details_frame.pack()

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='gray20',relief=GROOVE, fg='white')
nameLabel.grid(row=0, column=0, padx=23, pady=2)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx= 8)

# Removed duplicated "nameLabel" and corrected typo in "whidth" to "width"

phoneLabel = Label(customer_details_frame, text='Phone', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)


billLabel = Label(customer_details_frame, text='Bill', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
billLabel.grid(row=0, column=4, padx=20, pady=2)

billEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billEntry.grid(row=0, column=5, padx=8)

searchButton=Button(customer_details_frame,text='SEARCH', font=('ariel',12,'bold'),bd=7)
searchButton.grid(row=0, column=6,padx=10)

productsFrame = Frame(root)
productsFrame.pack(pady=10)

cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0, column=0,pady=9)

bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
bathsoapLabel.grid(row=0, column=0,pady=9,padx=10)

bathsoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)
#another one product
facecreamLabel = Label(cosmeticsFrame, text='Face cream', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facecreamLabel.grid(row=1, column=0,pady=9,padx=10)


facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
facecreamEntry.grid(row=1, column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

#another one product
facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facewashLabel.grid(row=2, column=0,pady=9,padx=10)

facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
facewashEntry.grid(row=2, column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

#another one product
hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
hairsprayLabel.grid(row=3, column=0,pady=9,padx=10)

hairsprayEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

#another one product
hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
hairgelLabel.grid(row=4, column=0,pady=9,padx=10)

hairgelEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
hairgelEntry.grid(row=4, column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

#another one product
bodylotionsLabel = Label(cosmeticsFrame, text='Body Lotions', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
bodylotionsLabel.grid(row=5, column=0,pady=9,padx=10)

bodylotionsEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
bodylotionsEntry.grid(row=5, column=1,pady=9,padx=10)
bodylotionsEntry.insert(0,0)



#product 02222///////////////////
groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 15, 'bold'), fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0, column=1,pady=9)


riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
riceLabel.grid(row=0, column=0,pady=9,padx=10)

riceEntry = Entry(groceryFrame, font=('times new roman', 15), width=10, bd=5)
riceEntry.grid(row=0, column=1,pady=9,padx=10)
riceEntry.insert(0,0)
#another one product
oilFrame = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
oilFrame.grid(row=1, column=0,pady=9,padx=10)

oilEntry = Entry(groceryFrame, font=('times new roman', 15), width=10, bd=5)
oilEntry.grid(row=1, column=1,pady=9,padx=10)
oilEntry.insert(0,0)
#another one product
daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
daalLabel.grid(row=2, column=0,pady=9,padx=10)

daalEntry = Entry(groceryFrame, font=('times new roman', 15), width=10, bd=5)
daalEntry.grid(row=2, column=1,pady=9,padx=10)
daalEntry.insert(0,0)
#another one product
wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
wheatLabel.grid(row=3, column=0,pady=9,padx=10)

wheatEntry = Entry(groceryFrame, font=('times new roman', 15), width=10, bd=5)
wheatEntry.grid(row=3, column=1,pady=9,padx=10)
wheatEntry.insert(0,0)
#another one product
sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
sugarLabel.grid(row=4, column=0,pady=9,padx=10)

sugarEntry = Entry(groceryFrame, font=('times new roman', 15), width=10, bd=5)
sugarEntry.grid(row=4, column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

#another one product
teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
teaLabel.grid(row=5, column=0,pady=9,padx=10)

teaEntry = Entry(groceryFrame, font=('times new roman', 15), width=10, bd=5)
teaEntry.grid(row=5, column=1,pady=9,padx=10)
teaEntry.insert(0,0)
#333333333333333product column = 02//////////////////////
cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0, column=2,pady=9)


bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
bathsoapLabel.grid(row=0, column=0,pady=9,padx=10)

bathsoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1,pady=9,padx=10)

#another one product
facecreamLabel = Label(cosmeticsFrame, text='Face cream', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facecreamLabel.grid(row=1, column=0,pady=9,padx=10)

facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
facecreamEntry.grid(row=1, column=1,pady=9,padx=10)

#another one product
facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facewashLabel.grid(row=2, column=0,pady=9,padx=10)

facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
facewashEntry.grid(row=2, column=1,pady=9,padx=10)

#another one product
hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
hairsprayLabel.grid(row=3, column=0,pady=9,padx=10)

hairsprayEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1,pady=9,padx=10)

#another one product
facecreamLabel = Label(cosmeticsFrame, text='Face cream', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facecreamLabel.grid(row=4, column=0,pady=9,padx=10)

facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
facecreamEntry.grid(row=4, column=1,pady=9,padx=10)

#another one product
facecreamLabel = Label(cosmeticsFrame, text='Face cream', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
facecreamLabel.grid(row=5, column=0,pady=9,padx=10)

facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15), width=10, bd=5)
facecreamEntry.grid(row=5, column=1,pady=9,padx=10)





#Bill area//////////////////////////////////////////////
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'))
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=18, width=55)
textarea.pack()

#///////////////
billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), fg='white',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetics Price', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
cosmeticpriceLabel.grid(row=0, column=0,pady=9,padx=10,sticky='w')

cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 15), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1,pady=9,padx=10)


#Another one for bill menu area///////////////


grocerypriceLabel = Label(billmenuFrame, text='Grocery Price', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=1, column=0,pady=9,padx=10,sticky='w')

grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 15), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1,pady=9,padx=10)


#Another one for bill menu area///////////////


colddrinkpriceLabel = Label(billmenuFrame, text='Cold Drink Price', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
colddrinkpriceLabel.grid(row=2, column=0,pady=9,padx=10,sticky='w')

colddrinkpriceEntry = Entry(billmenuFrame, font=('times new roman', 15), width=10, bd=5)
colddrinkpriceEntry.grid(row=2, column=1,pady=9,padx=10)


 #others side of this taxes
cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic Tax', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
cosmeticpriceLabel.grid(row=0, column=2,pady=9,padx=10,sticky='w')

cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 15), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=3,pady=9,padx=10)


#Another one for bill menu area///////////////


grocerypriceLabel = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=1, column=2,pady=9,padx=10,sticky='w')

grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 15), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=3,pady=9,padx=10)


#Another one for bill menu area///////////////


grocerypriceLabel = Label(billmenuFrame, text='Cold Drink Tax', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=2, column=2,pady=9,padx=10,sticky='w')

grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 15), width=10, bd=5)
grocerypriceEntry.grid(row=2, column=3,pady=9,padx=10)


#last section button creation

buttonFrame=Frame(billmenuFrame, bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='green',fg='white',bd=5,width=8,pady=10, command=total)
totalButton.grid(row=0, column=0,pady=20,padx=5)

#bill button
billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='green',fg='white',bd=5,width=8,pady=10 )
billButton.grid(row=0, column=1,pady=20,padx=5)

#Email button
emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='green',fg='white',bd=5,width=8,pady=10 )
emailButton.grid(row=0, column=2,pady=20,padx=5)

#print button
printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='green',fg='white',bd=5,width=8,pady=10 )
printButton.grid(row=0, column=3,pady=20,padx=5)

#Clear button
clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='green',fg='white',bd=5,width=8,pady=10 )
clearButton.grid(row=0, column=4,pady=20,padx=5)

root.mainloop()