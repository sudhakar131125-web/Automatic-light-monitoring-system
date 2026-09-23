import network
import time
import urequests
from machine import ADC, Pin

# WiFi
SSID = "Wokwi-GUEST"
PASSWORD = ""

# ThingSpeak Write API Key
API_KEY = "YOUR_WRITE_API_KEY"

# LDR sensor
ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

# Connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

print("Connecting to WiFi...")

wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(1)

print("WiFi Connected!")
print(wifi.ifconfig())

# Send data to ThingSpeak
while True:

    light_value = ldr.read()

    print("Light:", light_value)

    url = "https://api.thingspeak.com/update?api_key=" + API_KEY + "&field1=" + str(light_value)

    try:
        response = urequests.get(url)

        print("ThingSpeak Response:", response.text)

        response.close()

    except Exception as e:
        print("Error:", e)

    time.sleep(15)
