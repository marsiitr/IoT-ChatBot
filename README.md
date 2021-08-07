# Iot-Chatbot
## Open Projects 2021


<p align="center">
 <img src="https://user-images.githubusercontent.com/76246968/127762969-0b0b08ea-84e5-41cd-a843-ae954c220526.png" alt="Iot-Chatbot">
 <i>Iot-Chatbot</i>
</p>


<p align="justify">
<h2>Abstract</h2>
<p>It is a chatbot integrated with an Iot (Internet of Things) network of devices. The chatbot acts as an interface for the user to view real time data and live status of home appliances as well as control them by giving commands.</p>
</p>
 
<p align="justify">
<h2>Motivation</h2>
<p>Using IoT to allow communication between various home appliances, security systems, lighting, entertainment systems and sensors will enhance lives of people and make homes smarter. Controlling home device via chatbot remotely is convenient, easy to use and time saving.</p>
</p>

<p align="justify">
<h2>WORKFLOW</h2>
</p>

<p align="center">
 <img src="https://user-images.githubusercontent.com/76246968/127763126-a25261c6-256c-4462-b347-6034bd148757.png" alt="workflow">
 <i>IoT-chatbot Architecture</i>
</p>

<p align="justify">
<h2>Software Aspect</h2>

 <h3>Networking</h3> 
  <h4>Creation of IoT Network Using MQTT (Message Queuing Telemetry Transport)</h4>

   - Adding multiple client requires threading and has overhead if we havemany IoT applications.So, we used MQTT protocol which is suitable for IoT network. 
   - We used Paho MQTT module in python library to create clients(sensors and IoT devices).They continuously send their data to their respective topic to the broker in small          time intervals. 
   - This data is then received by flask server which acts as subscriber in this case. MQTT has been implemented in flask with the help of flask-mqtt module in python.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/76246968/127762697-35ea25c1-0845-4827-a4b0-a41863896f34.png">
  <i>Mqtt Communication</i>
  </p>
 </p>
 

 <h3>Chatbot</h3>

  - We used Flask-python Framework for creating Chatbot and Dashboard
  - We also added auth login system for security measures
  - Sqlite3 act as an database in backend
  - ***Microsoft Azure App services act as Cloud based hosting platform*** 

 </p>
 

<p align="justify">
 <h2>Cost Structure</h2>
 </p>
| Software Components | Cost |
|:---------------------:|:----:|
| Python | None(Open-Source) |
| Flask | None(Open-Source) |
| Paho MQTT | None(Open-Source) |
| Cloud Services | Depends on service provider |

<p align="justify">

<h2>Applications</h2>
<p>
  - Healthcare Sector
  - Home Automation
  - Automotive IoT
  - Industrial Automation
  - Wearables
</p>

<h2>Limitation</h2>
<p>
  - Currently our broker/server can handle only upto 8 clients/Iot devices 
</p>

<h2>Future Improvements</h2>
<p>
 - ML model for better User experience which can give best suggestions to user by analysing previous user input.
 - Allowing connection of more clients
 - Raspberry Pi and Sensors usage so that we can deal with realtime data.
 </p>






<h2>Installation</h2>
<p align="justify">
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
 </p>

<h2>Hosted Chatbot</h2>
   <p align="justify">[http://iotchatbot.azurewebsites.net/](http://iotchatbot.azurewebsites.net/)</p>
  
  
  <h2>Team Members</h2>
  <p>
  1. [Khushi Kumawat](https://github.com/khushi861)
  2. [Kushagra Agarwal](https://github.com/Kushagra-Agarwal44)
  3. [Nagesh Bansal](https://github.com/Nageshbansal)
  4. [Vaishnavi Gupta](https://github.com/vaishnavi-gupta18)
 </p> 
 
<h2> Mentors</h2>
<p>
  1. [Pradnesh Chavan](https://github.com/theobscuredev)
  2. [Sanjeev Krishnan R.](https://github.com/SanjeevKrishnan)
 </p> 
  
  <h2>References</h2>
  <p>
  1. [MQTT Basics](https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4)
  2. [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
  3. [IoT Architecture](https://www.avsystem.com/blog/what-is-iot-architecture/)
  4. [Azure IoTHub](https://docs.microsoft.com/en-in/azure/iot-hub/)
  </p>
  
