from flask import Flask
import psycopg2




def insert_into_students1_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="pass",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="adityaved")
        cursor = connection.cursor()
        postgreSQL_insert_Query = """
        
        insert into students1 
        values(%s,%s,%s,%s,%s,%s)

        """

        record_to_insert = (400,'name4','kerala','addr4','pin4',8.9)

        cursor.execute(postgreSQL_insert_Query,record_to_insert)

        connection.commit()

        return "Successfully performed insertion"

    
    except (Exception, psycopg2.Error) as error:
        return "Error while inserting data into PostgreSQL "+error


    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")




app = Flask(__name__)


@app.get("/insert")
def insert_fxn():
    operation_status = insert_into_students1_db()
    return operation_status


