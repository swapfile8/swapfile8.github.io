import os
import glob
import json
base_path = 'images'
dirs = [[d, os.path.join(base_path, d)] for d in os.listdir(base_path)]
dirs = list(filter(lambda x: os.path.isdir(x[1]) and not os.path.isfile(os.path.join(x[1], 'no.media')), dirs))
config = {}
for x in dirs:
    prefix, path = x
    print(f'Path: {path}')
    files = glob.glob(os.path.join(path, '*.jpg'))
    for y in files:
        config[f'{prefix}_{os.path.splitext(os.path.basename(y))[0]}'] = y
with open('wdts-config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=4, ensure_ascii=False)
