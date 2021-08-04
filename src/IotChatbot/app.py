from flask import Flask, render_template, jsonify, redirect, request
import json
import database
from random import choice
from datetime import datetime
import person
import os
import sqlite3
import random
import eventlet
import binascii
import string
from flask_mqtt import Mqtt

# from flask_socketio import SocketIO
app = Flask(__name__)
eventlet.monkey_patch()
logged_in = {}
api_loggers = {}
mydb = database.db()

temp2 = 0
app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection

# set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_KEEPALIVE'] = 5
# set TLS to disabled for testing purposes
app.config['MQTT_TLS_ENABLED'] = False

mqtt_light = Mqtt(app)
mqtt_fan = Mqtt(app)
mqtt = Mqtt(app)
mqtt_hum = Mqtt(app)


randlist = list(x for x in range(0, 20))


@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        user = person.user(request.form["username"], request.form["password"])

        if user.authenticated:
            user.session_id = str(binascii.b2a_hex(os.urandom(15)))
            logged_in[user.username] = {"object": user}
            return redirect(
                "/overview/{}/{}".format(
                    request.form["username"], user.session_id)
            )
        else:
            error = "invalid Username or Passowrd"

    return render_template("Login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        user = database.db.add_user(
            request.form["username"],
            request.form["password"],
            request.form["first_name"],
            request.form["last_name"],
            request.form["email"],
            request.form["phone_number"],
        )


# # this link is for the main dashboard of the website
# @app.route("/", methods=["GET", "POST"])
# def home():
#     return render_template("home.html", title="HOME - Landing Page")


@app.route("/overview/<string:username>/<string:session>", methods=["GET", "POST"])
def overview(username, session):

    global logged_in

    if username in logged_in and (logged_in[username]["object"].session_id == session):
        user = {"username": username, "session": session}

        devices = [{"Dashboard": "device1", "deviceID": "Device1"}]
        return render_template(
            "overview.html", title="Overview", user=user, devices=devices
        )

    else:
        return redirect("/login")


@app.route("/logout/<string:username>/<string:session>", methods=["GET", "POST"])
def logout(username, session):

    global logged_in

    if username in logged_in and (logged_in[username]["object"].session_id == session):
        logged_in.pop(username)
        # print("logged out")
        return redirect("/")
    else:
        return redirect("/login")


# mqtt




@mqtt_light.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt_light.subscribe('house/light')


@mqtt_fan.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt_fan.subscribe('house/fan')
    
@mqtt_hum.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt_hum.subscribe("house/hum")
    
    
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
  
    mqtt.subscribe("house/temp")





@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global temp_data
    temp_data = message.payload.decode()
    print(temp_data)

    with sqlite3.connect("user.sqlite") as con:

        query = "UPDATE Devices SET  temperature= ? WHERE username= ? "
        cur = con.cursor()
        cur.execute(query, (temp_data, "test"))


@mqtt_hum.on_message()
def handle_mqtt_message1(client, userdata, message):
    global hum_data
    hum_data = message.payload.decode()
    print(hum_data)
    data = dict(topic=message.topic, payload=message.payload.decode())
    with sqlite3.connect("user.sqlite") as con:

        query = "UPDATE Devices SET  humidity= ? WHERE username= ? "
        cur = con.cursor()
        cur.execute(query, (hum_data, "test"))


@mqtt_light.on_message()
def handle_mqtt_message_light(client, userdata, message):
    global light_data
    light_data = message.payload.decode()
    print(light_data)
    with sqlite3.connect("user.sqlite") as con:

        query = "UPDATE Devices SET  light= ? WHERE username= ? "
        cur = con.cursor()
        cur.execute(query, (light_data, "test"))


@mqtt_fan.on_message()
def handle_mqtt_message_fan(client, userdata, message):
    global fan_data
    fan_data = message.payload.decode()
    print(fan_data)
    with sqlite3.connect("user.sqlite") as con:

        query = "UPDATE Devices SET  fan= ? WHERE username= ? "
        cur = con.cursor()
        cur.execute(query, (fan_data, "test"))

# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#     print(level, buf)


# sensors data


def get_temperature(user):
    with sqlite3.connect("user.sqlite") as con:

        # query = "UPDATE Devices SET  temprature= ? WHERE username= ? "
        cur = con.cursor()
        query = "select temperature from Devices where username = '{}'".format(
            user)
        cur.execute(query)
        # randData = choice(randlist)
        temperature = cur.fetchall()
        print(temperature)
        temp = temperature[0][0]

        return temp


def get_fan(user):

    with sqlite3.connect("user.sqlite") as con:
        cur = con.cursor()
        query = "select fan from Devices where username = '{}'".format(user)
        cur.execute(query)

        fan = cur.fetchall()
        fa = fan[0][0]
        print(fan)
        return fa


def get_humidity(user):

    with sqlite3.connect("user.sqlite") as con:
        cur = con.cursor()
        query = "select humidity from Devices where username = '{}'".format(
            user)
        cur.execute(query)

        humidity = cur.fetchall()
        hum = humidity[0][0]

        return hum
    
# def get_ac(temp):
       
#       ac  = temp
#       return ac


@app.route("/api/<string:apikey>/light", methods=["GET", "POST"])
def get_light(user):
    with sqlite3.connect("user.sqlite") as con:
        cur = con.cursor()
        query = "select light from Devices where username = '{}'".format(user)
        cur.execute(query)

        light = cur.fetchall()
        li = light[0][0]

        return li


@app.route("/api/<string:user>/data/", methods=["GET", "POST"])
def data(user):
    temperature = get_temperature(user)
    fan = get_fan(user)
    light = get_light(user)
    humidity = get_humidity(user)

    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = {
        "temperature": temperature,
        "light": light,
        "humidity": humidity,
        "fan": fan,
      
        "time": time,
    }
    print(response)
    return response

AC = "off"

# chatbot
list1 = [
    "Hi",
    "hi",
    "hey",
    "How are you?",
    "Is anyone there?",
    "Hello",
    "Good day",
    "Whats up",
]
list2 = ["Hello!", "Good to see you again!", "Hi there, how can I help?"]


def task():
    print("here")
    # import time
    # time.sleep(1)
    return "here"


# def do_something():
#     get_bot_response()
#     return do_something_else()


@app.route("/set_temp")
def set_temp():
    return overview()


@app.route("/get")
# function for the bot response
def get_bot_response():

    userText = request.args.get("msg")

    usertext = userText.lower()

    if userText in list1:

        import random

        return random.choice(list2)

    elif "set" in userText:
        if "temperature" in userText:
            li = userText.split()
            print(li[-1])
            global temp2
            temp2 = li[-1]
            
            mqtt.publish("control/temp", str(temp2))
            with sqlite3.connect("user.sqlite") as con:

                query = "UPDATE Devices SET  temperature= ? WHERE username= ? "
                cur = con.cursor()
                cur.execute(query, (li[-1], "test"))

            return "temperature is {}".format(li[-1])
    elif "turn" in userText:
        if "light" in userText:
            li = userText.split()
            print(li[-2])
            mqtt.publish("control/light", str(li[-2]))
            with sqlite3.connect("user.sqlite") as con:

                query = "UPDATE Devices SET  light= ? WHERE username= ? "
                cur = con.cursor()
                cur.execute(query, (li[-2], "test"))

            return "light is now turned {}".format(li[-2])
        elif "fan" in userText:
            li = userText.split()
            print(li[-2])
            mqtt.publish("control/fan", str(li[-2]))
            with sqlite3.connect("user.sqlite") as con:

                query = "UPDATE Devices SET  fan= ? WHERE username= ? "
                cur = con.cursor()
                cur.execute(query, (li[-2], "test"))

            return "fan is now turned {}".format(li[-2])

    elif "temperature" in userText:
        temp = get_temperature("test")
        return str(temp)

    elif userText == "quit":
        if "download" in userText:
            pass  # do something
        elif "watch" in userText:
            pass  # do something else

    else:
        return "I did'nt get it "


if __name__ == "__main__":
    app.run(debug=True)
