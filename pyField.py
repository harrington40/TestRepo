import sys
from ruamel.yaml import YAML
import json
in_file = '/jobs/rembrandt-mayan-edkii.yaml'
out_file = '/.github/workflows/pyField.yaml'

yaml = YAML(typ='safe')
with open(in_file) as fpi:
    data = yaml.load(fpi)
    print(data)
with open(out_file, 'w') as fpo:
    json.dump(data, fpo, indent=2)