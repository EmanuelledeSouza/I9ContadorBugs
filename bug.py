class ContBug:
    def __init__(self):
        self.lista = []
        self.listas1 = ['Sprint 1']
        self.listas2 = ['Sprint 2']
        self.listas3 = ['Sprint 3']
        self.listas4 = ['Sprint 4']
        self.datas1 = []
        self.datas2 = []
        self.datas3 = []
        self.datas4 = []
        self.bugs1 = 0
        self.bugs2 = 0
        self.bugs3 = 0
        self.bugs4 = 0

    def contador_bugs(self, bug, sprint):
        if sprint == 1:
            self.bugs1 += bug
            print(self.bugs1)
        elif sprint == 2:
            self.bugs2 += bug
            print(self.bugs2)
        elif sprint == 3:
            self.bugs3 += bug
            print(self.bugs3)
        elif sprint == 4:
            self.bugs4 += bug
            print(self.bugs4)

    def registros_bugs(self, bug, data, sprint):
        registro = [f'Data:{data}', f'Número de bugs:{bug}']
        if sprint == 1:
            self.datas1.append(registro)
            print(self.datas1)
        elif sprint == 2:
            self.datas2.append(registro)
            print(self.datas2)
        elif sprint == 3:
            self.datas3.append(registro)
            print(self.datas3)
        elif sprint == 4:
            self.datas4.append(registro)
            print(self.datas4)

    def registro_final(self):
        self.listas1.append(self.bugs1)
        self.listas1.append(self.datas1)
        self.listas2.append(self.bugs2)
        self.listas2.append(self.datas2)
        self.listas3.append(self.bugs3)
        self.listas3.append(self.datas3)
        self.listas4.append(self.bugs4)
        self.listas4.append(self.datas4)
        self.lista.append(self.listas1)
        self.lista.append(self.listas2)
        self.lista.append(self.listas3)
        self.lista.append(self.listas4)
        lista = self.lista
        return lista
