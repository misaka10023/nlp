import pandas as pd


def Calibration():
    data = pd.read_csv(r'./data/preData.csv', encoding='utf-8')
    # data = pd.read_csv(r'preData.csv', encoding='utf-8')
    for i in range(len(data)):
        print(f"情感程度：{data.loc[i, 'label']}")
        if float(data.loc[i, 'label']) > 0.6:
            data.loc[i, 'label'] = 1
            print("预测情感：积极")
        else:
            data.loc[i, 'label'] = 0
            print("预测情感：消极")
        print(f"评论：\n{data.loc[i, 'review']}")
        label = input()
        if label != '' and label.isdigit():
            data.loc[i, 'label'] = label
    data.to_csv(r'./data/trainData.csv', mode='w', encoding='utf-8', columns=['label', 'review'], index=0)
