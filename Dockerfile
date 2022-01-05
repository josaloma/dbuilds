#For exercise 1.15
# Start from python latest image
FROM python

# Use /usr/src/app as our workdir. The following instructions will be executed in this location.
WORKDIR /usr/src/app

# Copy current folder to docker
COPY . .

 
CMD [ "python", "./main.py" ]

#docker build . -t dockertest && docker run -it --name dockertest dockertest
#docker exec -it peli bash



