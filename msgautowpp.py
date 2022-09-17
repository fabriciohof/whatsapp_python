#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyautogui
import time
import pywhatkit as kit

#Mensagem de alerta
pyautogui.alert("O computador será usado pelo python,não mexa em nenhuma tecla")

#Comando para pausar  e ir para o próximo
pyautogui.PAUSE = 1

#comando para clicar na tecla windows
pyautogui.press("winleft")

#comando para escrever
pyautogui.write("chrome")
pyautogui.press("enter")

#esperar 1 segundo antes de digitar o próximo comando
time.sleep(1)

#abrindo o wpp

kit.sendwhatmsg("+5521998958575","Olá tudo bem? ",19,44)



#comando para combinação de teclas
# pyautogui.hotkey("winleft","d")






# In[ ]:




