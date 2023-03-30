from flask import Flask
import psycopg2




def delete_from_students1_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="pass",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="adityaved")
        
        cursor = connection.cursor()

        postgreSQL_delete_Query = """
    
        delete from students1
        where student_id = %s

        """

        cursor.execute(postgreSQL_delete_Query,(400,))

        connection.commit()

        # no_of_rows_in_updated_table = cursor.rowcount() 

        return """Successfully performed deletion , 
        
        Note :: this message will appear even in 2 cases :
        1) the tuple was acutually deleted from database
         2) there was no tuple and still we tried to delete that tuple """

    
    except (Exception, psycopg2.Error) as error:
        return "Error while inserting data into PostgreSQL "+error


    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")




app = Flask(__name__)

@app.get("/delete")
def delete_fxn():
    operation_status = delete_from_students1_db()
    return operation_status


