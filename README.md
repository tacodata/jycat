# jycat
[![Version](https://pypip.in/version/jycat/badge.svg)![Status](https://pypip.in/status/jycat/badge.svg)![Downloads](https://pypip.in/download/jycat/badge.svg)](https://pypi.python.org/pypi/jycat/)[![Build Status](https://travis-ci.org/lgfausak/jycat.svg?branch=master)](https://travis-ci.org/lgfausak/jycat)

json yaml cat for kubernetes

## Summary
This is a silly program that concats just like cat from unix does, except,
it takes as input json and yaml files.  These json and yaml files must
be well formed. This program reads each file, converts internally to
a dictionary using yaml.load(), then adds that dictionary to a list
called 'items'.  When all files are imported the resulting dictionary
is turned back into a yaml representation (with two added elements at
the top level for Kubernetes).  If those files were Kubernetes pod,
replicationcontroller or service declarations, the resulting list is
the concatenation of those. This new list can be used to turn up/down
all of the listed resources at once. 

## Usage
```
jycat pod.yaml service.yaml replicationcontroller.yaml > /tmp/bigfile.yaml
```

## Notes
The top of the file will look like this:

```
apiVersion: v1beta3
kind: List
items:
```

Then, for each file that is concatenated, there are two spaces inserted before
each line, and the first line has - added (indicating an element of item).

