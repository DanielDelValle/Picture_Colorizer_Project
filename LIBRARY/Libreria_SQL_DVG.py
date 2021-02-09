def sqlite_to_csv(file_path, table_name, output_file):
    """ Creates a csv file from sqlite file

        Args:   
            file_path ([str]): path of the sqlite file to be converted
            table_name ([str]): name of the table to be converted
            output_file ([str]): name of the output csv file
    """
    # Creates SQL connection
    try:
        connection = sqlite3.connect(file_path, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    except FileNotFoundError:
        print("ERROR: File not found.")
    except:
        print("ERROR: SQL connection not created.")

    # Reads table from SQLite file and exports it to a csv file
    try:
        database = pd.read_sql_query("SELECT * FROM " + table_name, connection)
        database.to_csv(output_file, index=False)
    except:
        print("ERROR: CSV file not created.")