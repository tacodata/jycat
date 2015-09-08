# maas-util
[![Version](https://pypip.in/version/maas-util/badge.svg)![Status](https://pypip.in/status/maas-util/badge.svg)![Downloads](https://pypip.in/download/maas-util/badge.svg)](https://pypi.python.org/pypi/maas-util/)[![Build Status](https://travis-ci.org/lgfausak/maas-util.svg?branch=master)](https://travis-ci.org/lgfausak/maas-util)

maas utility for a 1.8 maas region installation

## Summary
Provide misc command line stuff for maas. The first one I need
is the ability to determine the system_id given the machine name.

## Usage
```
usage: maas-util.py [-h] [-p] [-t {json,yaml,text}]
                [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -p, --pretty
                        Pretty only works if the output is json
  -t|--type {json,yaml,text}
                        Output type, json, yaml or text, text is the default 
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Log level (DEBUG,INFO,WARNING,ERROR,CRITICAL) default
                        is: INFO
  -s, --save            save select command line arguments (default is always)
                        in "/home/gfausak/.maas-util.conf" file
maas-util.py node_by_name nodename
```
## Arguments
* --pretty, make the output (json) pretty. yaml is already pretty. text is ugly. default is false.
* --help, the usage message is printed.
* --type, json or yaml or text (this is the OUTPUT type), default text.
* ---loglevel, for debugging, default INFO.
* --save, save current arguments to persistent file in home directory, this file will be read as if it came from the command line in subsequent invocations of this program.  To remove it you have to remove the ~/.maas-util.conf file manually. Do this for making pretty default, for example. the default is no save is done.

## Notes

none yet

## Examples

```
maas-util.py node_by_name
```



