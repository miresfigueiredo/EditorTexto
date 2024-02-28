class Editor_texto:
    def __init__(self):  
        self._texto = ""
        self._historico = []

    def escrever(self, texto):
        self._historico.append(self._texto)
        self._texto += texto

    def desfazer(self):
        if self._historico:
            self._texto = self._historico.pop()
        else:
            print("Não há nada para desfazer")
    
    def mostrar(self):
          print(f"Texto: {self._texto}")
    
    def mostrar_historico(self):
        print(f"Histórico: {self._historico}")

editor = Editor_texto()
editor.escrever("Bem-vindos, usuários! ")
editor.mostrar() 

editor.escrever("Este é um editor de texto. ")
editor.mostrar() 

editor.desfazer()
editor.mostrar()  

editor.mostrar_historico()

editor.desfazer()