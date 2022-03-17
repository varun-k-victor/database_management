import database

def main():
    connection=database.connect()
    database.field(connection)
    while 1:
        print("1. add record")
        print("2. retrieve record by id")
        print("3. delete record by id")
        print("4. exit")
        option=int(input("select option:"))
        if option==1:
            database.value(connection)
        elif option==2:
            database.retrieve(connection)
        elif option==3:
            database.delete(connection)
        elif option==4:
            quit()
        print("****************************")
if __name__=="__main__":
    main()
    