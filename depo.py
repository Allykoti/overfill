from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk

#FUNCTION DEFINITION FOR TAKING VALUES
def insert():
    Loading_ID=e_Loading_ID.get()
    C1=e_C1.get()
    C2=e_C2.get()
    C3=e_C3.get()
    C4=e_C4.get()
    C5=e_C5.get()
    C6=e_C6.get()
    ChartNo=e_ChartNo.get()
    Expire_day=e_Expire_day.get()
    Expire_month=e_Expire_month.get()
    Expire_year=e_Expire_year.get()
    truck_ID=e_truck_ID.get()
    truck_No=e_truck_No.get()
    truck_company=e_truck_company.get()
    if(truck_ID==" " or truck_No==" "or truck_company==" "or C1==" " or C2==" "or C3==" "or C4==" "or C5==" " or C6==" " or ChartNo==" " or Expire_day==" " or Expire_month==" " or Expire_year==" " ):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="allykoti9898#",database="hassan") 
        cursor=con.cursor() 
        cursor.execute("insert into compartmentvolume values('"+Loading_ID+"','"+C1+"','"+C2+"','"+C3+"','"+C4+"','"+C5+"','"+C6+"')")
        cursor.execute("insert into calibrationchart values('"+ChartNo+"','"+Loading_ID+"','"+Expire_day+"','"+Expire_month+"','"+Expire_year+"')")
        cursor.execute("insert into truckinfo values('"+truck_ID+"','"+truck_No+"','"+truck_company+"','"+ChartNo+"')")
        cursor.execute("commit")
    #Delete section after inserting
        e_truck_ID.delete(0,'end')
        e_truck_No.delete(0,'end')
        e_truck_company.delete(0,'end')
        e_Loading_ID.delete(0,'end')
        e_C1.delete(0,'end')
        e_C2.delete(0,'end')
        e_C3.delete(0,'end')
        e_C4.delete(0,'end')
        e_C5.delete(0,'end')
        e_C6.delete(0,'end')
        e_ChartNo.delete(0,'end')
        e_Expire_day.delete(0,'end')
        e_Expire_month.delete(0,'end')
        e_Expire_year.delete(0,'end')      
        MessageBox.showinfo("Insert Status","Inserted Successful")
        con.close() 
#retrive function
def retrive():
    truck_ID=e_truck_ID.get()
    if(
    truck_ID == " " or truck_No == " " or truck_company == " " or Loading_ID == "" or C1 == " " or
    C2 == " " or C3 == " " or C4 == " " or C5 == " " or C6 == " " or ChartNo == "" or Expire_day == "" or
    Expire_month == "" or Expire_year == ""
):
       MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
       con = mysql.connect(host="localhost", user="root", password="allykoti9898#", database="hassan")
       cursor = con.cursor()
       query = """
        SELECT *
        FROM truckinfo
        JOIN calibrationchart ON truckinfo.ChartNo = calibrationchart.ChartNo
        JOIN compartmentvolume ON calibrationchart.Loading_ID = compartmentvolume.Loading_ID
        WHERE truckinfo.truck_ID = %s
    """
       truck_ID = int(truck_ID)
       cursor.execute(query, (truck_ID,))
       results = cursor.fetchall()

    if results:
        # Assuming you have separate entry fields for each parameter, adjust the names accordingly
        e_truck_No.insert(0, results[0][1])
        e_truck_company.insert(0, results[0][2])
        e_ChartNo.insert(0, results[0][3])
        e_Loading_ID.insert(0, results[0][5])
        e_Expire_day.insert(0, results[0][6])
        e_Expire_month.insert(0, results[0][7])
        e_Expire_year.insert(0, results[0][8])
        e_C1.insert(0, results[0][10])
        e_C2.insert(0, results[0][11])
        e_C3.insert(0, results[0][12])
        e_C4.insert(0, results[0][13])
        e_C5.insert(0, results[0][14])
        e_C6.insert(0, results[0][15])      
    else:
        MessageBox.showinfo("Insert Status", "Truck ID not found in the database")

    con.commit()  
    con.close()
    MessageBox.showinfo("Insert Status", "Retrieved Successfully")
    
#Function for clearing
def clear():
    e_truck_ID.delete(0,'end')
    e_truck_No.delete(0,'end')
    e_truck_company.delete(0,'end')
    e_Loading_ID.delete(0,'end')
    e_C1.delete(0,'end')
    e_C2.delete(0,'end')
    e_C3.delete(0,'end')
    e_C4.delete(0,'end')
    e_C5.delete(0,'end')
    e_C6.delete(0,'end')
    e_ChartNo.delete(0,'end')
    e_Expire_day.delete(0,'end')
    e_Expire_month.delete(0,'end')
    e_Expire_year.delete(0,'end')      
    MessageBox.showinfo("Insert Status","CLEARED SUCCESSFUL")
