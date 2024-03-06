from trabalhoBdD.Aluno import Aluno

saida = 1
while saida!=0:
    listaDeAlunos = []
    numeroDeAlunos = int(input("Digite o numero de alunos:"))
    contador = 1

    while contador <= numeroDeAlunos:
        print(f"Aluno nº {contador}")
        listaDeAlunos.append(Aluno(str(input("Digite o nome do aluno: ")), str(input("Digite o ID do aluno: ")), int(input("Digite a idade do aluno: "))))
        contador += 1

    contador = 1
    print("Alunos | Nome | ID | Idade")
    for alunos in listaDeAlunos:
        print(f"{contador} | {alunos.nome} | {alunos.id} | {alunos.idade}")
        contador += 1

    while saida != 0:
        idProcurado = str(input("Digite o id que deseja procurar: "))
        Aluno.procuraPorId(listaDeAlunos,idProcurado)

        saida = int(input("Digite 0 se não deseja mais fazer pesquisas: "))

    if saida != 1: saida = 1

    saida = int(input("Digite 0 se nao deseja mais fazer lista de alunos: "))
print("Programa finalizado...")


