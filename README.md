# CpuAndRamUsage

MVP do Software

Software tem a ideia de fazer a coleta e futuramente análise de parâmetros de RAM e CPU, por um X período.

Com isso, temos a expectativa de ter uma maneira fácil de fazer uma avaliação de quando um usuário precisa de um upgrade em seu computador.

## Funcionalidades do projeto

- `Funcionalidade 1`: Monitorar o uso de memória RAM em %.
- `Funcionalidade 2`: Monitorar o uso de CPU em %.
- `Funcionalidade 3`: Criar um gráfico para mostrar o uso de memória RAM.
- `Funcionalidade 4`: Criação de um arquivo CSV com as informações.

## Aprimoramentos futuros

- `Aprimoramento futuro 1`: criar um algoritmo para calcular e gerar estatísticas sobre o uso de RAM.
- `Aprimoramento futuro 2`: Usar o pyinstaller para criar um executável da aplicação completa.
- `Aprimoramento futuro 3`: Criação de uma interface gráfica para escolher o tempo total e o intervalo de monitoramento.
- `Aprimoramento futuro 4`: Salvar os programas com maior uso de RAM ou CPU no momento da coleta.

## Como Fazer para testar essa versão do Software?

Recomendamos a versão 3.11.3 do Python, porém acredito que funcione em qualquer versão do Python 3.

(Testes realizados apenas em Windows 10 e 11).

(Não compatível com sistemas Linux).

As bibliotecas que precisam estar instaladas são:

- `psutil`
- `os`
- `csv`
- `datetime`
- `time`
- `matplotlib.pyplot`

Por padrão, algumas delas já vêm instaladas.

Recomendo o PIP para instalar:

pip install psutil
pip install matplotlib


## Variáveis que podem ser ajustadas no programa

Dentro de `def TempoDeExecucao()`, a variável `TempoDeAnalise` determina, em segundos, o tempo total que a aplicação vai ficar rodando no computador.

Dentro de `def IniciarColeta()`, a variável `TempoEntreColetasEmSegundo` determina o intervalo entre as coletas das informações (recomendo deixar em 60, assim fica mais fácil visualizar o gráfico).

## Executar o código

Depois de definir as variáveis no código, execute-o. Nada aparentemente acontecerá. Após o tempo total escolhido, um gráfico será exibido na tela com as informações.

Exemplo abaixo (executado por 3 minutos e com intervalo de 1 minuto):

![image](https://github.com/Arthurzineo/CpuAndRamUsage/assets/78982690/4fc04ec0-4493-4a07-8cd6-0366acef442d)

Por fim, na pasta raiz da execução, será criado um arquivo chamado `Coleta.csv`, que contém todas as informações coletadas.




  