#defining a fuction to update data
def update():
    Loading_ID=e_Loading_ID.get()
    C1=e_C1.get()
    C2=e_C2.get()
    C3=e_C3.get()
    C4=e_C4.get()
    C5=e_C5.get()
    C6=e_C6.get()
    ChartNo=e_ChartNo.get()
    Expire_day=e_Expire_day.get()
    Expire_month=e_Expire_month.get()
    Expire_year=e_Expire_year.get()
    truck_ID=e_truck_ID.get()
    truck_No=e_truck_No.get()
    truck_company=e_truck_company.get()
    if(truck_ID==" " or truck_No==" "or truck_company==" "or C1==" " or C2==" "or C3==" "or C4==" "or C5==" " or C6==" " or ChartNo==" " or Expire_day==" " or Expire_month==" " or Expire_year==" " ):
        MessageBox.showinfo("Status","No Entries")
    else:
        con=mysql.connect(host="localhost",user="root",password="allykoti9898#",database="hassan") 
        cursor=con.cursor() 
        cursor.execute("update compartmentvolume set C1='"+C1+"',C2='"+C2+"',C3='"+C3+"',C4='"+C4+"',C5='"+C5+"',C6='"+C6+"'")
        cursor.execute("update calibrationchart set Expire_day='"+Expire_day+"',Expire_month='"+Expire_month+"',Expire_year='"+Expire_year+"'")
        #cursor.execute("update truckinfo set truck_ID='"+truck_ID+"',truck_No='"+truck_No+"',truck_company='"+truck_company+"',ChartNo='"+ChartNo+"'")
        cursor.execute("commit")
    #Delete section after inserting
        e_truck_ID.delete(0,'end')
        e_truck_No.delete(0,'end')
        e_truck_company.delete(0,'end')
        e_Loading_ID.delete(0,'end')
        e_C1.delete(0,'end')
        e_C2.delete(0,'end')
        e_C3.delete(0,'end')
        e_C4.delete(0,'end')
        e_C5.delete(0,'end')
        e_C6.delete(0,'end')
        e_ChartNo.delete(0,'end')
        e_Expire_day.delete(0,'end')
        e_Expire_month.delete(0,'end')
        e_Expire_year.delete(0,'end')      
        MessageBox.showinfo("Status","Updated Successful")
        con.close() 
    
#defining a function for evaluation
def compa():
    C11 = e_C11.get()
    C21 = e_C21.get()
    C31 = e_C31.get()
    C41 = e_C41.get()
    C51 = e_C51.get()
    C61 = e_C61.get()
    pn = e_pn.get()
    if C11 == "" or C21 == "" or C31 == "" or C41 == "" or C51 == "" or C61 == "":
        MessageBox.showinfo("STATUS", "Enter the Order Volume")
    else:
        con = mysql.connect(host="localhost", user="root", password="allykoti9898#", database="hassan")
        cursor = con.cursor()
        query = "SELECT C1, C2, C3, C4, C5, C6 FROM compartmentvolume WHERE Loading_ID = %s"
        cursor.execute(query, (pn,))
        result = cursor.fetchone()
        errors = []
        if result[0] < int(C11):
            errors.append("Compartment C1: Incorrect volume")
        if result[1] < int(C21):
            errors.append("Compartment C2: Incorrect volume")
        if result[2] < int(C31):
            errors.append("Compartment C3: Incorrect volume")
        if result[3] < int(C41):
            errors.append("Compartment C4: Incorrect volume")
        if result[4] < int(C51):
            errors.append("Compartment C5: Incorrect volume")
        if result[5] < int(C61):
            errors.append("Compartment C6: Incorrect volume")

        if len(errors) == 0:
            MessageBox.showinfo("STATUS", "Volume Allocations are correct. You can proceed importing this allocation to loading CARD and Loading to proceed.")
        else:
            error_message = "DANGER: Overfilling Is Going To Happen. Please re-allocate the following compartments:\n\n" + "\n".join(errors)
            MessageBox.showinfo("STATUS", error_message)
        
        cursor.close()
def clear1():
    e_C11.delete(0,'end')
    e_C21.delete(0,'end')
    e_C31.delete(0,'end')
    e_C41.delete(0,'end')
    e_C51.delete(0,'end')
    e_C61.delete(0,'end')
    e_pn.delete(0,'end')      
    MessageBox.showinfo("Status","CLEARED SUCCESSFUL")        
                                         
#DEFINITION OF SYSTEM DASHBOARD
root=Tk()
root.geometry("1500x1500")
root.title("LOADING INFORMATION CHECKING DASHBOARD")

