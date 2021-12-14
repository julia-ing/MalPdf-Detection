import os
import pandas as pd
from logger import elk_logger
from predict import predict


def print_result(index):
    f = open('../test-data.libsvm', 'r')

    lines = f.readlines()
    result = os.popen("cat ../features.nppf | wc -l")
    result = result.read()

    for line in lines:
        minus_list = [-1] * (int(result) - 1)

        l = line.split(' #')[0]
        l = l.split(' ')
        file_name = line.split(' #')[1].strip('\n')

        for i in range(len(l)):
            if i != 0:
                key = int(l[i].split(':')[0])
                val = float(l[i].split(':')[1])
                minus_list[key - 1] = val

        result_string = str(minus_list).strip('[]')

        tmp = [[]]
        for i in range(len(result_string.split(','))):
            tmp[0].append(result_string.split(',')[i])

        final = pd.DataFrame(tmp)
        prediction = predict(final)
        print(prediction)

        if prediction == "['B']" or prediction == ['B']:
            logger = elk_logger.create_logger('elk-test-logger')
            logger.info('prediction result: benign pdf')
            return "Benign pdf with high probability"
        elif prediction == "['M']" or prediction == ['M']:
            logger = elk_logger.create_logger('elk-test-logger')
            logger.info('prediction result: malicious pdf')
            return "Malicious pdf with high probablity"
        else:
            return "Failed to predict the result"
