class Aluno:
    nome : str
    id : str
    idade : int

    def __init__(self,nome : str, id : str, idade : int):
        self.nome = nome
        self.id = id
        self.idade = idade

    def procuraPorId(lista,idProcurado):
        for alunos in lista:
            if alunos.id == idProcurado:
                return print(f"Aluno encontrado!!\nNome: {alunos.nome} | Id: {alunos.id} | Idade: {alunos.idade}")
        return print("Aluno não encontrado!!")


