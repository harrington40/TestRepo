#!/usr/local/bin/python3.9

import yaml

with open('rembrandt-mayan-edkii.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)