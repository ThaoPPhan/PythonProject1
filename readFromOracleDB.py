import oracledb
import yaml

# Load connection config from YAML
with open('oracle.yml') as stream:
    config = yaml.safe_load(stream)
    connection = config['connection']

# Update connection to use SYSDBA mode if using SYS
connection['mode'] = oracledb.SYSDBA  # Use SYSDBA mode if connecting as SYS

# Connect to Oracle
try:
    cnx = oracledb.connect(**connection)
    if cnx:
        print("Open connection OK")

        # SQL queries to fetch records from Student, Grade, and Course tables
        sql_student = "SELECT * FROM Student ORDER BY ID"
        sql_grade = "SELECT * FROM Grade ORDER BY ID"
        sql_course = "SELECT * FROM Course ORDER BY ID"

        # Function to print records from any table
        def print_records(sqlQry, table_name):
            print(f"\nRunning SQL for {table_name}: {sqlQry}")
            with cnx.cursor() as cursor:
                cursor.execute(sqlQry)
                records = cursor.fetchall()
                if records:
                    for i, row in enumerate(records, start=1):
                        print(f"Record {i}: {row}")
                else:
                    print(f"No records found in {table_name}")

        # Execute queries and print results for each table
        print_records(sql_student, 'Student')
        print_records(sql_grade, 'Grade')
        print_records(sql_course, 'Course')

        print("\nClose connection")
        cnx.close()

    else:
        print("Could not connect to Oracle DB")

except oracledb.DatabaseError as e:
    print(f"Database error occurred: {e}")
