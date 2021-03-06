- [raeros_ledbutton](#raeros_ledbutton)
- [Instructions](#instructions)
  - [Installation](#installation)
  - [Set perception system](#set-perception-system)
  - [Start the server](#start-the-server)
  - [Control via the client](#control-via-the-client)
  - [LED](#led)
    - [On and off](#on-and-off)
    - [Blink](#blink)
    - [Heartbeat pattern](#heartbeat-pattern)
  - [Button](#button)
    - [Read current state](#read-current-state)
    - [Register event](#register-event)
      - [Onpress](#onpress)
      - [Onrelease](#onrelease)

# raeros_ledbutton
This repository contains ros based drivers to control a button with integrated led.
The used button can be ordered here: [conrad.de/ledbutton](https://www.conrad.de/de/p/tru-components-gq16f-10e-j-b-12v-vandalismusgeschuetzter-drucktaster-48-v-dc-2-a-1-x-aus-ein-ip65-tastend-1-st-701855.html?refresh=true#attributesNotes_delivery)

<p align="center">
<img style="margin-left: auto;" src="https://asset.conrad.com/media10/isa/160267/c1/-/de/701855_BB_00_FB/tru-components-gq16f-10e-j-b-12v-vandalismusgeschuetzter-drucktaster-48-v-dc-2-a-1-x-aus-ein-ip65-tastend-1-st.jpg" width="25%">
</p>

# Instructions
## Installation
Clone the repository inside your workspace and build it:
```bash
cd ~/catkin_ws/src &&
git clone https://github.com/romzn/raeros_ledbutton.git &&
cd .. &&
catkin_make
```
## Set perception system
Because the realsense case has one an the kinect case has two led-buttons you have to set an parameter which decides how many servers are started- Set either __realsense__ or __kinect__ as `perception_system` parameter inside the `system.launch` of the `raeros_system` package. Realsense is set as default.

## Start the server
```bash
roslaunch rae_ledbutton_server server.launch
```
> This launch file is also in the `system.launch` from the `raeros_system` package integrated

## Control via the client
The script `scripts/example.py` guides you through the available commands to control the led and read button states. First you have to turn on the server and then you can run the script directly or via rosorun.

```bash
rosrun rae_ledbutton_client example.py
```

Before you can send any commands to the server via the python client you have to create an object.

```python
from raerospy_ledbutton_client import LedButtonClient
lb = LedButtonClient()
```

## LED
### On and off
The following command turns the led on.
```python
lb.led_on()
```

You can also specify the intensity which enables you to dimm the led. The default value is 100.
```python
lb.led_on(intensity=10)
```

Turn the Led off with
```python
lb.led_off()
```

### Blink
The command `lb.blink()` lets the led blink, 7 Times with a frequency of 7 Hz.

You also can specify the frequency an the number of blinks:

```python
lb.blink(freq=17,cnt=17)
```

If you want blink permanently you have to use the `lb.blink_on()` function which takes the frequency as parameter. Default is 7 Hz.

```python
lb.blink_on(freq=17)
```
And turn it off with:

```python
lb.blink_off()
```
### Heartbeat pattern
You can start an **realistic** heartbeat pattern with the `lb.hearbeat_on()` functions. With the `speed` parameter you can specify how fast the heartbeat pattern runs. Default is 50 and ranges from 0-100. `lb.heartbeat_off()` turns the heartbeat off.

```python
lb.hearbeat_on(speed=100)
time.sleep(10)
lb.set_hearbeat_speed(7)
time.sleep(10)
lb.heartbeat_off()
```

## Button

### Read current state
The `lb.button_state()` returns the current state of the button. If pressed the function will return 1 otherwise  0.

```python
lb.button_state() 
```

### Register event
For an event-based communication you need to register a function which will be called if the event occurs. Here the examples for the `onpress` or `onrelease` function

#### Onpress
```python
def onpress():
    print("onpress:event")

lb.register_press_event(onpress)
```

#### Onrelease
```python
def onrelease():
    print("onrelease:event")

lb.register_release_event(release)
```
