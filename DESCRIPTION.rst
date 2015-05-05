# jycat

json yaml cat for kubernetes

## Summary
This program concats just like cat from unix does, except,
it takes as input json and yaml files.  These json and yaml files must
be well formed. This program reads each file, converts internally to
a dictionary using yaml.load(), then adds that dictionary to a list
called 'items'.  When all files are imported the resulting dictionary
is turned back into a yaml (or json) representation (with two added elements at
the top level for Kubernetes).  If those files were Kubernetes pod,
replicationcontroller or service declarations, the resulting list is
the concatenation of those. This new list can be used to turn up/down
all of the listed resources at once. 

## Usage
```
usage: jycat.py [-h] [-p] [-t {json,yaml}]
                [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-s]
                [files [files ...]]

yaml json k8s laundry

positional arguments:
  files

optional arguments:
  -h, --help            show this help message and exit
  -p, --pretty
  -t {json,yaml}, --type {json,yaml}
                        Output type, json or yaml
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Log level (DEBUG,INFO,WARNING,ERROR,CRITICAL) default
                        is: INFO
  -s, --save            save select command line arguments (default is always)
                        in "/home/gfausak/.jycat.conf" file
jycat pod.yaml service.yaml replicationcontroller.yaml > /tmp/bigfile.yaml
```
## Arguments
* --pretty, make the output (json) pretty. yaml is already pretty. default is false.
* --help, the usage message is printed.
* --type, json or yaml (this is the OUTPUT type, input can be either), default yaml.
* ---loglevel, for debugging, default INFO.
* --save, save current arguments to persistent file in home directory, this file will be read as if it came from the command line in subsequent invocations of this program.  To remove it you have to remove the ~/.jycat.conf file manually. Do this for making pretty default, for example. the default is no save is done.
* files, this is the list of files to process. must have at least one. any one of the files can be a - dash indicating taking it from stdin. default is a single file -.  One note here, if a single file is specified the output will not be a List.

## Notes
The top of the file will look like this (in yaml presentation):

```
apiVersion: v1beta3
kind: List
items:
```

Then, for each file that is concatenated, there are two spaces inserted before
each line, and the first line has - added (indicating an element of item).

## Examples
I initially wrote this to create encapsulated Kubernetes scripts that can
be launched with a single command.  I found another use when the api was upgraded
from v1beta1 to v1beta3, there is a program called kube-version-change which converts
json from beta 1 to beta 3.  It doesn't work with yaml.  My scripts are all yaml,
so this was modified to convert from one to another. So, here is how you might update
a yaml from beta 1 to 3:

```
jycat beta1.yaml -t json | kube-version-change | jycat - > beta3.yaml
```

In the previous example the yaml file is promoted to json, then the json is
processed by the kube-version-change go program, finally, jycat - converts the
imput back to yaml.

The next example shows how to 'package' more than one Kubernetes resource file
into a single file:

```
jycat file1.yaml file2.yaml file3.yaml > package.yaml
```

The resulting file is passable to kubectl, like this:

```
kubectl create -f package.yaml
```

which does about the same thing as this:
```
kubectl create -f file1.yaml
kubectl create -f file2.yaml
kubectl create -f file3.yaml
```


