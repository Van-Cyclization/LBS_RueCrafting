# -*- coding: UTF-8 -*-

import json

woods = ['acacia', 'birch', 'crimson', 'dark_oak', 'jungle', 'spruce', 'oak', 'warped']
products = ['stairs', 'slab']


def jsonGenerate():
    for wood in woods:
        for product in products:
            file_name = f'rnc_{wood}_{product}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
  "type": "stonecutting",
  "group": "wooden_{product}",
  "ingredient": {{
    "item": "{wood}_planks"
  }},
  "result": "{wood}_{product}",
  "count": {products.index(product) + 1}
}}
'''
            json_file.write(file_contents)


if __name__ == '__main__':
    jsonGenerate()
