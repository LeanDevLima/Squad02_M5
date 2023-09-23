# source pvenv/Scripts/activate

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

navegador = Firefox()

url = "https://www.google.com/"

navegador.get(url)

barra_de_pesquisa = navegador.find_element(By.NAME, "q")
barra_de_pesquisa.click()
barra_de_pesquisa.send_keys("Instituto Joga Junto")
barra_de_pesquisa.send_keys(Keys.RETURN)

sleep(5)

elemento = navegador.find_element(By.XPATH, "//h3[text()='Instituto Joga Junto']")
elemento.click()

sleep(5)

elemento_contato = navegador.find_element(By.XPATH, "//a[@href='/#Contato']")
elemento_contato.click()

sleep(5)

elemento_nome = navegador.find_element(By.ID, "nome")
elemento_nome.send_keys("Leanderson")
elemento_nome = navegador.find_element(By.ID, "email")
elemento_nome.send_keys("leanderson.devlima@gmail.com")

elemento_assunto = navegador.find_element(By.ID, "assunto")
selecionar = Select(elemento_assunto)
selecionar.select_by_value("Ser facilitador")

elemento_nome = navegador.find_element(By.ID, "mensagem")
elemento_nome.send_keys("Até seria legal ser facilitador, mas esse é o meu primeiro script de automação - LEANDERSON DA SQUAD 02")

sleep(5)

botao_enviar = navegador.find_element(By.XPATH, "//button[@type='submit']/p[text()='Enviar']")
botao_enviar.click()

sleep(5)

navegador.quit()
