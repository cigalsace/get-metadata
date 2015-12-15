#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Script: getMetadata.py
'''

__author__ = "Guillaume RYCKELYNCK"
__copyright__ = "Copyright 2015 CIGAL / Région Alsace"
__license__ = "MIT"

import os
import json
import time
import re
import shutil
from libs import requests

# Get color for screen printing
class bcolors:
    HEADER = '\033[95m'     # rose
    OKBLUE = '\033[94m'     # blue
    OKGREEN = '\033[92m'    # green
    WARNING = '\033[93m'    # orange
    FAIL = '\033[91m'       # red
    ENDC = '\033[0m'        # end line
    BOLD = '\033[1m'        # bold ?
    UNDERLINE = '\033[4m'   # highlight

# Directory of nodes files
nodes_dir = 'nodes'
# Get list of nodes files
files = [ f for f in os.listdir(nodes_dir) if os.path.isfile(os.path.join(nodes_dir,f)) ]

count_file = 1
for file in files:
    print ''
    print bcolors.OKGREEN + u'*'*80 + bcolors.ENDC
    print bcolors.OKGREEN + u'File ' + str(count_file) + '/' + str(len(files)) + ': ' + file + '.' + bcolors.ENDC
    if file.startswith('_'):
        print u'Fichier ignoré.'
    else:
        file_path = os.path.join(nodes_dir, file)
        with open(file_path, 'r') as json_data:
            data = json.load(json_data)

        print bcolors.BOLD + u'Organisme: ' + data['organisme'] + bcolors.ENDC
        
        count_node = 1
        for node in data['nodes']:
            print ''
            print bcolors.OKBLUE + u'-'*80 + bcolors.ENDC
            print bcolors.OKBLUE + u'Node ' + str(count_node) + '/' + str(len(data['nodes'])) + bcolors.ENDC
            print u'Description: ' + node['description']
            if node['active'] == '0':
                print u'Noeud désactivé.'
            else:
                print u'Active: ' + node['active']
                print u'Source: ' + node['src_domain'] + node['src_path']
                print u'Destination: ' + node['dst_path']
                print u'Pattern: ' + node['pattern'] % node['src_path']
                
                src_url = node['src_domain'] + node['src_path']
                pattern = node['pattern'] % node['src_path']
                
                # Remove dst directory and recreate it (empty)
                if os.path.isdir(node['dst_path']):
                    shutil.rmtree(node['dst_path'])
                os.mkdir(node['dst_path'])
                
                r = requests.get(src_url)

                print u'Start: ' + str(time.strftime("%Y-%m-%d %H:%M:%S"))
                
                for filename in re.findall(pattern, r.text):
                    r = requests.get(src_url+filename)
                    with open(node['dst_path']+filename, 'w') as f:
                        f.write(r.text.encode('utf-8'))
                    print '=> ' + filename + bcolors.OKGREEN + u' [OK]' + bcolors.ENDC

                print u'End: ' + str(time.strftime("%Y-%m-%d %H:%M:%S"))

                count_node += 1
                
        count_file += 1
        