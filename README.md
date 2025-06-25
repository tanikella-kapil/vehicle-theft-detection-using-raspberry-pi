# 🚗 Vehicle Security System with Real-Time Intrusion Alerts

A Raspberry Pi-based embedded system that monitors for intrusions using IR sensors and sends instant SMS alerts via a GSM module. Built for smart vehicle protection.

---

## 🔧 Features

- 📡 **Intrusion Detection** using IR sensors.
- 📲 **Instant Alerts** via GSM module (SMS within 10 seconds).
- 🧠 **Interrupt-driven** event handling for low-latency response.
- 🛠️ Modular code with clear GPIO pin mapping and logging.

---

## 🧰 Tech Stack

- **Hardware:**
  - Raspberry Pi 4
  - IR Sensors (Digital Output)
  - GSM Module (SIM800L or equivalent)
  - Jumper Wires, Breadboard/PCB

- **Software & Tools:**
  - Python 3
  - GPIO Library (`RPi.GPIO`)
  - Serial Communication (`pySerial`)
  - UART & I2C protocols
  - Crontab (optional: for autorun on boot)

---

## ⚙️ Circuit Diagram

 IR SENSOR ] ----> [ GPIO Pin - Interrupt ]
[ GSM TX ] --------> [ Raspberry Pi RX ]
[ GSM RX ] --------> [ Raspberry Pi TX ]
[ GND + VCC Connections ]
## 🚀 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/tanikella-kapil/vehicle-theft-detection-using-raspberry-pi.git
cd vehicle-theft-detection-using-raspberry-pi
### install dependancies
pip install pyserial RPi.GPIO

3. Connect Hardware
Ensure:

IR sensor is connected to a GPIO pin with interrupt capability (e.g., GPIO17).

GSM module is connected to UART pins (TX/RX).

Power supply is stable (especially for GSM module).

4. Run the Script
