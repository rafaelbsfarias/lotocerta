import requests
import time

base_url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/"
concurso_num = 1  # Número inicial do concurso

while True:
    try:
        url = base_url + str(concurso_num)  # Construir a URL com o número do concurso
        response = requests.get(url)
        response.raise_for_status()  # Verifica se ocorreu algum erro na resposta
        data = response.json()

        # Imprimir os dados da chave "data"
  
       
        print("Dezenas:", data["dezenas"]) 

        # E assim por diante...

        concurso_num += 1  # Incrementar o número do concurso

    except requests.exceptions.RequestException as e:
        print("Erro na chamada à API:", e)

    # Pausa de 5 segundos antes de fazer a próxima chamada
    time.sleep(5)
