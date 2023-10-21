from datetime import date
import csv, datetime, os.path, re
from termcolor import *
import colorama
colorama.init()




#create sales record file name every first day of the month yyyy-mm-1S.csv
def dateFileNameSales():
    current_date = date.today()
    first_day_of_month = date(current_date.year, current_date.month, 1)
    ext = "Sales.csv"
    return f"{str(first_day_of_month) + ext}"

#create sales record file name every first day of the month yyyy-mm-1S.csv
def dateFileNameStock():
    current_date = date.today()
    first_day_of_month = date(current_date.year, current_date.month, 1)
    ext = "Stock.csv"
    return f"{str(first_day_of_month) + ext}"

    

class Admin:
    def __init__(self, admin_username, admin_password):                  
        self.admin_username = admin_username
        self.admin_password = admin_password

    def __str__(self):
        return f"{self.admin_username}, {self.admin_password}"
    
    @property
    def admin_username(self):
        return self._admin_username

    @admin_username.setter
    def admin_username(self, admin_username):
        if not admin_username:
            raise ValueError("You're not an Admin!")
        self._admin_username = admin_username

    @property
    def admin_password(self):
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        if not admin_password:
            raise ValueError("You're not an Admin!") 
        self._admin_password = admin_password
    
    @classmethod
    def admin_signin_credentials(cls):
        try:
            admin_username = input("Username: ")
            admin_password = input("Password: ")        
            return cls(admin_username, admin_password)           
        except:
            cprint("You're not an Admin!", "red")


    @classmethod
    def admin_signin_credentials_to_signup(cls):       
        try:
            admin_username = input("Old Username: ")
            admin_password = input("Old Password: ")        
            return cls(admin_username, admin_password)           
        except:
            cprint("You're not an Admin!", "red")


    @classmethod
    def admin_signup_credentials(cls):
        try:
            admin_username = input("E-mail: ")
            admin_password = input("New Password: ")        
            return cls(admin_username, admin_password)           
        except:
            cprint("You're not an Admin!", "red")

    @classmethod
    def user_authentication(cls):
        cprint("SignIn", "yellow")
        try:
            email = input("Forgot password? Enter e-mail: ")
        except:
            pass


        credentials = []
        try:
            with open("admin-credentials.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    credentials.append(row)
        except:
            pass 

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')        
        for cred in credentials: 
            admin_username = cred["username"]  
            admin_password = cred["password"]
        if re.fullmatch(regex, email) and email == admin_username:
            print("Your password: ", admin_password)                        
        elif not re.fullmatch(regex, email):
            cprint("Invalid email!", "red")
            admin_credentials = Admin.admin_signin_credentials()               
            try:                     
                if admin_credentials.admin_username == cred["username"] and admin_credentials.admin_password == cred["password"]:                                    
                    return cls(admin_username, admin_password)           
            except:
                pass
        


    @classmethod
    def user_authentication_signup(cls):
        cprint("SignUp", "yellow")
        credentials = []
        try:
            with open("admin-credentials.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    credentials.append(row)
        except:
            pass        
        admin_credentials = Admin.admin_signin_credentials_to_signup()
        for cred in credentials: 
            admin_username = cred["username"]  
            admin_password = cred["password"] 
        if admin_credentials.admin_username != cred["username"] or admin_credentials.admin_password != cred["password"]:
            pass                                
        elif admin_credentials.admin_username == cred["username"] and admin_credentials.admin_password == cred["password"]:                                    
            return cls(admin_username, admin_password)
        

    @classmethod
    def create_admin_signin_credentials(cls, default_username, default_password):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')     
        if default_username and default_password:
            try:
                admin_credentials = Admin.admin_signup_credentials()  
                if re.fullmatch(regex, admin_credentials.admin_username):   
                    with open("admin-credentials.csv", "a") as file:
                        fieldnames = ["username", "password"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        #If file does not exist create header.              
                        if file.tell() == 0:
                            writer.writeheader()
                        writer.writerow({"username": admin_credentials.admin_username, "password": admin_credentials.admin_password})    
            except:
                cprint("SignUp unsuccessful! Check the email your entered.", "red")

    



# temp file to be deleted at the conclusion of every sale
def temp_file():
    tempfile_ext = ".csv"
    return f"{'tempfile_name' + tempfile_ext}"


    
"""
RETURN TOTAL QUANTITY OF EACH NAMED PRODUCT STOCKED IN STOCK FILE

Notee: This function does not calculate quantity of product with batch_no it uses the name of the product. For now am using batch_no that i assigned to identify products. But the final product will use the bar code number on the product to identify product. 

So what this function does is that it loops through all stock files,
the file that contains the batch_no becomes the active file. It loops through the active file, graps all products
that have similar name and then calculate their quantity. 

This applies to function that calculates total_quantity_stocked, total_quantity_sold, total_quantity_expired,
and total_quantity_damaged.
"""

def delete_file():
    '''
    To delete a csv file
    first check if file exists
    call remove method to delete the csv file
    '''
    files = temp_file()
    if(os.path.exists(files) and os.path.isfile(files)):
        os.remove(files) 


#Function to calculate quantity of product
def get_quantity():
    number_of_product = []
    quantity =0
    quantity += 1
    number_of_product.append(quantity)
    qty = int(number_of_product[-1])
    return qty

def get_real_qty():
    qty_list = []
    with open("tempfile_name.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            qty_list.append(row["qty"])
            return sum(int(list) for list in qty_list)









#STOCK CLASS
class Stock: 
    def __init__(self, batch_no, PRD, QTY, CP, SP):
        self.batch_no = batch_no
        self.PRD = PRD
        self.QTY = QTY
        self.CP = CP
        self.SP = SP
    
    
    def __str__(self):
        return f"{self.batch_no}, {self.PRD}, {self.QTY}, {self.CP}, {self.SP}"
    
    
    @property
    def batchNo(self):
        return self.batch_no
    
    @batchNo.setter
    def batchNo(self, batch_no):
        if not batch_no:
            raise ValueError("Missing batch number!")
        self.batch_no = batch_no
    
    @property
    def prodName(self):
        return self.PRD

    @prodName.setter
    def prodName(self, PRD):
        if not PRD:
            raise ValueError("Missing product name!")
        self.PRD = PRD

    @property
    def QTY(self):
        return self._QTY

    @QTY.setter
    def QTY(self, QTY):
        if not QTY:
            raise ValueError("Missing qty!")
        self._QTY = QTY

    @property
    def costPrice(self):
        return self.CP

    @costPrice.setter
    def costPrice(self, CP):
        if not CP:
            raise ValueError("Missing cost price!")
        self.CP = CP

    @property
    def sellPrice(self):
        return self.getStockedProduct  

    @sellPrice.setter
    def sellPrice(self, SP):
        if not SP:
            raise ValueError("Missing sell price!")
        self.SP = SP  
    


    
    @classmethod
    def getStockedProduct(cls):
        while True:
            try:                  
                batch_no = input("|ENTER PRODUCT BATCH NO: ").title()
                if batch_no == "Admin":
                    break
            except BaseException:
                print("Check batch number!")   
                       
            for product in cls.stockList():
                if batch_no == product["batch_no"] or batch_no == "":
                    print(f"Batch number {batch_no} has been used!")
                    break
                    
            else:                
                try:
                    print(f"Batch number {batch_no} is unused!")
                    PRD = input("Product name: ").title()
                    QTY = int(input("Quantity of product: "))
                    CP = int(input("Cost price(#Naira) per product: #"))
                    SP = int(input("Selling price(#Naira) per product: #"))              
                    return cls(batch_no, PRD, QTY, CP, SP)
                except BaseException:
                    pass 


    @classmethod
    def createStockFile(cls):
        stock = cls.getStockedProduct() 
        
        try:
            with open(dateFileNameStock(), "a") as file:
                fieldnames = ["batch_no", "DAT", "PRD", "QTY", "CP", "SP", "TP"]
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                #If file does not exist create header.
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"batch_no": stock.batch_no, "DAT": date.today(), "PRD": stock.PRD, "QTY": stock.QTY, "CP": stock.CP, "SP": stock.SP, "TP": cls.profit(stock.SP, stock.CP, stock.QTY)})
        except BaseException as err:
            print(err)    


    '''
    FUNCTION TO PRINT OUT STOCK RECORD.
    '''
    @classmethod
    def displayStockRecord(cls):
        stocked_product = []
        cost_price = [] 
        sell_price = []
        expected_profit = []
        counter = 0 
        #dateFileName      
        # display list of stock record filename previously created 
        #read_stockrecord_filename()       
        try:           
            with open(dateFileNameStock()) as file:
                reader = csv.DictReader(file)
                for row in reader:                                               
                    stocked_product.append(row)
                    cost_price.append(row["CP"]) 
                    sell_price.append(row["SP"])
                    expected_profit.append(row["TP"])  
        except BaseException as err:
            print(err)
        else:   
            cprint("\nCONTENT OF STOCK RECORD", "green")
            for product in stocked_product: 
                counter += 1                       
                print("|DAT: ", product["DAT"], "|PRD: ", product["PRD"], "|QTY: ", product["QTY"], "|CP: #", product["CP"], "|SP: #", product["SP"], "|TP: #", product["TP"], sep="")  
                    
            cprint("\nSUMMARY OF STOCK RECORD", "green")
            #print("|TOTAL COST PRICE: ", sum(int(list) for list in cost_price))
            #print("|TOTAL SELLING PRICE: ", sum(int(list) for list in sell_price))
            print("|EXPECTED PROFIT: ", sum(int(list) for list in expected_profit)) 
        
   
   
    @classmethod
    def profit(cls, SP, CP, QTY):
        return (SP * QTY) - (CP * QTY)
    

    @classmethod
    def total_quantity_stocked(cls, batch_no):         
        stocked_product = []
        try:
            with open(dateFileNameStock()) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if batch_no == row["batch_no"]:
                        stocked_product.append(row["QTY"])               
        except BaseException as err:
            print(err)
        return sum(int(list) for list in stocked_product)


    #Returns a list of stock record
    @classmethod
    def stockList(cls):               
        try:
            with open(dateFileNameStock()) as file:
                        reader = csv.DictReader(file)
                        return [row for row in reader]
        except BaseException as err:
            print(err) 
    
    
    
    





#SALES CLASS
class Sales:
    def __init__(self):
        ...

    @classmethod        
    def sell_product(cls):    
        #Display sales record, create sales record, create expired product record, display sales summary    
        cprint("|SELL PRODUCT", "green")         
        while True:
            try:
                batch_no = input("|TO SELL ENTER PRODUCT BATCH NO: ")
                if not batch_no:
                    break                                      
            except BaseException as err:
                print(err)  
            else:       
                for product in Stock.stockList():
                    if batch_no == product["batch_no"]:
                        qty = get_quantity()
                        cls.createTempFile(batch_no)
                        cls.createSalesFile(batch_no)                
                        print("|PRD: ", product["PRD"], "|PRICE: #", product["SP"], "|QTY:", qty, sep="")                       
        # display a summary of sales details                                    
        cls.show_sales_summary()                                  
            
            
    
    @classmethod
    def createSalesFile(cls, batch_no):    
        #if product is still in stock and not yet expired a sales file is created to hold details
        trans_date = str(date.today())
        qty = get_quantity()               
        for product in Stock.stockList():   
            if batch_no == product["batch_no"]:    
                try:                
                    with open(dateFileNameSales(), "a") as file:                
                        
                        fieldnames = ["batch_no", "DAT", "PRD", "CP", "SP", "QTY", "TP"]                
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        #If file does not exist create header.            
                        if file.tell() == 0:
                            writer.writeheader() 
                        writer.writerow({"batch_no": product["batch_no"], "DAT": trans_date, "PRD": product["PRD"], "CP": product["CP"], "SP": product["SP"], "QTY": qty, "TP": product["TP"]})                       
                        
                except BaseException as err:
                    print(err)    
        

    
    @classmethod   
    def createTempFile(cls, batch_no):
        trans_date = str(date.today())
        qty = get_quantity()            
        for product in Stock.stockList(): 
            if batch_no == product["batch_no"]:
            # create a temp file to display sales summary        
                try:             
                    with open(temp_file(), "a") as file:                
                        fieldnames = ["batch_no", "DAT", "PRD", "SP", "QTY"]                
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        #If file does not exist create header.            
                        if file.tell() == 0:
                            writer.writeheader() 
                        writer.writerow({"batch_no": product["batch_no"], "DAT": trans_date, "PRD": product["PRD"], "SP": product["SP"], "QTY": qty})                       
                        
                except BaseException as err:
                    print(err)

   
   
    @classmethod
    def show_sales_summary(cls):
        counter = 0    
        price_product = []
        total_qty = []
        product_name = []    
        try:
            with open(temp_file()) as file:
                reader = csv.DictReader(file)
                for row in reader:                                    
                    product_name.append(row)            
                    price_product.append(row["SP"]) 
                    total_qty.append(row["QTY"])
        except (FileNotFoundError, Exception) as err:
            pass
        else:
            cprint("\n|SALES SUMMARY:", "green")
            for prod_name in product_name:
                counter += 1 
                print("|s/n.", counter, "|", prod_name["PRD"], "#",prod_name["SP"], "per item.") 
                        
            print("\n")     
            print("|Total Qty: ", sum(int(list) for list in total_qty))
            print("|Total Amount: #", sum(float(list) for list in price_product), "\n", sep="")        
            #product balance in stock
            cls.product_balance() 

    
    
    @classmethod
    def product_balance(cls):        
        try:
            with open(temp_file()) as file:
                reader = csv.DictReader(file)
                products = [row for row in reader] 
        except BaseException as err:
            print(err)
        else:
            cprint("|PRODUCT BALANCE IN STOCK:", "green") 
            for prod in products:
                batch_no = prod["batch_no"] 
                prod_name = prod["PRD"]             
                if Stock.total_quantity_stocked(batch_no) == cls.total_quantity_sold(batch_no):            
                    print("|",prod_name, "Out of stock!")                    
                else:  
                    print(f"|{prod_name}, {Stock.total_quantity_stocked(batch_no) - cls.total_quantity_sold(batch_no)} remaining in stock, {cls.total_quantity_sold(batch_no)} sold.")  
     
    
    
    
    @classmethod
    def searchForSalesFile(cls):   
        try:
            # year
            yy = input("Please type the year of profit/loss information needed (e.g. 2021): ").strip()        
            # month
            mm = input("Please type the month of profit/loss information needed (e.g. 09): ").strip()
        except BaseException as err:
            print(err)
        else:
            # year and month
            year_and_month = yy + "-" + mm
            # read and collect data from sales-record
            #Sales file is created every first day of the month
            return year_and_month + "-" + str(0) + str(1) + 'Sales.csv'



    # read and collect data from damage product record
    @classmethod
    def display_profit_or_loss_summary(cls):
        price_product = []
        t_qty = []
        total_cost_price = []
        try:
            with open(cls.searchForSalesFile()) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    price_product.append(row["sell_price"])
                    t_qty.append(row["qty"])
                    total_cost_price.append(row["cost_price"])
                    total_quantity_sold = sum(int(list) for list in t_qty)
                    total_profit = sum(float(list) for list in price_product) - sum(float(list) for list in total_cost_price)
        except BaseException as err:
            print(err)
        else:
            # display profit/ loss
            cprint("\n|PROFIT/LOSS INFORMATION", "green")
            print("|TOTAL AMOUNT SOLD: #", sum(float(list) for list in price_product))
            print("|TOTAL COST PRICE: #", sum(float(list) for list in total_cost_price))
            print("|PROFIT: #", sum(float(list) for list in price_product) - sum(float(list) for list in total_cost_price))
            print("|TOTAL QUANTITY OF PRODUCT SOLD: ", total_quantity_sold)
            print("|TOTAL AMOUNT OF PRODUCT SOLD: #", sum(float(list) for list in price_product))
            print("|EXPECTED PROFIT: #",total_profit)



    # display sales summary
    @classmethod
    def display_sales_summary(cls):                
        total_sales_quantity = []
        total_total_amount = []
        try:
            with open(cls.searchForSalesFile()) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total_sales_quantity.append(row["qty"])
                    total_total_amount.append(row["sell_price"])
        except BaseException as err:
            print(err)
        else:
            #dispay sales summary
            cprint("\nSUMMARY OF SALES", "green")
            print("|QUANTITY OF PRODUCT SOLD: ", end="")
            print(sum(int(list) for list in total_sales_quantity), end="\n")
            print("|TOTAL AMOUNT OF PRODUCT SOLD: #", end="")
            print(sum(float(list) for list in total_total_amount), end="\n")


    @classmethod
    def summary(cls):
        # menu
        while True:
            try:
                menu = input("\n|CHOOSE MENU\n|Sales, Profit\n|MENU: ").title().strip()
                if menu == "Admin":
                    break
            except BaseException as err:
                print(err)
            else:
                menu_list = ["Sales", "Profit"]
                if menu in menu_list:
                    match menu:
                        case "Sales":
                            cls.display_sales_summary()
                        case "Profit":
                            cls.display_profit_or_loss_summary()
                        case "_":
                            print("Incorrect Input")


    @classmethod
    def total_quantity_sold(cls, batch_no):
        sold_product = []         
        try:
            with open(dateFileNameSales()) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if batch_no == row["batch_no"]:
                        sold_product.append(row["QTY"])                        
        except BaseException as err:
            print(err)
        return sum(int(list) for list in sold_product)




    
                                                

def main():
#Sales.sell_product()
#Sales.createTempFile(121212)
#Sales.createSalesFile(121212)
#Sales.show_sales_summary()
#print(Sales.stockList())
    
    stock = Stock.getStockedProduct()
    print(stock)
    
                
                

    
    
if __name__=="__main__":
    main()
    







