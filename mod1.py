from datetime import date
import csv, datetime, os.path, re, os, glob, random
from xlsxwriter.workbook import Workbook
    

# temp file to be deleted at the conclusion of every sale
def temp_file():
    return f"{'tempfile_name' + '.csv'}"


    

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
    def __init__(self, PC, PRD, QTY, CP, SP):
        self.PC = PC
        self.PRD = PRD
        self.QTY = QTY
        self.CP = CP
        self.SP = SP
    
    
    def __str__(self):
        return f"{self.PC}, {self.PRD}, {self.QTY}, {self.CP}, {self.SP}"
    
    
    @property
    def PCode(self):
        return self.PC
    
    @PCode.setter
    def PCode(self, PC):
        if not PC:
            raise ValueError("Missing batch number!")
        self.PC = PC
    
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
    def csv_to_excel(cls):        
        for csvfile in glob.glob(os.path.join(".", "*Stock.csv")):
            workbook = Workbook(csvfile[:-4] + '.xlsx')
            worksheet = workbook.add_worksheet()
            with open(csvfile, 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()    

    #create sales record file name every first day of the month yyyy-mm-1S.csv
    @classmethod
    def dateFileNameStock(cls):
        current_date = date.today()
        first_day_of_month = date(current_date.year, current_date.month, 1)
        return f"{str(first_day_of_month) + 'Stock.csv'}"
    
    @classmethod
    def getStockedProduct(cls):
        while True:
            try:                  
                PC = input("|ENTER PRODUCT CODE: ").title()
                if PC == "Admin":
                    break
            except BaseException:
                print("Check Product code!")   
                       
            for product in cls.stockList():
                if PC == product["PC"] or PC == "":
                    print(f"Product code {PC} is used!")
                    break
                    
            else:                
                try:
                    print(f"Product code {PC} is free!")
                    PRD = input("Product name: ").title()
                    QTY = int(input("Quantity of product: "))
                    CP = int(input("Cost price(#Naira) per product: #"))
                    SP = int(input("Selling price(#Naira) per product: #"))              
                    return cls(PC, PRD, QTY, CP, SP)
                except BaseException:
                    pass 


    @classmethod
    def createStockFile(cls):
        #Get product from user
        stock = cls.getStockedProduct()      
        try:
            with open(Stock.csv, "a", newline="") as file:
                fieldnames = ["PC", "DATE", "PRD", "QTY", "CP", "SP", "TP"]
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                #If file does not exist create header.
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"PC": stock.PC, "DATE": date.today(), "PRD": stock.PRD, "QTY": stock.QTY, "CP": stock.CP, "SP": stock.SP, "TP": cls.profit(stock.SP, stock.CP, stock.QTY)})
        except BaseException as err:
            print(err)   
        #convert csv stock file to excel
        cls.csv_to_excel() 


    
   
   
    @classmethod
    def profit(cls, SP, CP, QTY):
        return (SP * QTY) - (CP * QTY)
    

    @classmethod
    def total_quantity_stocked(cls, PC):         
        stocked_product = []
        try:
            with open("Stock.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if PC == row["PC"]:
                        stocked_product.append(row["QTY"])               
        except BaseException as err:
            print(err)
        return sum(int(list) for list in stocked_product)


    #Returns a list of stock record
    @classmethod
    def stockList(cls): 
        stocklist = []             
        try:
            with open("Stock.csv") as file:
                reader = csv.DictReader(file)  
                for row in reader:            
                    stocklist.append(row)              
        except BaseException as err:
            pass 
        try:
            return stocklist
        except BaseException as err:
            pass

    @classmethod
    def codeGenerator(cls):
        n = int(input("No. of PC to generate: "))
        random_list = []
        for i in range(0, n):
            random_list.append(random.randint(100, 1000000))
        for n in random_list:
            print(n)

    
    
    
    





#SALES CLASS
class Sales:
    @classmethod
    def totalQuantitySold(cls, PC):
        now = datetime.datetime.now()
        if now.day == 1:
            salesFileName = Sales.dateFileNameSales()
            #if salesFileName == True:
            #write a code that will store all sales file.
            try:
                with open("fileNames.csv", "a", newline="") as file:
                    fieldnames = ["filenames"]
                    writer = csv.DictWriter(file, fieldnames = fieldnames)
                    #If file does not exist create header.
                    if file.tell() == 0:
                        writer.writeheader()        
                    writer.writerow({"filenames": salesFileName})        
            except BaseException as err:
                print(err)

        #write a code that will read and open all sales file stored
        try:
            fileNamesList1 =set()
            with open("fileNames.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    fileNamesList1.add(row["filenames"])
        except BaseException as err:
            print(err)   
        for fileNames in fileNamesList1:    
            quantity = []
            fileNamesList2 = []      
            #open each file, compare data, store quantity of product in
            # each file, and find the sum. 
            try:
                with open(fileNames[0:]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        fileNamesList2.append(row)
            except BaseException as err:
                print(err)
            for fileName in fileNamesList2:
                if PC == fileName["PC"]:
                    quantity.append(fileName["QTY"])
            return sum(int(list) for list in quantity)


    #create sales record file name every first day of the month
    #  yyyy-mm-dd.csv
    @classmethod
    def dateFileNameSales(cls):
        current_date = date.today()
        first_day_of_month = date(current_date.year, current_date.month, 1)        
        return f"{str(first_day_of_month) + 'Sales.csv'}"


    @classmethod    
    def csv_to_excel(cls):  
        try:      
            for csvfile in glob.glob(os.path.join(".", "*Sales.csv")):
                workbook = Workbook(csvfile[:-4] + '.xlsx')
                worksheet = workbook.add_worksheet()
                with open(csvfile, 'rt', encoding='utf8') as f:
                    reader = csv.reader(f)
                    for r, row in enumerate(reader):
                        for c, col in enumerate(row):
                            worksheet.write(r, c, col)
                workbook.close()
        except BaseException as err:
            pass 
        
    @classmethod        
    def sell_product(cls):         
        #Display sales record, create sales record, create expired product record, display sales summary    
        print("|SELL PRODUCT")         
        while True:
            try:
                PC = input("|TO SELL ENTER PRODUCT CODE: ")
                if not PC:
                    break                                      
            except BaseException as err:
                print(err)
            try:
                for product in Stock.stockList():
                    if PC == product["PC"]:
                        qty = get_quantity()
                        cls.createTempFile(PC)
                        cls.createSalesFile(PC) 
                        #converts csv sales file to excel
                        #  spreadsheet
                        cls.csv_to_excel()                      
                        print("|PRD: ", product["PRD"], "|PRICE: #", product["SP"], "|QTY:", qty, sep="")
            except BaseException:
                pass
        # display a summary of sales 
        # detail
        try:
            cls.show_sales_summary()
        except BaseException:
            pass
                                      
            
            
    
    @classmethod
    def createSalesFile(cls, PC):                 
        #if product is still in stock and not yet expired a sales file is created to hold details
        trans_date = str(date.today())
        qty = get_quantity()
        for product in Stock.stockList(): 
            if PC == product["PC"]:            
                try:                
                    with open(cls.dateFileNameSales(), "a", newline="") as file:                
                        
                        fieldnames = ["PC", "DATE", "PRD", "SP", "QTY"]                
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        #If file does not exist create header.            
                        if file.tell() == 0:
                            writer.writeheader() 
                        writer.writerow({"PC": product["PC"], "DATE": trans_date, "PRD": product["PRD"], "SP": product["SP"], "QTY": qty})                       
                        
                except BaseException as err:
                    print(err)
                

        
    @classmethod   
    def createTempFile(cls, PC):
        trans_date = str(date.today())
        qty = get_quantity()            
        for product in Stock.stockList(): 
            if PC == product["PC"]:
            # create a temp file to display sales summary        
                try:             
                    with open(temp_file(), "a", newline="") as file:                
                        fieldnames = ["PC", "DATE", "PRD", "SP", "QTY"]                
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        #If file does not exist create header.            
                        if file.tell() == 0:
                            writer.writeheader() 
                        writer.writerow({"PC": product["PC"], "DATE": trans_date, "PRD": product["PRD"], "SP": product["SP"], "QTY": qty})                       
                        
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
        except BaseException as err:
            pass
        else:
            print("\n|SALES SUMMARY:")
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
            print("|PRODUCT BALANCE IN STOCK:") 
            for prod in products:
                PC = prod["PC"] 
                prod_name = prod["PRD"]             
                if Stock.total_quantity_stocked(PC) == cls.totalQuantitySold(PC):            
                    print("|",prod_name, "Out of stock!")                    
                else:  
                    print(f"|{prod_name}, {Stock.total_quantity_stocked(PC) - cls.totalQuantitySold(PC)} remaining in stock, {cls.totalQuantitySold(PC)} sold.")  
     
    
    
    
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



    
    # display sales summary
    @classmethod
    def display_sales_summary(cls):                
        total_sales_quantity = []
        total_total_amount = []
        try:
            with open(cls.searchForSalesFile()) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total_sales_quantity.append(row["QTY"])
                    total_total_amount.append(row["SP"])
        except BaseException as err:
            print(err)
        else:
            #dispay sales summary
            print("\nSUMMARY OF SALES")
            print("|QUANTITY OF PRODUCT SOLD: ", end="")
            print(sum(int(list) for list in total_sales_quantity), end="\n")
            print("|TOTAL AMOUNT OF PRODUCT SOLD: #", end="")
            print(sum(float(list) for list in total_total_amount), end="\n")


   

    
                                                

def main():
    count = 0
Sales.totalQuantitySold("121212")
#Sales.sell_product()
#Sales.createTempFile(121212)
#Sales.createSalesFile(121212)
#Sales.show_sales_summary()
#print(Sales.stockList())
    
              

    
    
if __name__=="__main__":
    main()
    







