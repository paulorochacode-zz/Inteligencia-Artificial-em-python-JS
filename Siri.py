# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3

l = ['Oi','Ola','Oi Siri','Ola Siri','Tudo e com você','Tudo e com voce','Estou bem obrigado','Siri','Qual seu nome','Quantos anos voce tem','Oque e voce','Tudo','Olá','Qual o seu nome']
dialogo = ''

path = './WebDriver/chromedriver.exe'
option = Options()

option.add_experimental_option("prefs", {\
    "profile.default_content_setting_values.media_stream_mic": 1
    })

option.headless = False;
driver = webdriver.Chrome(path,0,option)
driver.set_window_position(0,0)
driver.set_window_size(200,200) 

def falar(dialogo,):
    speak = pyttsx3.init('sapi5')
    speak.say(dialogo)
    speak.runAndWait()

def respostanula(res,):
    if res != l[0] :
        falar('Não entendi')
    elif res != l[1]:    
        falar('Não entendi')   
    elif res != l[2]:
        falar('Não entendi')        
    elif res != l[3]:
        falar('Não entendi')            
    elif res != l[4]:
        falar('Não entendi')                
    elif res != l[5]:
        falar('Não entendi')                    
    elif res != l[6]:
        falar('Não entendi')                        
    elif res != l[7]:
        falar('Não entendi')                            
    elif res != l[8]:                                
        falar('Não entendi')                                
    elif res != l[9]:                                    
        falar('Não entendi')                                    
    elif res != l[10]:                                        
        falar('Não entendi')
    elif res != l[11]:                                            
        falar('Não entendi')
    elif res != l[12]:                                            
        falar('Não entendi')
    elif res != l[13]:                                            
        falar('Não entendi')    

    else : 
        pass  

def resposta(dialogo, resposta, funcao):
    if funcao == None:
        if speech == dialogo :
            falar(resposta)
    else:
        os.system('funcao')        
        if speech == dialogo :
                falar(resposta)



def recognition(language):
    
    engine = os.getcwd() + '/Engines/' + str(language) + '.html'  
    driver.get(engine)
    time.sleep(5)

    while True:
        speech = driver.find_element_by_id("resultSpeak").text

        if speech != 'error' and speech != 'on' and speech != '':
            return speech

while True:
    speech = recognition('pt-BR')
    print(speech)
    
    resposta(l[0],'oi,tudo bem?',None)
    resposta(l[1],'oi,tudo bem?',None)
    resposta(l[2],'oi,tudo bem?',None)
    resposta(l[3],'oi,tudo bem?',None)
    resposta(l[4],'tudo bem, obrigado',None)
    resposta(l[5],'Estou bem obrigado',None)
    resposta(l[6],'Estou bem obrigado',None)
    resposta(l[7],'Olá,como posso ajuda-lo',None)
    resposta(l[8],'Meu nome é Siri',None)
    resposta(l[9],'Fui desenvolvida em dezenove do cinco de dois mil e vinte',None)
    resposta(l[10],'Que bom, como posso ajuda-lo',None)
    resposta(l[11],'Que bom, como posso ajuda-lo',None)
    resposta(l[12],'oi,tudo bem?',None)
    resposta(l[13],'Meu nome é Siri',None)
    respostanula(speech)

    
    #if speech == "Oi" :
     #   print('##############')
     #   falar('oi, tudo bem?')

