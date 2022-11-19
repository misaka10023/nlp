import pandas as pd
import snownlp


def train():
    print('正在将训练集分类')
    # data = pd.read_csv(r'./data/trainData.csv', encoding='utf-8')
    data = pd.read_csv(r'./data/preData.csv', encoding='utf-8')
    neg = data.iloc[:, 1][data.label == 0]
    pos = data.iloc[:, 1][data.label == 1]
    neg.to_csv(r'./data/neg.csv', index=0, header=0)
    pos.to_csv(r'./data/pos.csv', index=0, header=0)
    print('分类完成， 开始训练')
    snownlp.sentiment.train(r'./data/neg.csv', r'./data/pos.csv')
    print('训练完成， 文件将储存于result文件夹内')
    snownlp.sentiment.save(r'./result/sentiment.marshal')


if __name__ == '__main__':
    train()
