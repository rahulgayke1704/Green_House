
import random
class Climatecontrol:
    def __init__(self):
        self.temperature = round(random.uniform(0, 150), 1)
        self.humidity = round(random.uniform(0, 100), 1)
        self.lightIntensity = round(random.uniform(0, 9999), 1)
        self.co2 = round(random.uniform(300, 2300), 1)
        self.soilMoisture = round(random.uniform(0, 100), 1)
        self.temperature = 25  
        print("Climate sensor initialized successfully.")

        
    def display(self): 
        return f"T={self.temperature:.1f}°C  H={self.humidity:.1f}%  L={self.lightIntensity:.0f} Lux  CO₂={self.co2:.0f} ppm  SM={self.soilMoisture:.1f}%"


    def _str_(self):
        return self.display()