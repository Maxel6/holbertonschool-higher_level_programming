#!/usr/bin/python3
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
my_list = args
filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
my_list.extend(args)
save_to_json_file(my_list, filename)
