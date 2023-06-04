import psutil
import os
import csv
import datetime
import time
import matplotlib.pyplot as plt
#######################################

def PegarHorario():
    horario_atual = datetime.datetime.now()
    horario_formatado = horario_atual.strftime(' %H:%M')
    return horario_formatado

def PegarPorcentagemRAM():
     RamUsagePorcentage = psutil.virtual_memory()[2]
     return RamUsagePorcentage

def PegarQuantidadeDeRamUltilizada():
     RamUsageGB = (psutil.virtual_memory()[3])/1000000000
     return RamUsageGB

def PegarUsoDeCPU():
     CpuUsagePorcentage = psutil.cpu_percent(1)
     return CpuUsagePorcentage

def TempoDeExecucao():
     ## converteHorasSegundo é a variavel para colocar os segundos de tempo de execução total do programa exemplo 3600 = 3 horas
     TempoDeAnalise = 180
     return TempoDeAnalise

def IniciarColeta():
     with open('Coleta.csv', 'w', newline='') as csvfile:
          #selecione na var abaixo os segundos entre cada coleta
          TempoEntreColetasEmSegundo = 60
          fieldnames = ['Horario','% De RAM', 'GB RAM', '% De CPU']
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
          writer.writeheader()
          TempoDeColeta = TempoDeExecucao()
          while TempoDeColeta>0:
               Horario = PegarHorario()
               RamUsagePorcentage = PegarPorcentagemRAM()
               RamUsageGB = PegarQuantidadeDeRamUltilizada()
               CpuUsagePorcentage = PegarUsoDeCPU()
               writer.writerow({'Horario':Horario,'% De RAM': RamUsagePorcentage, 'GB RAM': RamUsageGB, '% De CPU': CpuUsagePorcentage})
               time.sleep(TempoEntreColetasEmSegundo)
               TempoDeColeta = TempoDeColeta - TempoEntreColetasEmSegundo  
     CriarGrafico()

def CriarGrafico():
     vetor = []
     with open('Coleta.csv', newline='') as csvfile:
               # cria um objeto reader
          reader = csv.reader(csvfile, delimiter=',', quotechar='"')
          next(reader)
          for row in reader:

               vetor.append(float(row[1]))
     vetorMinutosTamanho = len(vetor)
     vetorMinutosINT = range(1, vetorMinutosTamanho+1)
     vetorMinutos = [str(i) for i in vetorMinutosINT]
     plt.plot(vetorMinutos,vetor,'k--')
     plt.plot(vetorMinutos,vetor,'go')
     plt.gcf().autofmt_xdate() 
     plt.show()



#######################################

def Main():
     IniciarColeta()

if __name__ == "__main__":
     Main()
