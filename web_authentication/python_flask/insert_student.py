import psycopg2


def insert_student_into_db(studentId,rollNo,studentName,studentEmail,studentPassword,studentCurrentSem,deptId):
    connection = 0
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="pass",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres",
                                    options="-c search_path=sy_mp,public")

        cursor = connection.cursor()

        postgreSQL_insert_Query = """
        
        insert into student 
        values(%s,%s,%s,%s,%s,%s,%s)

        """

        record_to_insert = (studentId,rollNo,studentName,studentEmail,studentPassword,studentCurrentSem,deptId)

        cursor.execute(postgreSQL_insert_Query,record_to_insert)
        
        connection.commit()

        return 1,"1"

    except (Exception, psycopg2.Error) as error:
        return 0,"Error while inserting data into PostgreSQL : "+ str(error)
        

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        
        