#welcoming information
hd=Label(root,text="WELCOME TO THE LOADING INFORMATION CHECKING SYSTEM",font=('bold',20),bg="grey")
hd.place(x=300,y=10)

#directing the user
dr0=Label(root,text="SECTION: 1",font=('bold',15))
dr0.place(x=250,y=50)
dr01=Label(root,text="SECTION: 2",font=('bold',15))
dr01.place(x=900,y=50)
dr1=Label(root,text="Registred:Enter Truck ID,then GET Button",font=('bold',15),bg="grey")
dr1.place(x=20,y=80)
dr2=Label(root,text="Not Registred:Fill the Information Bellow",font=('bold',15),bg="grey")
dr2.place(x=20,y=110)
dr3=Label(root,text="ENTER:The Order Volume Distribution in Every Compartment",font=('bold',15),bg="grey")
dr3.place(x=700,y=110)
#creating that requirest input values
truck_ID=Label(root,text="ENTER: TruckID",font=('bold',10),bg="red")
truck_ID.place(x=20,y=160)
truck_No=Label(root,text="ENTER: TruckNo",font=('bold',10),bg="orange")
truck_No.place(x=20,y=200)
Loading_ID=Label(root,text="ENTER: Loading_ID",font=('bold',10),bg="orange")
Loading_ID.place(x=20,y=240)
ChartNo=Label(root,text="ENTER: The CalibrationChart No",font=('bold',10),bg="orange")
ChartNo.place(x=20,y=275)
Expire_day=Label(root,text="ENTER:Calibration Chart_day",font=('bold',10),bg="orange")
Expire_day.place(x=20,y=310)
Expire_month=Label(root,text="ENTER:Calibration Chart_month",font=('bold',10),bg="orange")
Expire_month.place(x=20,y=340)
Expire_year=Label(root,text="ENTER:Calibration Chart_year",font=('bold',10),bg="orange")
Expire_year.place(x=20,y=370)
truck_company=Label(root,text="ENTER:Truck's Company name",font=('bold',10),bg="orange")
truck_company.place(x=20,y=400)
C1=Label(root,text="ENTER:Compartment 1 Volume",font=('bold',10),bg="orange")
C1.place(x=20,y=430)
C2=Label(root,text="ENTER:Compartment 2 Volume",font=('bold',10),bg="orange")
C2.place(x=20,y=460)
C3=Label(root,text="ENTER:Compartment 3 Volume",font=('bold',10),bg="orange")
C3.place(x=20,y=490)
C4=Label(root,text="ENTER:Compartment 4 Volume",font=('bold',10),bg="orange")
C4.place(x=20,y=520)
C5=Label(root,text="ENTER:Compartment 5 Volume",font=('bold',10),bg="orange")
C5.place(x=20,y=550)
C6=Label(root,text="ENTER:Compartment 6 Volume",font=('bold',10),bg="orange")
C6.place(x=20,y=580)
#LogMode=Label(root,text="ENTER:Transport_type",font=('bold',10),bg="orange")
#LogMode.place(x=20,y=510)
#SECTION 2
C11=Label(root,text="ENTER:Compartment 1 Volume",font=('bold',15),bg="orange")
C11.place(x=700,y=160)
C21=Label(root,text="ENTER:Compartment 2 Volume",font=('bold',15),bg="orange")
C21.place(x=700,y=210)
C31=Label(root,text="ENTER:Compartment 3 Volume",font=('bold',15),bg="orange")
C31.place(x=700,y=260)
C41=Label(root,text="ENTER:Compartment 4 Volume",font=('bold',15),bg="orange")
C41.place(x=700,y=310)
C51=Label(root,text="ENTER:Compartment 5 Volume",font=('bold',15),bg="orange")
C51.place(x=700,y=360)
C61=Label(root,text="ENTER:Compartment 6 Volume",font=('bold',15),bg="orange")
C61.place(x=700,y=410)
pn=Label(root,text="ENTER:Enter the Loading_ID",font=('bold',15),bg="orange")
pn.place(x=700,y=460)



