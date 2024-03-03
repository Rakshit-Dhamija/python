# connecting python and sql
def code():
    c='y'
    while c=='y' or c=='Y':
        print('\t\t\t')
        print('Sql functions:')
        print('1. Add records')
        print('2. Delete records')
        print('3. Display records')
        print('4. Update records')
        print('5. Exit')
        ch=int(input('Enter your choice:'))
        if ch==1:
            add()
        elif ch==2:
            delete()
        elif ch==3:
            fetchdata()
        elif ch==4:
            search()
        elif ch==5:
            print('Exiting....')
            break
    else:
        print('Wrong input')
    c=input('Do you want to continue y/n?')
def fetchdata():
    import mysql.connector as a
    try:
        db=a.connect(host='localhost',user='root',password='root',database='s1')
        cur=db.cursor()
        cur.execute('select * from student')
        result=cur.fetchall()
        for i in result:
            print(i)
    except:
        print('ERROR!!! unable to fetch data')

def add():
    import mysql.connector as a
    db=a.connect(host='localhost',user='root',password='root',database='s1')
    cur=db.cursor()
    name=input('Enter name:')
    sub=input('Enter subject:')
    marks=int(input('Enter Marks:'))
    grade=input('Enter grade:')
    clas=input('Enter class:')
    cur.execute('insert into student values(%s,%s,%s,%s,%s)',(name,sub,marks,grade,clas))
    db.commit()
    print('Record added')


def delete():
    import mysql.connector as a
    db=a.connect(host='localhost',user='root',password='root',database='s1')
    cur=db.cursor()
    sql=("delete from student where Name='Ritu';")
    cur.execute(sql)
    print("RECORD DELETED")
    db.commit()

def update():
    import mysql.connector as a
    db=a.connect(host='localhost',user='root',password='root',database='s1')
    cur=db.cursor()
    q=("Update student set marks=99 where Name='Ritu'")
    cur.execute(q)
    print('record updated')
    db.commit()   


code()







   # print('Chose what do you want to update?')
   # print('1. Name')
   # print('2. Subject')
  #  print('3. Marks')
  #  print('4. Grade')
  #  print('5. Class')
  #  ch=int(input('Enter choice:'))
  #  while True:
#elif ch==2:
 #           update()

 #def search():
#    import mysql.connector as a
 #   try:
  #      db=a.connect(host='localhost',user='root',password='root',database='s1')
   #     cur=db.cursor()
    #    column_name=input('Enter name of column to be searched in:')
     #   item=input('Enter item to be searched')
      #  cur.execute('select * from student where %s = %s',(column_name,'item'))
       # data=cur.fetchall()
        #print(data)
        #for i in data:
         #   print(i)
    #    print('Records Searched')
  #  except:
   #     print('Error in search')
