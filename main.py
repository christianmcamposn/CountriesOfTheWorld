import os
import re
import pymysql
import sys

def get_filenames(path):
    file_list = []
    for file in os.listdir(path):
        file_list.append(file)
        #print(file_list)
    return file_list

def read_filelines(path, filename, filemode):
    filelines = []
    with open(path+filename, filemode) as file:
        data = file.read()
    return data
    #.rstrip(os.linesep)
    #print(type(data))

def process_filelines(dataline, separator):
    #print('line = ' + line)
    #parts = dataline.split(",")
    dataline = dataline.replace('(informal)', '[informal]')
    parts = re.split(r',\s*(?![^()]*\))', dataline)

    for part in parts:
        print(part.strip())

def insert_country_database(country_name):
    host1 = "127.0.01"
    user1 = "root"
    password1 = "mypas1s2"
    database1 = "WorldCatalogues"
    charset1 =  'utf8'
    conn = pymysql.connect(host=host1, user=user1, password=password1, database=database1,charset=charset1, cursorclass=pymysql.cursors.DictCursor)
    # Create a cursor object
    cur  = conn.cursor()
    query = f"INSERT INTO TblCountry (CountryName) VALUES ('{country_name}')"
    cur.execute(query)
    print(f"{cur.rowcount} details inserted")
    conn.commit()
    conn.close()

"""
def insert_country_database(country_name):
    try:
        conn = mariadb.connect(
            user="root",
            password="mypas1s2",
            host="127.0.0.1",
            port=3306,
            database="WorldCatalogues"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    cursor.execute("INSERT INTO employees (CountryName) VALUES ({0})".format(country_name))
"""

def main():
    dir_path = 'files/'
    file_list = get_filenames(path = dir_path)
    for file in file_list:
        #print(file)
        print('----' + file + '----\n')
        insert_country_database(file)
        #data = read_filelines(path = dir_path, filename = file, filemode= 'r')
        #parts = process_filelines(dataline=data, separator=',')
        #print('\n')

if __name__ == '__main__':
    main()