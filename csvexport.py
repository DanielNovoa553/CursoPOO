# programa que haga un select mysql y exporte a csv
import pandas as pd
import os
from conexion_db import connectdb
from datetime import datetime

def exportar_datos_csv():
    """
    Export data from database to csv file
    Returns:
        None
    """
    x = datetime.now()  # Get current date and time
    date = x.strftime("%d_%m_%Y_%H_%M_%S")  # change format date to string

    con = connectdb()  # connect to database
    if not con: # If connection is not established
        print("Error al conectar a la base de datos")
        exit()  # Close program

    cur = con.cursor()  # create cursor
    query = "SELECT * FROM usuarios"  # Query to select data
    cur.execute(query)  # Execute query
    results = cur.fetchall()  # Fetch all data

    df = pd.DataFrame(results, columns=["id", "nombres", "apellidos", "usuario"])   # Create dataframe
    profit = df['profit'] = df['id'] * 1000000.34 / 2.5  # Add date column
    profit = pd.Series(profit)  # Convert to series to apply lambda function
    profit = profit.apply(lambda x: "{:,.2f}".format(x))  # Replace . with ,

    df = df.sort_values(by=['id'], ascending=False)# Sort dataframe by id column (descending
    df['profit'] = profit   # Add profit column to dataframe
    print(df)
    nameFile = "datos_" + date + ".csv"  # Create filename

    # Export dataframe to csv
    df.to_csv(f"C:/Users/danie/OneDrive/Documentos/Balance_Profit_Users/{nameFile}", index=False, decimal=",",
              encoding='latin1')   #write data to csv file

    filePath = os.path.abspath(f"C:/Users/danie/OneDrive/Documentos/Balance_Profit_Users/{nameFile}")  # Get absolute path of file
    os.startfile(filePath)  # Open file

    print("Datos exportados exitosamente a --> datos.csv")
    con.close()  # Close connection
    cur.close()  # Close cursor


if __name__ == '__main__':  # If file is executed directly
    try:
        exportar_datos_csv()  # Execute function exportar_datos_csv
    except Exception as e:
        print("Ocurrió un error al exportar los datos: ", e)
        exit()
