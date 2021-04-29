import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from bug import ContBug

x = 1
cb = ContBug()

while x == 1:
    sprint = int(input("Digite a sprint na qual os bugs foram detectados: "))
    if sprint not in [1, 2, 3, 4]:
        print('Sprint inválida!')
        continue
    data = (input("Digite a data na qual os bugs foram detectados: "))
    data_f = "{}/{}/{}".format(data[0:2], data[2:4], data[4:8])
    bug = int(input("Digite quantos bugs foram detectados nessa data e sprint: "))
    ContBug.contador_bugs(cb, bug, sprint)
    ContBug.registros_bugs(cb, bug, data_f, sprint)
    x = int(input("Deseja registrar mais Bugs? 1 para sim, 0 para não "))


excel = pd.DataFrame(ContBug.registro_final(cb), columns=['Sprint', 'Total de bugs', 'Registros'])
excel.to_excel("contador-de-bugs.xlsx", index=False)
graf = pd.read_excel(r"C:\Python\TraineeI9\contador-de-bugs.xlsx")   # endereço de onde a planilha foi salva (mesmo lugar onde o arquivo do codigo está)
plt.plot(graf['Sprint'], graf['Total de bugs'])
plt.title('Relatorio de Bugs detectados no projeto')
plt.savefig('relatorio-bugs.png')
plt.show()
