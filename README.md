# ***IoTChatbot***
![image](https://user-images.githubusercontent.com/76246968/127762969-0b0b08ea-84e5-41cd-a843-ae954c220526.png)


## Abstract 
 It is a chatbot integrated with an Iot (Internet of Things) network of devices. The chatbot acts as an interface for the user to view real time data and live status of home appliances as well as control them by giving commands.

## Motivation
Using IoT to allow communication between various home appliances, security systems, lighting, entertainment systems and sensors will enhance lives of people and make homes smarter. Controlling home device via chatbot remotely is convenient, easy to use and time saving.
    
## Networking 
 ### Creation of IoT Network Using MQTT (Message Queuing Telemetry Transport)
   - Adding multiple client requires threading and has overhead if we havemany IoT applications.So, we used MQTT protocol which is suitable for IoT network. 
   - We used Paho MQTT module in python library to create clients(sensors and IoT devices).They continuously send their data to their respective topic to the broker in small      time intervals. 
   - This data is then received by flask server which acts as subscriber in this case. MQTT has been implemented in flask with the help of flask-mqtt module in python.
  ![image](https://user-images.githubusercontent.com/76246968/127762697-35ea25c1-0845-4827-a4b0-a41863896f34.png)

## Chatbot
  - We used Flask-python Framework for creating Chatbot and Dashboard
  - We also added auth login system for security measures
  - Sqlite3 act as an database in backend
  - ***Microsoft Azure App services act as Cloud based hosting platform*** 
 
## WORKFLOW
 ### IoT-chatbot Architecture

  ![Screenshot (376)](https://user-images.githubusercontent.com/76246968/127763126-a25261c6-256c-4462-b347-6034bd148757.png)

## Applications
  - Healthcare Sector
  - Home Automation
  - Automotive IoT
  - Industrial Automation
  - Wearables

## Limitation 
  - Currently our broker/server can handle only upto 8 clients/Iot devices 

## Future Improvements : 
 - ML model for better User experience which can give best suggestions to user by analysing previous user input.
 - Allowing connection of more clients
 - Raspberry Pi and Sensors usage so that we can deal with realtime data.
 






## Installation
 >By Using Hosted Website 
   - Download the all files from folder [sensors](https://github.com/Nageshbansal/IotChatbot/tree/main/sensors) 
   -  Install Python 
   -  Install Paho-mqtt
      ``` 
      pip install paho-mqtt
      ```
   - Run each files in a seperate terminal 
   
     ```
     python pub_temp.py
     python pub_humidity.py
     python pub_fan.py
     python pub_light.py
     ```
     
   - Open the link [IotChatbot](https://iotchatbot.azurewebsites.net/)
   - Use following credentials
       ```
       Username: test
       Password : 1234 
        ```
>By Using Local Host
   - Downlaod the code as a zip file 
     or clone the repo By using following command in git bash
     ```
      git clone https://github.com/marsiitr/IoT-ChatBot.git
      ```
   - create venv (optional)
   - Install required python-packages 
      ```
        pip install -r requirements.txt
      ```
   - Go to Iotchatbot directory in command line and run flask app
      ```
      python app.py
     ```
   - Go to sensors directory and  Run each files in a seperate terminal 
     ```
     python pub_temp.py
     python pub_humidity.py
     python pub_fan.py
     python pub_light.py
     ```
     
   - Open the link in browser 
      ```
        http://127.0.0.1:5000/
       ```
   - Use following credentials
       ```
       Username: test
       Password : 1234 
        ```
  ## Hosted Chatbot
   [http://iotchatbot.azurewebsites.net/](http://iotchatbot.azurewebsites.net/)
  
  ## Team Members
  1. [Khushi Kumawat](https://github.com/khushi861)
  2. [Kushagra Agarwal](https://github.com/Kushagra-Agarwal44)
  3. [Nagesh Bansal](https://github.com/Nageshbansal)
  4. [Vaishnavi Gupta](https://github.com/vaishnavi-gupta18)
  
  ## Mentors
  1. [Pradnesh Chavan](https://github.com/theobscuredev)
  2. [Sanjeev Krishnan R.](https://github.com/SanjeevKrishnan)
  
  
  ## References
  1. [MQTT Basics](https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4)
  2. [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
  3. [IoT Architecture](https://www.avsystem.com/blog/what-is-iot-architecture/)
  4. [Azure IoTHub](https://docs.microsoft.com/en-in/azure/iot-hub/)
  
  
