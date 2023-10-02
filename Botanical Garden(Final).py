print("Welcome to The Botanical Garden!!!!!!!")
print("A beautiful World of Plants")
p=input("Enter your Mysql password :")
d=input("Enter your Database name :")
def table():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=p,database=d)
        mycursor = mydb.cursor()
        q="create table garden(plant_name varchar(30) primary key,lifespan int(5),uses varchar(50),type varchar(20),family varchar(20),natural_habitat varchar(35));"
        mycursor.execute(q)
        print("Table Created")
        v1="insert into garden values('Lemon',50,'good source of vitamin C and improves digestion','Shrub','Rutaceae','tropical and subtropical region');"
        v2="insert into garden values('Palm',150,'used as cooking ingredient and oil','tree','arecaceae','tropical and subtropical region');"
        v3="insert into garden values('Grape',30,'good source of vitamin and high antioxidant','Climber','Vitaceae','subtropical region');"
        v4="insert into garden values('Money Plant',50,'purifies air and other medicinal benefits','creeper','araceae','tropical region');"
        v5="insert into garden values('Pomegranate',15,'medicinal benefits and beneficial nutrients','shrubs','punicaceae','tropical region');"
        v6="insert into garden values('strawberry',6,'high fibre and used as food','creeper','rosaceae','tropical region');"
        v7="insert into garden values('Oak',300,'timber and used as medicine','tree','fogaceae','semi-desert to subtropical region');"
        v8="insert into garden values('mint',10,'improve oral health','herb','lamiceae','tropical region');"
        mycursor.execute(v1)
        mycursor.execute(v2)
        mycursor.execute(v3)
        mycursor.execute(v4)
        mycursor.execute(v5)
        mycursor.execute(v6)
        mycursor.execute(v7)
        mycursor.execute(v8)
        mydb.commit()
        print("Record (s) Added")
        print("Please continue to program")
    except Exception as e:
        print(e)
        
def fetchdata():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=p,database=d)
        mycursor = mydb.cursor()
        mycursor.execute("Select * from garden")
        myrecords = mycursor.fetchall()
        for x in myrecords:
            print(x)
    except:
        print("Unable to fetch data")
    c=input("Do you want to continue or not(Y/N): ")
    if c=='y' or c=='Y':
        menu()
    else:
        print("Exiting")
def deldata():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=p,database=d)
        mycursor = mydb.cursor()
        nam= input("Input the Plant Name to delete the record:")
        qry="DELETE FROM garden where plant_name ='%s';" %(nam,)
        mycursor.execute(qry)
        mydb.commit()
        print(mycursor.rowcount,"Record (s) Deleted")
    except Exception as e:
        print(e)
    c=input("Do you want to continue or not(Y/N): ")
    if c=='y' or c=='Y':
        menu()
    else:
        print("Exiting")
def updatedata():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=p,database=d)
        mycursor = mydb.cursor()
        nm=input("Input the Plant Name for Lifespan to be changed:")
        lfspn=int(input("Input the Lifespan to update:"))
        qry="UPDATE garden set lifespan = %s where plant_name = '%s';"%(lfspn,nm)
        mycursor.execute(qry)
        mydb.commit()
        print(mycursor.rowcount,"Record (s) Updated")
    except Exception as e:
        print(e)
    c=input("Do you want to continue or not(Y/N): ")
    if c=='y' or c=='Y':
        menu()
    else:
        print("Exiting")
def adddata():
    try:
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=p,database=d)
        mycursor = mydb.cursor()
        nam=input("Enter the Plant name to be added :")
        lfspn=int(input("Enter the Lifespan of the plant :"))
        use=input("Enter one use :")
        typ=input("Enter Type of Plant :")
        fam=input("Enter Family of the Plant :")
        nh=input("Enter Natural Habitat of the Plant :")
        upd=(nam,lfspn,use,typ,fam,nh)
        mycursor.execute("INSERT INTO garden values(%s,%s,%s,%s,%s,%s)",upd)
        mydb.commit()
        print(mycursor.rowcount,"Record (s) Added")
    except Exception as e:
        print(e)
    c=input("Do you want to continue or not(Y/N): ")
    if c=='y' or c=='Y':
        menu()
    else:
        print("Exiting")
def graph():
    try:
        import mysql.connector
        import pandas as pd
        import matplotlib.pyplot as plt
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=p,database=d)
        qry="Select plant_name,lifespan from garden;"
        df=pd.read_sql(qry, mydb)
        plt.bar(df['plant_name'],df['lifespan'])
        plt.title("Plants Lifespan(in years)")
        plt.xlabel("Plant Name")
        plt.ylabel("Lifespan(in years)")
        plt.show()
    except Exception as e:
        print(e)
    c=input("Do you want to continue or not(Y/N): ")
    if c=='y' or c=='Y':
        menu()
    else:
        print("Exiting")
def making():
    tab=input("Do you want to Make a table(garden) with data(s),(Y/N) : ")
    if tab=="y" or tab=="Y":
        table()
    elif tab=='n' or tab=="N":
        print("Please continue to program")
    else:
        print("Wrong input")
        making()
making()    
c=input("Do you want to continue or not(Y/N): ")
if c=='Y' or c=='y':
    def menu():
        while True:
            print ("1: Display Plants Record")
            print ("2: Update a Plant Lifespan")
            print ("3: Add a plant Record")
            print ("4: Delete a Plant Record")
            print ("5. Display Graph of Plants vs Lifespan")
            print ("6. Want to Exit")
            ch=int(input("Enter your choice: "))
            if ch== 3:
                adddata()
            elif ch== 2:
                updatedata()
            elif ch== 4:
                deldata()
            elif ch== 1:
                fetchdata()
            elif ch==5:
                graph()
            elif ch== 6:
                print("Exiting")
                break
            else:
                print("Wrong input")
                print("Try again")
                menu()
            break
    menu()
elif c=='N' or c=='n':
    print("Exiting")
else:
    print("Wrong Input")
    print("Please Start the program again")
    print("Exiting")
    print("Thank You")
            
