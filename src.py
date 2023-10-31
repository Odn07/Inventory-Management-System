import mod1

print("\n|INVENTRY MANAGEMENT SYSTEM\n")  
#Display sales record, create sales record, create expired product record, display sales summary
while True:
    try:
        count = int(input("\nPress 1 to sell, 2 to use menu tab, and zero to logout: "))
        print("\n")
    except BaseException as err:
        pass
    if count == 1:
        mod1.Sales.sell_product()
        #delete temporary file after printing the current sales details
        mod1.delete_file()
    elif count == 2:
        print("\n|MENU =>", "|Pcode", "|Stock", "|Sales")
        # menu
        while True:
            try:
                menu = input("\n|MENU =>: ").title().strip()
                if menu == "Admin":
                    break        
            except BaseException as err:
                print(err)
            menu_list = ["Pcode", "Stock", "Sales"]
            if menu in menu_list:
                match menu:
                    case "Pcode":
                        mod1.Stock.codeGenerator()    
                    case "Stock":       
                        #CREATE STOCK FILE
                        mod1.Stock.createStockFile()
                    case "Sales":
                        #DISPLAY A SUMMARY OF SALES DATA
                        mod1.Sales.display_sales_summary()
                    case _:
                        pass

    elif count == 0:
        break   

