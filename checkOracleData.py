import oracledb
import yaml

# Load connection config from YAML
with open('oracle.yml') as stream:
    config = yaml.safe_load(stream)
    connection = config['connection']

# Update connection to use SYSDBA mode if using SYS
connection['mode'] = oracledb.SYSDBA  # Use SYSDBA mode if connecting as SYS

# Function to check if the table has data
def check_table_has_data(table_name):
    try:
        # Connect to Oracle
        cnx = oracledb.connect(**connection)
        if cnx:
            print(f"Connected to Oracle DB.\nChecking if {table_name} has data...")

            # Query to count rows in the table
            #sql_query = f"SELECT COUNT(*) FROM {table_name}"
            sql_query = f"SELECT * FROM {table_name}"

            with cnx.cursor() as cursor:
                cursor.execute(sql_query)
                #row_count = cursor.fetchone()[0]
                row_count = cursor.fetchall()

                if row_count > 0:
                    print(f"The table {table_name} has {row_count} rows of data.")
                    return True
                else:
                    print(f"The table {table_name} is empty.")
                    return False

            # Close connection
            cnx.close()

    except oracledb.DatabaseError as e:
        print(f"Database error occurred: {e}")
        return False

# Usage Example
table_name = 'sys.student'  # Replace with your table name
check_table_has_data(table_name)

