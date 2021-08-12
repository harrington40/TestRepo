import ruamel.yaml
import json
in_file = '/jobs/rembrandt-mayan-edkii.yaml'
out_file = 'output.json'

yaml = ruamel.yaml.YAML(typ='safe')
with open(in_file) as fpi:
    data = yaml.load(fpi)
with open(out_file, 'w') as fpo:
    json.dump(data, fpo, indent=2)