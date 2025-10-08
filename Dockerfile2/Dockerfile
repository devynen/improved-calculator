FROM python:3.12.11-slim
 #got the version from hub.docker.com (python official image)... slim because it takes lesser data as opposed to trixie.
 #note this image is built by someone. we'll build ours

 WORKDIR /app
 #mkdirn -p /app & cd /app
 #copy file contents from my computer to this virtual computer
 COPY recharge.py .
 #the command that is ran so i dont have to do python3 grade.py
 # note theres no 3 on the python coz i already did on line 1.
 CMD ["python","recharge.py"] 


#basically this is my image file.a recipe.anyone who pulls this will 