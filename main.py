"""
@author: github/ObjectAstra
"""

import random
import argparse

cn_area = (0x4e00, 0x9fff)
en_area = (0x0020, 0x007f)

def generate_xgzyish_cn(length: int):
    return ''.join([chr(random.randint(*cn_area)) for i in range(length)])

def generate_xgzyish_en(length: int):
    return ''.join([chr(random.randint(*en_area)) for i in range(length)])


parser = argparse.ArgumentParser(description='Generate XGZY-ish string')

parser.add_argument('-l', '--length', type=int, default=10, help='Length of the string')
parser.add_argument('-t', '--type', type=str, default='cn', help='Type of the string (cn/en)')

args = parser.parse_args()

if args.type == 'cn':
    print(generate_xgzyish_cn(args.length))
elif args.type == 'en':
    print(generate_xgzyish_en(args.length))
else:
    print('Invalid type')