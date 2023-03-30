from flask import Flask
import psycopg2


def select_specific_tuple_from_students1_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="pass",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="adityaved")
        
        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from students1 where student_id = 200"

        cursor.execute(postgreSQL_select_Query)

        print("Selecting rows from students1 table using cursor.fetchall")

        students_record = cursor.fetchall()

        # print("type of students_records - cursor ", type(students_records))
        # print("number of rows ", len(students_records))
        
        # print(students_records)

        return students_record

    except (Exception, psycopg2.Error) as error:
        return "Error while fetching data from PostgreSQL"+ error

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

app = Flask(__name__)

@app.get("/select_specific")
def select_specific_fxn():
    operation_result = select_specific_tuple_from_students1_db()
    return operation_result


