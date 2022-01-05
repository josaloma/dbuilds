# dbuilds

 simple docker build service

https://devopswithdocker.com/part3/

3.2 Building images inside of a container

Watchtower uses volume to docker.sock socket to access Docker daemon of the host from the container. By leveraging this ourselves we can create our own simple build service.

Create a project that downloads a repository from github, builds a Dockerfile located in the root and then publishes it into Docker Hub.

You can use any programming language / technology for the project implementation. A simple bash script is viable.

Then create a Dockerfile for it so that it can be run inside a container.

Make sure that it can build at least some of the example projects.

------------------------------------------------------------------------------------

This docker image is for course Dev Ops with docker by Aalto university.

This docker image just prints docker works and local time every 5 seconds after running it.

Software for printing have been done with python to test running own python code inside docker.Own codecan be found from file main.py.

image have been done from latest python official docker image. 

to run the project:

docker run -it --name dockertest dockertest

docker file included also. to run from docker file: 

docker build . -t dockertest && docker run -it --name dockertest dockertest
