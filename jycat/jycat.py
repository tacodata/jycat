#!/usr/bin/env python2.7
# concat json or yaml files into large k8s List
# p.py file1 file2 file3
# produces all files on output wrapped by an enclosing list
import yaml
import sys

def run():
    av = sys.argv
    av.pop(0)

    s = { "apiVersion":"v1beta3", "kind":"List", "items":[] }

    for i in range(len(av)):
        s['items'].append(yaml.load(open(av[i]).read()))

    print yaml.dump(s)

if __name__ == '__main__':
   run()
