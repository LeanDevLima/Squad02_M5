from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
import time
import mouse

navegador = Firefox()
navegador.get("https://web.whatsapp.com/")

input("Faça o login no WhatsApp Web e pressione Enter após a conclusão...")

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

sleep(3)

grupo_nome = "[3] IJJ - BUGOU? QA TÁ ON!"
campo_pesquisa = navegador.find_element(By.XPATH, "//div[@contenteditable='true']")
campo_pesquisa.send_keys(grupo_nome)

sleep(3)

resultado_grupo = navegador.find_element(By.XPATH, f"//span[@title='{grupo_nome}']")
resultado_grupo.click()

sleep(5)

mensagem = "Automação do WhatsApp - Leanderson - Atividade 8 - Squad02 - TESTE1."

time.sleep(2)
mouse.move(690, 900, absolute=True, duration=0.1)
mouse.click('left')
time.sleep(1)

pyautogui.write(mensagem)
pyautogui.press('enter')

sleep(5)

navegador.quit()
