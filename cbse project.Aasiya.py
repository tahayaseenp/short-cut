import mysql.connector as sql , random , datetime as dt
import mysql.connector as db
con=sql.connect(host='localhost',user='root',password='#aasiya!',database='EBS')
if con.is_connected():
    print("successfully connected")
else:
    print('error')
c='YES' or "yes" or 'Yes'
V='YES' or "yes" or 'Yes'
cursor=con.cursor() 
while c=='YES' or "yes" or 'Yes':
    print('--------WELCOME TO ELECTRICITY BILLING SYSTEM !--------')
    print(dt.datetime.now())
    print('1.NEW USER')
    print('2.EXISTING USER')
    print('3.EXIT')
    choice1=int(input('ENTER YOUR CHOICE:'))
    if choice1==1:
        user_no=input("Enter your user number :")
        user_name=input("Enter your user name :")
        password=input("Enter your password:")
        confirm_password=input("Confirm your password:")
        if password==confirm_password:
            info1="insert into sign_in values('{}','{}','{}','{}')".format(user_no,user_name,password,confirm_password)
            cursor.execute(info1)
            con.commit()
            c=input("Do you want to continue?(yes or no)")
        else:
            print('your confirm password is incorrect')
            print('Try again')
            c=input("do you want to try again?(yes or no)")
    elif choice1==2:
        user_no=input('Enter your user_no:')
        password=input('Enter your password:')
        info2="select * from sign_in where user_no='{}' and password='{}'".format(user_no,password)
        cursor.execute(info2)
        data=cursor.fetchall()
        while V=='YES' or "yes" or 'Yes':
            if any (data):
                print('----------WELCOME TO ELECTRICITY BILLING SYSTEM----------')
                print("1.ACCOUNT SETTINGS")
                print("2.TRANSACTION")
                print("3.VIEW CUSTOMER DETAILS")
                print("4.GRAPHICAL REPRESENTATION")
                print('5.EXIT')
                choice=int(input('ENTER YOUR CHOICE:'))
                if choice==1:
                    print('1.NEW CUSTOMER')
                    print('2.DELETE EXISTING ACCOUNT')
                    ch=int(input('ENTER YOUR CHOICE:'))
                    while True:
                        
                        if ch==1:
                            accountno(print("your account no is : 644-283-753-1"))
                            boxid=input("Enter your meter box ID :")
                            bankname=input('Enter your BANK NAME :')
                            bankbranch=input('Enter your BANK BRANCH :')
                            linked_name=input('Enter your linked name :')
                            address=input('Enter your permanent address :')
                            areacode=int(input('Enter your area PIN CODE  :'))
                            phone_no=int(input('Enter your PHONE NUMBER  :'))
                            email=input('Enter your valid email address :')
                            info3="insert into acc_details values({},{},{},{},{},{},{},{},{})".format(accountno,boxid,bankname,bankbranch,linked_name,address,areacode,phone_no,email,boxid)
                            cursor.execute(info3)
                            con.commit()
                            V=input("do you want to continue?(yes or no)")
                            if V=='yes':
                                pass
                            else:
                                break
                        elif ch==2:
                            acc=input("ENTER YOUR ACCOUNT NUMBER:")
                            use=input("ENTER YOUR USERNAME:")
                            info6=cursor.execute("delete from transaction where accountno='{}'".format(acc))
                            info7=cursor.execute("delete from acc_details where accountno='{}'".format(acc))
                            info8=cursor.execute("delete from sign_in where username='{}'".format(use))
                            cursor.execute(info6)
                            cursor.execute(info7)
                            cursor.execute(info8)
                            con.commit()
                            print("YOUR ACCOUNT IS SUCCESSFULLY DELETED")
                            V=input("do you want to continue?(yes or no)")
                            if V=='yes':
                                continue
                            else:
                                break
                 
                elif choice==2:
                    bank_acc_no=int(input('Enter your account number :'))
                    info10="select * from transaction where bank_acc_no={}".format(bank_acc_no)
                    cursor.execute(info10)
                    data1=cursor.fetchall()
                    for row in data1:
                        unit=random.randint(0,101)
                        print('Dear customer, you have used ',unit,'units of electricity.')
                        print('One unit of current is AED 1')
                        amount=1*unit
                        today=dt.date.today()
                        deadline=dt.date(2022/6/30)
                        if deadline<today:
                            fine=(today-deadline)+2
                            totamt=amount+fine
                            print('you have delayed for ',today-deadline,'days.The fine per day is AED 2.')
                            GST=(10/100)*totamt
                            totalamt=totamt+GST
                            print('kindly pay AED ',totalamt,' including GST')
                            p=input("Please Enter YES to transact")
                            if p=="YES"or 'Yes'or'yes':
                                print("Transaction successful")
                                print("You have paid the bill")
                            else:
                                print('Transaction incomplete/error')
                        else:
                            totamt=0
                            GST=(15/100)*amount
                            totalamt=amount+GST
                            print('kindly pay ',totalamt,'AED including GST')
                            p=input("Please Enter YES to transact")
                            if p=="YES":
                                print("Transaction successful")
                                print("You have paid the bill")
                            else:
                                print('you have to pay the bill soon')
                        info3="insert into Transaction values({},{},'{}',{},{},{},'{}')".format(bank_acc_no,unit,day,totamt,GST,totalamt,p)
                        cursor.execute(info3)
                        con.commit()
                        V=input("do you want to continue?(yes or no)")
                        if V=='yes':
                            continue
                        else:
                            break
                elif choice==3:
            
                    accountno=int(input('Enter your account number :'))
                    info4="select * from acc_details where accountno=" + str(accountno)
                    cursor.execute(info4)
                    data1=cursor.fetchall()
                    for row in data1:
                        print(" Account Number: ", row[0])
                        print("bankname:",row[1])
                        print("bankbranch:",row[2])
                        print("Linked name:",row[3])
                        print("Your meter device ID=",row[8])
                        print("Residential address:",row[4])
                        print("area code:",row[5])
                        print("phone number:",row[6])
                        print("email:",row[7])
                        info5="select * from Transaction where accountno=" + str(accountno)
                        cursor.execute(info5)
                        data2=cursor.fetchall()
                    for row in data2:
                
                        print(" Unit : ",row[1])
                        print(" Paid on:",row[2])
                        print("Amount to be paid without GST:",row[3])
                        print("GST=",row[4])
                        print("Amount to be paid including GST:",row[5])
                    V=input("do you want to continue?(yes or no)")
                    if V=='yes':
                        continue
                    else:
                        break
                elif choice==4:
                    info9="select accountno,totalamt from Transaction"
                    cursor.execute(info9)
                    L1,L2,=[],[]
                    for i in cursor.fetchall():
                        L1.append(i[0])
                        L2.append(i[1])
                    dt.plot(L1,L2)
                    dt.title("GRAPH")
                    dt.show()
                    V=input("do you want to continue?(yes or no)")
                    if V=='yes':
                        continue
                    else:
                        break
                elif choice==5:
                    print( "THANK  YOU FOR VISITING!")
                    break
                    
                else:
                    print('username / password is incorrect')
                    break
                c=input("do you want to try again?(yes or no)")
    
        else:
            print("THANK  YOU FOR VISITING!")
            V='no'
        
    elif choice1==3:
        print("THANK  YOU FOR VISITING!")
        c='no'
        break        
    else:
        print("invalid choice")
        c=input("do you want to try again?(yes or no)")
else:
    print("THANK YOU VISIT AGAIN!")
 
