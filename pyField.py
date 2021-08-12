#!/usr/local/bin/python3.7

import yaml

with open('items.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)