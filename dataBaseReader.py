import pandas as pd
import pymysql


def creatCsv(stop=100000, step=100):
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root', password='123456',
                         database='comDataBaseName',
                         charset='utf8mb4')

    cursor = db.cursor()

    n = 0
    trainData = pd.DataFrame(columns=['label', 'review'])
    trainData.to_csv(r'./data/UnprocessedData.csv', mode='w', encoding='utf-8', columns=['label', 'review'], index=0)
    while n <= stop:
        sql = f'SELECT message FROM bilicomment limit {n}, {step}'
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            if result == ():
                return
        except:
            db.rollback()
            db.close()
        num = n
        for j in result:
            trainData.loc[num] = ['', j[0]]
            num += 1
        n += step
        trainData.to_csv(r'./data/UnprocessedData.csv', mode='a', encoding='utf-8', header=0, index=0)
    db.close()


if __name__ == '__main__':
    creatCsv(50000)
