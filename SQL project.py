import mysql.connector as sql
conection=sql.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='project_shoemaker'
    )
if conection.is_connected():
    print("SQL is connected; You may Proceed >>")
else:
    print("Unable to establish connection")
conection.autocommit=True
crsr=conection.cursor()

                                      #Function for manager interface
def manager_login():
                    # (13-20) make all names lowercase
    managerlst=["Amit","Adi"]
    s=[]
    for a in managerlst:
        l=a.lower()
        s.append(l)
    for i in s:
        managerlst.append(i)
                    #(22-30) check name and password for manager
    empt_num_1=0       
    while empt_num_1<1:  
        name=input("Enter Name: ")
        pwd=input("Enter Password: ")      
        if name in managerlst and pwd=='1234':
            print("Type 'MODIFY' to modify values; 'SHOW' to show Customer Table; 'FIND' to find customers or shoe available ")
            empt_num_1=empt_num_1+1
        else:
            print("Name or Password does not match; Try again: ")
def user_signup():
    print("<=================SIGN UP===================>")
    newname=input("ENTER YOUR NAME: ")
    newpwd=input("ENTER A PASSWORD: ")
    def user_login():
        userlst=["Amit","Adi"]
        s=[]
        for a in managerlst:
            l=a.lower()
            s.append(l)
        for i in s:
            managerlst.append(i)
                        #(22-30) check name and password for manager
        empt_num_1=0       
        while empt_num_1<1:  
            name=input("Enter Name: ")
            pwd=input("Enter Password: ")      
            if name in managerlst and pwd=='1234':
                print("Type 'MODIFY' to modify values; 'SHOW' to show Customer Table; 'FIND' to find customers or shoe available ")
                empt_num_1=empt_num_1+1
            else:
                print("Name or Password does not match; Try again: ")
    user_login()    

def input_of_manager():
    empt_num_1=2
    while empt_num_1>1:

        managerinput=input("[|>> ")
                            #(40-43) show the customer table
        if managerinput in ["SHOW","show","Show"]:
            print(crsr.execute("select * from customers;"))
            for d in crsr:
                print(d)

                            #(46-51) add delete or edit values of the table
        elif managerinput in ["MODIFY","modify","Modify"]:
            print("Do you want to add or drop a record")
            modifyinput=input('[|>> ')
                            #add values code
            if modifyinput in ["ADD","add","Add"]:
                print("Input data :")
                fnameinput=input("Enter the First Name [|>> ")
                snameinput=input("Enter the Second Name [|>> ")
                phoneinput=int(input("Enter the Phone No. [|>> "))
                addressinput=input("Enter the Address [|>> ")
                shoe_id_input=int(input("Enter the Shoe Id [|>> "))
                crsr.execute("insert into customers values (' + fnameinput + ',' + snameinput + ',' + phoneinput + ',' + shoe_id_input + ',' + addressinput + ')")             #ERROR
            
            elif modifyinput in ["DROP","drop","Drop"]:
                print("Input data :")
                phoneinput=input("Enter the corresponding Phone No. [|>> ")
                crsr.execute("delete from customers where phone_no= " + Phoneinput + " ")                                                                                       #ERROR

        elif managerinput in ["FIND","find","Find"]:
            What_to_find=input("Find customer or product?")
            if What_to_find in ['Customer','customer','CUSTOMER']:
                
                print("Choose among first name, last name, phone number, address, product number ")
                find_customers_using=input("Find Record using : ")
                
                if find_customers_using=="FIRST NAME":
                    customer_fname=input("Enter the first name of the customer: ")
                    crsr.execute('select First_Name,Second_Name,Phone_No,Shoe_bought,Address from customers where first_name ='+customer_fname)                                      #ERROR
                
                elif find_customers_using=="lAST NAME":
                    customer_lname=input("Enter the last name of the customer: ")
                    crsr.execute('select First_Name,Second_Name,Phone_No,Shoe_bought,Address from customers where first_name ='+customer_lname)                                       #ERROR        
                
                elif find_customers_using=="PHONE NUMBER":
                    pno=input("Enter the phone number of the customer: ")
                    crsr.execute('select First_Name,Second_Name,Phone_No,Shoe_bought,Address from customers where first_name ='+pno)                                       #ERROR
        
                elif find_customers_using=="ADDRESS":
                    adrs=input("Enter the address of the customer: ")
                    crsr.execute('select First_Name,Second_Name,Phone_No,Shoe_bought,Address from customers where first_name ='+adrs)                                       #ERROR
       
                elif find_customers_using=="PRODUCT NUMBER":
                    customer_name=input("Enter the product number of the customer: ")
                    crsr.execute('select First_Name,Second_Name,Phone_No,Shoe_bought,Address from customers where first_name ='+customer_name)                                       #ERROR

            elif What_to_find in ['Product','product','PRODUCT']:
                print("CHOOSE AMONG ID,BRAND,MODEL OR SIZE 1-7")
                find_products_using=input("FIND PRODUCT USING : ")
                
                if find_products_using=="ID":
                    productid=input("ENTER ID: ")
                    crsr.execute('select id,brand,model,Size_1,Size_2,Size_3,Size_4,Size_5,Size_6,Size_7 from products where id ='+productid)                                      #ERROR
                elif find_products_using=="BRAND":
                    brand=input("ENTER ID: ")
                    crsr.execute('select id,brand,model,Size_1,Size_2,Size_3,Size_4,Size_5,Size_6,Size_7 from products where id ='+brand)                                      #ERROR
                elif find_products_using=="MODEL":
                    brand=input("ENTER ID: ")
                    crsr.execute('select id,brand,model,Size_1,Size_2,Size_3,Size_4,Size_5,Size_6,Size_7 from products where id ='+brand)                                      #ERROR
                elif find_products_using=="SIZE":
                    crsr.execute('select id,brand,model,Size_1,Size_2,Size_3,Size_4,Size_5,Size_6,Size_7 from products where id= AVAILABLE')                                      #ERROR



        
        else:
            print ("Invalid Input; Try again")
            empt_num_1=empt_num_1+1





conection.close()  