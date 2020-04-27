#!/usr/bin/env python

# Ressources: 

import numpy as np
#import pandas as pd

#!curl -O https://raw.githubusercontent.com/DJCordhose/ml-examples/master/datasets/Iris/iris_dirty.csv
#ls -l

#df = pd.read_csv('iris_dirty.csv',header=None ,encoding='iso-8859-15',names=['sepal length', 'sepal width', 'petal length', 'petal width',]) 'class'])


from farmware_tools import get_config_value, device

#df.loc[82,'sepal width'] = value

INPUT_VALUE = get_config_value(farmware_name='CSV File API', config_name='input', value_type=str)
device.log(message='Hello Farmware! Input was: {}'.format(INPUT_VALUE), message_type='success')
