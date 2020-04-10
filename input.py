#!/usr/bin/env python

# Ressources: 

import numpy as np
import pandas as pd

#!curl -O LOCATION/NAME.csv
#ls -l

df = pd.read_csv('NAME.csv',
                 header=None,
                 encoding='iso-8859-15',
                 names=['temp', 'hummidity', 'co2', 'phase', 'time'])
   
from farmware_tools import get_config_value, device


INPUT_VALUE = get_config_value(farmware_name='Hello Farmware Input', config_name='input', value_type=str)
device.log(message='Hello Farmware! Input was: {}'.format(INPUT_VALUE), message_type='success')
