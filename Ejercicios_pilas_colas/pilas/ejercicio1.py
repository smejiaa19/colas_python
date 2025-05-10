'''
Una oficina de atención ciudadana en una alcaldía municipal en Nicaragua 
recibe documentos para revisión. Por cada solicitud, se apilan los documentos 
entregados en el orden en que llegan. El personal debe revisar el último documento
entregado primero. Se debe simular el proceso de revisión, utilizando una pila, 
y permitir agregar nuevos documentos, eliminar el último revisado 
y mostrar los pendientes.
'''

class oficina:
    
    def __init__(self):
        self.documentos = []
    
    def agregar_documentos(self):
        n = int(input('Cuantos documentos desea agregar: '))
        for i in range(n):
            self.documento = input(f'Ingrese el nombre del documento: {i+1}' '\n')
            self.documentos.append(self.documento)
            
    def mostrar_pila(self):
        print('Documentos pendientes: ')
        for i in range(len(self.documentos)):
            print(f'Documento {i+1} - {self.documentos[i]}')     
        
    def eliminar_documentos(self):
        if len(self.documentos) == 0:
            print('No hay documentos para eliminar')
        else: 
            print('Cuantos documentos desea eliminar: ')
            n = int(input())
            if n > len(self.documentos):
                print('No hay suficientes documentos para eliminar')
            else:
                for i in range(n):
                    self.documentos.pop()
                print(f'Documentos restantes: {self.documentos}')
        
new_oficina = oficina()
new_oficina.agregar_documentos()
new_oficina.mostrar_pila()
new_oficina.eliminar_documentos()