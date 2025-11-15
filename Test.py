
from GreenHouse import Climatecontrol
from GreenHouse.Climatecontrol import Climatecontrol
from GreenHouse.Farm import Farm

try:
    # Create Climate sensor
    try:
        sensor = Climatecontrol()
        print("Climate sensor initialized successfully.")
        print("Temperature:", sensor.temperature)
        print("Humidity:", sensor.humidity)
        print("Light:", sensor.lightIntensity)
        print("CO2:", sensor.co2)
        print("Soil Moisture:", sensor.soilMoisture)

    except Exception as e:
        print("Error initializing climate sensor:", e)

    # Create Farm
    try:
        farm = Farm(2, 5)
        print("Farm created successfully:")
        farm.display()

    except Exception as e:
        print("Error creating farm:", e)

except Exception as e:
    # Fallback for any unexpected error
    print("An unexpected error occurred:", e)