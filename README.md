# studio_pyside6

Clone/download the repo then (tested on a Mac silicon):

```
$ cd PhysiCell-Studio-development
$ sudo docker build -t studio-dev-docker .
...

$ IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
$ xhost +
access control disabled, clients can connect from any host
$ docker run --rm -it  -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=$IP:0 studio-dev-docker
```

the `docker run` command seems to run (it dumps some debug print info from the application), but the GUI is not displayed. And I cannot simply ctl-C to kill the process; I have to "force stop" the `docker` (lower-case) process in the "Activity Monitor" utility. I tried to mimic the Dockerfile in https://github.com/rheiland/docker_simple_mpl which, while not doing the more complex Python Qt GUI as we are attempting to do here, did at least display a matplotlib plot for its `docker run`.
