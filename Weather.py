import requests
import json
import pyttsx3
import speech_recognition as sr

def ouvi_microphone():
# obtain audio from the microphone
    microphone = sr.Recognizer()

    with sr.Microphone() as source:  
      microphone.adjust_for_ambient_noise(source)
      
      print("Diga a cidade para a qual deseja obter informações meteorológicas: ")
    
      audio = microphone.listen(source)   
    try:
       
       frase = microphone.recognize_google(audio,language='pt-br')
       print(frase)
    except sr.UnknownValueError: 
        print("Não entendi")
    
    # Faça uma solicitação à API OpenWeatherMap para obter as informações
    api_key = "e19bcae1082079012dd2d847cb3f2b50" #chave da api
#link para fazer a busca
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={frase}&appid={api_key}"
#pega a informação retornada da url 
    response = requests.get(weather_url)

# Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
    # Se a solicitação foi bem-sucedida, analise os dados JSON
     weather_data = json.loads(response.text)
     main_data = weather_data["main"]
     temperature_kelvin = main_data["temp"]
    #faz a conversão da temperatura para Celsius
     temperature_celsius = temperature_kelvin - 273.16
     print(f"A temperatura em {frase} é de {temperature_celsius:.0f}°C")
    #pyttsx3 retora por audio a tempertura
     engine = pyttsx3.init()
     engine.say(f"A temperatura em {frase} é de {temperature_celsius:.0f}°C")
     engine.runAndWait()
    else:
     # Se a solicitação não for bem-sucedida, imprima uma mensagem de erro
     print("Ocorreu um erro ao obter as informações meteorológicas.")
     engine = pyttsx3.init()
     engine.say("Ocorreu um erro ao obter as informações meteorológicas.")
     engine.runAndWait()
      
ouvi_microphone()       
