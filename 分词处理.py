import pymysql
import csv


db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root', password='123456',
                     database='comDataBaseName',
                     charset='utf8mb4')

cursor = db.cursor()

sql = 'SELECT message FROM bilicomment'

try:
    cursor.execute(sql)
    result = cursor.fetchall()
except:
    db.rollback()
    db.close()

f = open(r'./data/message.csv', 'a+', encoding='utf-8')
csv_write = csv.writer(f)
for i in result:
    csv_write.writerow(i)
f.close()
db.close()
