from selenium import webdriver

# Caminho para o ChromeDriver (altere para o caminho correto)
CHROME_DRIVER_PATH = '/home/link/Documentos/git/lotocerta/chromedriver'

# Configurar o ChromeDriver e abrir o navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Para executar em modo "headless" (sem interface gráfica)
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

# Acessar o site desejado
url = 'https://www.exemplo.com'
driver.get(url)

# Agora você pode usar o objeto "driver" para interagir com o site e extrair informações usando o Selenium
# Por exemplo, para obter o título da página:
title = driver.title
print('Título da página:', title)

# Fechar o navegador
driver.quit()
