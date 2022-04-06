#Specifying the base image
FROM python:3.10
#here the dockerfile is pulling the python 3.10 from docker hub which already has python installed so we have all the things we need to have python in our container.
ADD good_string.py.
#Here we added the python file that we want to run in docker and define its location.
CMD [ "python3" "./good_string.py" ]
#lastly we specified the entry command this line is simply running python ./main.py in our container terminal

