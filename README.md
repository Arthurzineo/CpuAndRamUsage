# CpuAndRamUsage
MVP do Software

Software tem a ideia de fazer a coleta e futuramente analise de parametros de ram e cpu, por um X periodo.

Com isso temos a espectativa de ter uma maneira facil de fazer uma avaliação de quando um usuario precisa de um Upgrade em seu computador. 

# :hammer: Funcionalidades do projeto

- `Funcionalidade 1`: Monitorar o uso de memoria ram em %.
- `Funcionalidade 2`: Monitorar o uso de CPU em %.
- `Funcionalidade 3`: Criar um grafico para mostrar o uso de memoria ram.
- `Funcionalidade 4`: Criação de CSV com as informações.
#
# ⚒️ Aprimoramentos futuros

- `Aprimoramento futuro 1`: criar um algoritmo para calcular e gerar estatisticas sobre o uso de ram.
- `Aprimoramento futuro 2`: Usar o pyinstaller para fazer um .exe da aplicação completa
- `Aprimoramento futuro 3`: Criação de uma interface grafica para escolher o tempo total e o tempo de intervalo do monitoramento.
-  `Aprimoramento futuro 4`: Salvar os programas com mais uso de ram ou cpu no momento da coleta.


# ✅ Como Fazer para testar essa versão do Software? 
  Recomendamos a versão 3.11.3 do Python porem acredito que funcione em qualquer versão do Python 3.
  
  (Testes realizados apenas em Windows 10 e 11).
  
  (Não compativel com sistemas linux).

  As Bibliotecas que precisam estar instaladas são: 

  import psutil

  import os

  import csv

  import datetime

  import time

  import matplotlib.pyplot as plt

  Por padrão algumas delas já vem instaladas.

  Recomendo o PIP para instalar.

  pip install psutil 

  pip install matplotlib

# ⚙️ Variaveis que podem ser ajustadas no programa:
Dentro de def TempoDeExecucao(): a variavel  TempoDeAnalise determina em segundos o tempo total que a aplicação vai ficar rodando no computador. 

Dentro de def IniciarColeta(): a variavel TempoEntreColetasEmSegundo determina o intervalo entre as coletas das informações ( recomendo deixar em 60, assim fica mais facil visualizar o grafico).

# 📈 Executar o codigo:
Depois de definir as veriaveis no codigo, executar o codigo. 

Nada vai aparentemente acontecer, depois do tempo total escolhido um grafico vai aparecer na tela com as informações. 
Exemplo abaixo: (executado por 3 minutos e com intervalo de 1 minuto.) 

![image](https://github.com/Arthurzineo/CpuAndRamUsage/assets/78982690/4fc04ec0-4493-4a07-8cd6-0366acef442d)

E por fim na pasta raiz da execução vai ser criado um arquivo chamado Coleta.csv que contem todas informações coletadas. 
Exemplo do CSV:

![image](https://github.com/Arthurzineo/CpuAndRamUsage/assets/78982690/e15d675f-d1a9-4fc1-a072-cfd87b66c053)

Atenção ao uso de CPU que esta em uma escala difente 0.4 = 4%, 10.0 = 100%.





  



