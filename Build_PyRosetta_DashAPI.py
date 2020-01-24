#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
import shutil

RootDir = os.getcwd()

def wget_api_document():
    '''    
    Download pyrosetta API from graylab.
    '''

    os.system('wget -r -p -np -k -T 60 https://graylab.jhu.edu/PyRosetta.documentation/')


def create_dashing_json(html_path):
    contents = '''
{
    "name": "PyRosetta",
    "package": "PyRosetta",
    "index": "index.html",
    "selectors": {
        "dl.class>dt code.descname": "Class",
        "dl.function>dt code.descname":"Function",
        "dl.attribute>dt code.descname":"Attribute",
        "dl.method>dt code.descname":"Method",
        "h1": "Package"
    },
    "ignore": [
        "ABOUT"
    ],
    "icon32x32": "%s/pyrosetta.png",
    "allowJS": true,
    "ExternalURL": "https://graylab.jhu.edu/PyRosetta.documentation/"
}
'''%RootDir

    with open(os.path.join(html_path, 'dashing.json'), 'w') as f:
        f.write(contents)


def run():

    # download;
    wget_api_document()

    # build;
    html_path = os.path.join(RootDir, 'graylab.jhu.edu/PyRosetta.documentation')
    os.chdir(html_path)
    create_dashing_json(html_path)
    os.system('dashing build')  # building the dash

    # mv docset
    shutil.move(os.path.join(os.getcwd(), 'PyRosetta.docset'), RootDir)


if __name__ == "__main__":
    run()