import math

while True:    
   temperature = input("Enter temperature (°C): ")

   try:
       temperature = float(temperature)

       if math.isfinite(temperature) and -50 <= temperature <= 60:
           break

       else:
           print("Temperature must be between -50 and 60°C.")
               
       
   except ValueError:
       print("Please enter a valid number.")


while True:  
   humidity = input("Enter humidity (%): ")

   try:
       humidity = float(humidity)
       
       
       
       if math.isfinite(humidity) and 0 <= humidity <= 100:
        break
   
       else:
           print("Humidity must be between 0 and 100.")
     
   
   except ValueError:
       print("Please enter a valid number.")


while True:
   light = input("Enter light level (%): ")

   try:
       light = float(light)
       
       if math.isfinite(light) and 0<= light <= 100:
        break
   
       else:
           print("Light level must be between 0 and 100.")


   except ValueError:
       print("Please enter a valid number.")


while True:
   air_quality = input("Enter air quality (AQI): ")

   try:
       air_quality = float(air_quality)
       
       if math.isfinite(air_quality) and air_quality >= 0:
        break

       else:
           print("Air quality index cannot be negative.")

           
   except ValueError:
       print("Please enter a valid number.")


while True:
   noise = input("Enter noise level (dB): ")

   try:
       noise = float(noise)
       
       if math.isfinite(noise) and 0<= noise <= 200:
           break
       
       else:
           print('Noise level must be between 0 and 200 dB.')
       
       
   except ValueError:
       print("Please enter a valid number.")


attention_count = 0
recommendations = [] 

print("\n=== Environmental Analysis ===")

if temperature < 20:
    print("Temperature: Cold")
    recommendations.append("Increase the temperature if possible.")
    attention_count += 1

elif temperature <= 28:
    print("Temperature: Comfortable")

else:
    print("Temperature: Warm")
    recommendations.append("Cool the environment if possible.")
    attention_count += 1     



if humidity < 40:
    print("Humidity: Dry")
    recommendations.append("Increase the humidity if possible.")
    attention_count += 1   

elif humidity <= 60:
    print("Humidity: Comfortable")

else:
    print("Humidity: Humid")
    recommendations.append("Reduce the humidity if possible.")
    attention_count += 1   



if light <= 30:
    print("Light: Low")
    recommendations.append("Increase the light level if possible.")
    attention_count += 1

elif light <= 60:
    print("Light: Moderate")

else:
    print("Light: Bright")
    recommendations.append("Reduce the light level if possible.")
    attention_count += 1   



if air_quality <= 50:
    print("Air Quality: Good")  

elif air_quality <= 100:
    print("Air Quality: Moderate")
    recommendations.append("Improve the ventilation if possible.")
    attention_count += 1

else:
    print("Air Quality: Poor")
    recommendations.append("Improve air quality and avoid polluted areas if possible.")
    attention_count += 1



if noise <= 40:
    print("Noise: Quiet")
    
elif noise <= 70:
    print("Noise: Moderate")
    recommendations.append("Reduce the noise level if possible.")
    attention_count += 1    

else:
    print("Noise: Loud")
    recommendations.append("Move to a quieter area if possible.")
    attention_count += 1


print("\n=== Recommendations ===")

if recommendations:
    for recommendation in recommendations:
        print("- " + recommendation)

else:
    print("No recommendations. Environment is in good condition.")
if attention_count == 0:
    print("Overall Environment: Good")

elif attention_count <= 2:
    print("Overall Environment: Needs Attention")

else:
    print("Overall Environment: Poor")