import requests
import json
import sqlite3 as lite
import datetime

substring = input('введите подстроку для поиска: ')

url = 'https://gitlab.com/api/v4/projects'
params = {
    'search': substring
    }

# getting full json from gitlab
res = requests.get(url, params=params)
json_in = res.json() 

# connecting to the database
conn = lite.connect('gitlab_database.db')
cursor = conn.cursor()

# creating a table
try:
    cursor.execute("""
                    CREATE TABLE gitlab_projects
                    (id INT, name TEXT, description TEXT, last_activity_at TEXT, created_at TEXT)
                   """)
    conn.commit()
except lite.OperationalError:
    pass

# inserting data from json into the table, including current date and time in the same format as in initial json
for i in json_in:
    try:
        created_at = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z'
        cursor.execute("INSERT INTO gitlab_projects VALUES ('{}', '{}', '{}', '{}', '{}')".format(i['id'], i['name'], i['description'], i['last_activity_at'], created_at))
        conn.commit()
    except lite.OperationalError:
        pass
        
# creating a json file containing the table data
output_data = []

cursor.execute("SELECT * FROM gitlab_projects")
for i in cursor.fetchall():
    d = {}
    d['id'] = i[0]
    d['name'] = i[1]
    d['description'] = i[2]
    d['last_activity_at'] = i[3]
    d['created_at'] = i[4]
    output_data.append(d)
    
conn.close()

with open('gitlab_projects.json', 'w') as f:
    json.dump(output_data, f, indent=4, sort_keys=False)