#creating entry boxex
e_truck_ID=Entry()
e_truck_ID.place(x=310,y=160)
e_truck_No=Entry()
e_truck_No.place(x=310,y=200)
e_Loading_ID=Entry()
e_Loading_ID.place(x=310,y=240)
e_ChartNo=Entry()
e_ChartNo.place(x=310,y=275)
e_Expire_day=ttk.Combobox(root)
e_Expire_day['values']=('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15',
                     '16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
e_Expire_day.place(x=310,y=310)
e_Expire_month=ttk.Combobox(root)
e_Expire_month['values']=('01','02','03','04','05','06',
                      '07','08','09','10','11','12')
e_Expire_month.place(x=310,y=340)
e_Expire_year=ttk.Combobox(root)
e_Expire_year['values']=('2020','2021','2022','2023','2024','2025','2026','2027','2028',
                     '2029','2030','2031','2032','2033','2034','2035','2036','2037','2038',
                     '2039','2040','2041','2042','2043','2044','2045','2046','2047','2048',
                     '2049','2050')
e_Expire_year.place(x=310,y=370)
e_truck_company=Entry()
e_truck_company.place(x=310,y=400)
e_C1=ttk.Combobox(root)
e_C1['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                '5000','5500','6000','6500','7000','7500','8000','8500',
                '9000','9500','10000','10500','11000','11500','12000',
                '12500','13000','13500','14000','14500')
e_C1.place(x=310,y=430)
e_C2=ttk.Combobox(root)
e_C2['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                '5000','5500','6000','6500','7000','7500','8000','8500',
                '9000','9500','10000','10500','11000','11500','12000',
                '12500','13000','13500','14000','14500')
e_C2.place(x=310,y=460)
e_C3=ttk.Combobox(root)
e_C3['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                '5000','5500','6000','6500','7000','7500', '8000','8500',
                '9000','9500','10000','10500','11000','11500','12000',
                '12500','13000','13500','14000','14500')
e_C3.place(x=310,y=490)
e_C4=ttk.Combobox(root)
e_C4['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                '5000','5500','6000','6500','7000','7500','8000','8500',
                '9000','9500','10000','10500','11000','11500','12000',
                '12500','13000','13500','14000','14500')
e_C4.place(x=310,y=520)
e_C5=ttk.Combobox(root)
e_C5['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                '5000','5500','6000','6500','7000','7500','8000','8500',
                '9000','9500','10000','10500','11000','11500','12000',
                '12500','13000','13500','14000','14500')
e_C5.place(x=310,y=550)
e_C6=ttk.Combobox(root)
e_C6['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                '5000','5500','6000','6500','7000','7500','8000','8500',
                '9000','9500','10000','10500','11000','11500','12000',
                '12500','13000','13500','14000','14500')
e_C6.place(x=310,y=580)
#SECTION 2
e_C11=ttk.Combobox(root)
e_C11['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                 '5000','5500','6000','6500','7000','7500','8000','8500',
                 '9000','9500','10000','10500','11000','11500','12000',
                 '12500','13000','13500','14000','14500')
e_C11.place(x=1000,y=160)
e_C21=ttk.Combobox(root)
e_C21['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                 '5000','5500','6000','6500','7000','7500','8000','8500',
                 '9000','9500','10000','10500','11000','11500','12000',
                 '12500','13000','13500','14000','14500')
e_C21.place(x=1000,y=210)
e_C31=ttk.Combobox(root)
e_C31['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                 '5000','5500','6000','6500','7000','7500','8000','8500',
                 '9000','9500','10000','10500','11000','11500','12000',
                 '12500','13000','13500','14000','14500')
e_C31.place(x=1000,y=260)
e_C41=ttk.Combobox(root)
e_C41['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                 '5000','5500','6000','6500','7000','7500','8000','8500',
                 '9000','9500','10000','10500','11000','11500','12000',
                 '12500','13000','13500','14000','14500')
e_C41.place(x=1000,y=310)
e_C51=ttk.Combobox(root)
e_C51['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                 '5000','5500','6000','6500','7000','7500','8000','8500',
                 '9000','9500','10000','10500','11000','11500','12000',
                 '12500','13000','13500','14000','14500')
e_C51.place(x=1000,y=360)
e_C61=ttk.Combobox(root)
e_C61['values']=('0','1000','1500','2000','2500','3000','3500','4000','4500',
                 '5000','5500','6000','6500','7000','7500','8000','8500',
                 '9000','9500','10000','10500','11000','11500','12000',
                 '12500','13000','13500','14000','14500')
e_C61.place(x=1000,y=410)
e_pn=Entry()
e_pn.place(x=1000,y=460)
#Creating  input buttons SECTION 1
insert=Button(root,text="INSERT",font=("italic",12),bg="purple",command=insert)
insert.place(x=20,y=610)
retrive=Button(root,text="RETRIVE",font=("italic",12),bg="green",command=retrive)
retrive.place(x=120,y=610)
update=Button(root,text="UPDATE",font=("italic",12),bg="yellow",command=update)
update.place(x=230,y=610)
clear=Button(root,text="CLEAR",font=("italic",12),bg="white",command=clear)
clear.place(x=330,y=610)
#Creating input buttons SECTION 2
evaluate=Button(root,text="EVALUATE",font=("italic",15),bg="yellow",command=compa)
evaluate.place(x=1200,y=500)
evaluate=Button(root,text="CLEAR",font=("italic",15),bg="green",command=clear1)
evaluate.place(x=1095,y=500)
root.mainloop()