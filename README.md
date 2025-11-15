# 🌱 GreenHouse Climate Control & Farm Simulation

A Python project that simulates a **digital greenhouse** with climate sensors and a farm grid.  
It demonstrates **Object-Oriented Programming (OOP)** concepts like classes, inheritance, encapsulation, and modular design.

---

## 🚀 Features
- **Climatecontrol class**  
  - Generates random sensor values: Temperature, Humidity, Light Intensity, CO₂, Soil Moisture.  
  - Provides a `display()` method to show sensor readings neatly.  

- **Farm class**  
  - Creates a grid of greenhouses (rows × columns).  
  - Each greenhouse has its own climate sensor.  
  - Displays sensor data for the entire farm in tabular format.

---

## 📂 Project Structure

---

## 🛠️ Installation & Usage
Clone the repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

#outPut

Climate sensor initialized successfully.
Temperature: 25.0
Humidity: 45.6
Light: 345 Lux
CO2: 1200 ppm
Soil Moisture: 67.8 %

Farm created successfully:
[R1C1] T=34.5°C H=56.7% L=123 Lux CO₂=1500ppm SM=45.6%   [R1C2] ...
...
