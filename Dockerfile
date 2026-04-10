#Use official python image
From python:3.12-slim

#Set working directory
WORKDIR /app

#Copy files 
COPY requirements.txt .

#Install Dependecies
RUN pip install --no-cache-dir -r requirements.txt

#Copy files
COPY . .


#Expose port 
EXPOSE 5000

#Run app 
CMD ["python","app.py"]