import snownlp
import csv

snownlp.sentiment.load(r'result/sentiment.marshal')


def process():
    def nlp(str):
        label = snownlp.SnowNLP(str)
        return '1' if label.sentiments >= 0.5 else '0'

    # data = pd.read_csv(r'./data/UnprocessedData.csv', encoding='utf-8')
    # data.loc[:, 'label'] = data.loc[:, 'review'].apply(nlp)
    # data.to_csv(r'./data/preData.csv', mode='w', encoding='utf-8', columns=['label', 'review'], index=0)
    writer = open(r'data/preData.csv', mode='w', encoding='utf-8', newline='')
    csv_writer = csv.writer(writer, dialect='excel')
    csv_writer.writerow(['label', 'review'])
    with open(r'data/UnprocessedData.csv', 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp)
        reader.__next__()
        for row in reader:
            csv_writer.writerow([nlp(row[1]), row[1]])
    writer.close()


if __name__ == '__main__':
    process()
