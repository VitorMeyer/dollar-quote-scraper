import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
print(requisicao)
site = BeautifulSoup(requisicao.text,"html.parser")
#print(site.prettify())
title = site.find("title")
print(title)

pesquisa = site.find_all("input")
print("pesquisa por posição: ",pesquisa)
print("________________________________")
pesquisa2 = site.find("span", class_="SwHCTb")
print(pesquisa2.get_text())