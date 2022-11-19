import dataBaseReader
import autoProcessing
import Calibration
import nlpTrain
import tencent


if __name__ == '__main__':
    # dataBaseReader.creatCsv()
    print("数据读取完成")
    # autoProcessing.process()
    print("情感标注完成")
    # 数据校验
    # Calibration.Calibration()
    tencent.tencentCali()
    print("准备开始训练")
    nlpTrain.train()
