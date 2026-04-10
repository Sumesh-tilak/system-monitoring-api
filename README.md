# system-monitoring-api

A simple pyhton Flask based API to monitor system health metrics

##Features
-Cpu usage monitoring 
-Memory usage monitoring 
-Disk usage Monitoring 
-Dockerized for easy deployment

##Tech Stack
-Python
-Flask
-psutil
-Docker

##Run Locally

bash
python app.py

## Run with Docker 
 
 bash 
 docker build -t system-monitor .
 docker run -d -p 5000:5000 system-monitor