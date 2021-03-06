# GATEWAY_RUUVI_MQTT
Gateway between Ruuvi and MQTT, {over Raspberry PI 3}

### Requirements

* RuuviTag with Weather Station firmware
    * Setup [guide](https://ruu.vi/setup/)
    * Supports [Data Format 2, 3, 4 and 5](https://github.com/ruuvi/ruuvi-sensor-protocols)
* Python 2.7 and 3
    * psutil
        * Package uses psutil to start and stop processes. Psutil requires `sudo apt-get install python-dev python-psutil` or `sudo apt-get install python3-dev python3-psutil`
* Linux
    * Package's Windows and OSX supports are only for testing and url decoding
* Bluez
    * `sudo apt-get install bluez bluez-hcidump`
    * Package uses internally hciconfig, hcitool and hcidump. These tools are deprecated. In case tools are missing, older version of Bluez is required ([Issue](https://github.com/ttu/ruuvitag-sensor/issues/31))
* Superuser rights
    * BlueZ tools require superuser rights
* PAHO MQTT
    * `pip3 install paho-mqtt`
    
### Installation

Install latest released version
```sh
$ pip install ruuvitag_sensor
```

Install latest developement version
```sh
$ pip install git+https://github.com/ttu/ruuvitag-sensor
# Or clone this repository and install locally
$ pip install -e .
```

Full installation guide for [Raspberry PI & Raspbian](https://github.com/ttu/ruuvitag-sensor/blob/master/install_guide_pi.md)

### First run

* Clone from git:
   * `git clone https://github.com/drvrh/GATEWAY_RUUVI_MQTT.git`
* `cd GATEWAY_RUUVI_MQTT`   
* `nano test3.py`
* Edit file, with your RUUVI MAC address and IP of your MQTT broker
* `python3 test3.py`

### TO DO:
1. Multiple publish all data from RUUVI
2. Use multiple RUUVI at once Gateway
3. Update simple MQTT with secure MQTT (username, password and SSL)
### 4. ... please commit and make live this code :D
