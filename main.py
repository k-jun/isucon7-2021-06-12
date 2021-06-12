import mysql.connector
import cchardet
import base64

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database="isubata",
)

cur = conn.cursor(dictionary=True)
cur.execute('select * from image')

result = cur.fetchall()

for i in result:
    with open("./public/icons/" + i["name"], "wb") as f:
        f.write(i["data"])
