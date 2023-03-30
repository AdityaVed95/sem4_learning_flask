from flask import Flask
import psycopg2




def update_tuple_of_students1_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="pass",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="adityaved")
        
        cursor = connection.cursor()

        postgreSQL_update_Query = """
    
        update students1
        set city= %s
        where student_id = %s

        """

        cursor.execute(postgreSQL_update_Query,('surat',200))

        connection.commit()

        # no_of_rows_in_updated_table = cursor.rowcount() 

        return "Successfully performed updation"

    
    except (Exception, psycopg2.Error) as error:
        return "Error while inserting data into PostgreSQL "+error


    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")




app = Flask(__name__)

@app.get("/update")
def update_fxn():
    operation_status = update_tuple_of_students1_db()
    return operation_status


