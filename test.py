import datetime

import psycopg2

database = "rockblock_integration"
user = 'postgres'
password = 'postgres'
host = '127.0.0.1'
port = 5432


def delete_data(hour: int):
    # establishing the connection
    conn = psycopg2.connect(
        database=database, user=user, password=password, host=host, port=port
    )
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Executing an MYSQL function using the execute() method
    sql = f"DELETE FROM integration WHERE creation_date<= %s"
    try:
        cursor.execute(sql, (datetime.datetime.now() - datetime.timedelta(hours=hour),))
        conn.commit()
        print("Deleted Older Data from database")

    except:
        conn.rollback()
        print("Cann't delete older data")
    # Closing the connection
    conn.close()


delete_data(hour=10)
