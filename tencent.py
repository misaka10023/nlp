import csv
import json
import time

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
import pandas as pd

import tencent
cred = credential.Credential("AKIDSlsWaT7X0JOFtJVSPCl6Gl37jAOGvNaY", "nMhneHm23qOmxypTs53nMkx42oMfkcFg")


def nlp(text):
    try:
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SentimentAnalysisRequest()
        params = {
            "Text": f"{text}"
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个SentimentAnalysisResponse的实例，与请求对象对应
        resp = client.SentimentAnalysis(req)
        # 输出json格式的字符串回包
        ans = json.loads(resp.to_json_string())
        return ans['Positive']

    except TencentCloudSDKException as err:
        print(err)
        return err

    except Exception as err:
        print(err)
        return err


def updata(Positive):
    if type(Positive) == float:
        return '1' if float(Positive) >= 0.5 else '0'
    else:
        return Positive


def tencentCali():
    # data = pd.read_csv(r'./data/UnprocessedData.csv', encoding='utf-8')
    # data.loc[:, 'label'] = data.loc[:, 'review'].apply(nlp)
    # data.loc[:, 'label'] = data.loc[:, 'label'].apply(updata)
    # data.to_csv(r'preData.csv', mode='w', encoding='utf-8', columns=['label', 'review'], index=0)
    w = open(r'data/trainData.csv', mode='w', encoding='utf-8', newline='')
    p = open(r'data/problematicData.csv', mode='w', encoding='utf-8', newline='')
    writer = csv.writer(w, dialect='excel')
    writer.writerow(['label', 'review'])
    problem = csv.writer(p, dialect='excel')
    problem.writerow(['label_snownlp', 'label_tencent', 'review'])
    with open(r'data/preData.csv', mode='r', encoding='utf-8') as fp:
        reader = csv.reader(fp)
        reader.__next__()
        for row in reader:
            label = updata(nlp(row[1]))
            if row[0] == label:
                writer.writerow([label, row[1]])
            else:
                problem.writerow([row[0], label, row[1]])
    w.close()
    p.close()


if __name__ == '__main__':
    tencentCali()
