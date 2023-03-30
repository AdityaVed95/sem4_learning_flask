from flask import Flask
import psycopg2


# When you execute a query using the cursor from that connection, 
# it will search across those schemas mentioned in options 
# i.e., dbo,public in sequence from left to right.

def select_from_students1_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="pass",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="adityaved",
                                    options="-c search_path=sy_mp,public")
        

        # note : 
        # the options parameter is used to specify the schema of the database 
        # that contains the table
        # in the above example : 
        # 1st the sy_mp schema will be searched in and then we will search in 
        # public schema
        
        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from students1"

        cursor.execute(postgreSQL_select_Query)

        print("Selecting rows from students1 table using cursor.fetchall")

        students_records = cursor.fetchall()

        # print("type of students_records - cursor ", type(students_records))
        # print("number of rows ", len(students_records))
        
        # print(students_records)

        return students_records

    except (Exception, psycopg2.Error) as error:
        return "Error while fetching data from PostgreSQL"+ error

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

app = Flask(__name__)

@app.get("/select")
def select_fxn():
    operation_result = select_from_students1_db()
    x = str(type(operation_result))
    y = str(type(operation_result[0]))
    print(x)
    print(y)
    # although we get a list of tuples as a result of select * sql query
    # what is being displayed here is list of lists
    return operation_result


