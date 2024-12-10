# studio_pyside6

Clone/download the repo then:

```
$ cd PhysiCell-Studio-development
$ sudo docker build -t studio-dev-docker .
...

$ sudo docker run -it studio-dev-docker
Traceback (most recent call last):
  File "/app/bin/studio.py", line 31, in <module>
    from PySide6 import QtCore, QtGui
ImportError: libEGL.so.1: cannot open shared object file: No such file or directory

$ sudo docker run -v /usr/lib/x86_64-linux-gnu/:/usr/lib/x86_64-linux-gnu/  -it studio-dev-docker
... similar ImportError
```
