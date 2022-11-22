import pandas as pd
import sqlite3

db_path="stampcollector/database/stamps.sqlite"
query = "SELECT * FROM stamp_table"

query="""
    SELECT section, subsection_id, origin_W as origin, end_W as destination, distance, time_W as time, elevation_W as elevation 
    FROM stamp_table 
    ORDER BY section DESC, subsection_id DESC
    """

def split_elevation(row):
    data=row["elevation"]
    row["elevation_gain"]=int(data.split(" / ")[0])
    row["elevation_loss"]=int(data.split(" / ")[1])

    row.pop("elevation")
    return row

if __name__ == '__main__':
    conn=sqlite3.connect(db_path)
    sql_data=pd.read_sql_query(query, conn)
    
    sql_data=sql_data.apply(split_elevation, axis=1)
    sql_data["subsection_id"]=sql_data["subsection_id"].astype("int")
    sql_data["distance"]=sql_data["distance"].astype("float")
    sql_data["time"]=sql_data["time"]+":00"
    sql_data.to_excel("blue_stamps.xlsx")
    print(sql_data["distance"])
    