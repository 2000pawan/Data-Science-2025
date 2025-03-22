from pymysql import connect, Error

def create_table():
    try:
        # Create a database connection
        mydb = connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='db'
        )
        mycursor = mydb.cursor()
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Stationery (
                itemno INT(10) PRIMARY KEY,
                item VARCHAR(40) NOT NULL,
                price FLOAT(10, 2) NOT NULL,
                quantity INT(10) NOT NULL
            )
        """)
        mydb.commit()
        print('Table created')
    except Error as e:
        print(f"An error occurred: {e}")

def add_and_display():
    try:
        # Create a database connection
        mydb = connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='db'
        )
        mycursor = mydb.cursor()
        itemno = int(input('Enter item number: '))
        item = input('Enter item name: ')
        price = float(input('Enter price: '))
        quantity = int(input('Enter quantity: '))
        mycursor.execute("""
            INSERT INTO Stationery (itemno, item, price, quantity)
            VALUES (%s, %s, %s, %s)
        """, (itemno, item, price, quantity))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.execute('select * from Stationery')
        result=mycursor.fetchall()
        for i in result:
            print(i)
    except Error as e:
        print(f"An error occurred: {e}")

create_table()
add_and_display()