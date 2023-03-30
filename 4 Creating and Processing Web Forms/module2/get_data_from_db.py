import psycopg2

def select_from_students_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="pass",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="flask_sem4_db",
                                    options="-c search_path=sy_mp")
                
        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from students"

        cursor.execute(postgreSQL_select_Query)

        print("Selecting rows from students1 table using cursor.fetchall")

        students_records = cursor.fetchall()

        return students_records

    except (Exception, psycopg2.Error) as error:
        return "Error while fetching data from PostgreSQL"+ error

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")