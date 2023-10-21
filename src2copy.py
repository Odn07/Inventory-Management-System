from mod1 import *

cprint("\n|INVENTRY MANAGEMENT SYSTEM\n", "green")  
#Display sales record, create sales record, create expired product record, display sales summary
while True:
    try:
        count = int(input("\nPress 1 to sell, 2 to use menu tab, and zero to logout: "))
        print("\n")
    except BaseException as err:
        pass
    else:
        if count == 1:
            Sales.sell_product()
            #delete temporary file after printing the current sales details
            delete_file()
        elif count == 2:
            print("|MENU =>", "|Create Stock", "|View Stock", "|Sales")
            # menu
            while True:
                try:
                    menu = input("|MENU =>: ").title().strip()
                    if menu == "Admin":
                        break        
                except BaseException as err:
                    print(err)
                else:
                    menu_list = ["Create Stock", "View Stock", "View Sales"]
                    if menu in menu_list:
                        match menu:    
                            case "Create Stock":       
                                #CREATE STOCK FILE
                                Stock.createStockFile()
                            case "View Stock":              
                                #READ STOCK FILE
                                Stock.displayStockRecord()
                            case "Sales":
                                Sales.summary()
                            case "_":
                                pass

        elif count == 0:
            break   

