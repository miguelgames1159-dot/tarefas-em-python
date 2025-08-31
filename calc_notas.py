lista_alunos = []
lista_notas = []

def menu():
    print("="*30)
    print("Menu de Notas e médias")
    print("="*30)
    print("Bem vindo ao menu de notas!! \n Escolha uma das opções:")
    print("1- Cadastro do aluno")
    print("2- Cadastro da nota")
    print("3- Situação do aluno")
    print("4- Média faltante")
    print("5-sair")
    print("="*30)


def cadastro_nome():
    nome_aluno = input("qual o nome do aluno?").title().strip()
    if not nome_aluno:
        print("O nome do aluno não pode estar vazio...")
        return
    if nome_aluno in lista_alunos:
        print("nome do aluno já está cadastrado,tente denovo...")
        return
    lista_alunos.append(nome_aluno)
    lista_notas.append([])
    print(f"Parabéns {nome_aluno} !! você foi cadastrado com sucesso !")

def cadastro_notas():
    if not lista_alunos:
        print("Ainda não existe o cadastro de algum aluno, volte ao menu e tente novamente porfavor...")
        return
    
    print("Alunos cadastrados")
    for i in range(len(lista_alunos)):
        print(f"\n {i+1} = {lista_alunos[i]}")
    
    escolha = int(input("Escolha o número do aluno para cadastrar a nota: ")) -1
    if escolha < 0 or escolha >= len(lista_alunos):
        print("opção inválida!")
        return
    add_nota = float(input(f"Digite a nota de {lista_alunos[escolha]}: "))
    if add_nota < 0 or add_nota >10:
        print("escolha uma nota de 0 a 10!!")
        return


    lista_notas[escolha].append(add_nota)
    print(f" Nota {add_nota} cadastrada para {lista_alunos[escolha]}!")

def situacao_aluno():
    if not lista_alunos:
        print("Ainda não existe o cadastro de algum aluno, volte ao menu e tente novamente porfavor...")
        return
    print("Alunos cadastrados:")
    for i in range(len(lista_alunos)):
        print(f"{i+1} - {lista_alunos[i]}")
    escolha = int(input("Escolha o número do aluno para ver a situação da nota:")) -1
    if escolha < 0 or escolha >= len(lista_alunos):
        print("opção inválida!")
        return
    if not lista_notas[escolha]:
        print("O aluno ainda não tem uma nota cadastrada")
        return
    média = sum(lista_notas[escolha]) / len(lista_notas[escolha])
    print(f"A situação do(a) {lista_alunos[escolha]} é:")
    print(f"Notas:{lista_notas[escolha]} \n média:{média: .2f}")
    if média >= 6:
        print("Situação: Aprovado! Parabéns! ")
    else:
        print("A média esta abaixo de 6! situação: Reprovado!")

def media_faltante():
    if not lista_alunos:
        print("Ainda não existe nenhum aluno cadastrado.")
        return

    print("Alunos cadastrados:")
    for i in range(len(lista_alunos)):
        print(f"{i+1} - {lista_alunos[i]}")

    escolha = int(input("Escolha o número do aluno para calcular a média faltante: ")) - 1
    if escolha < 0 or escolha >= len(lista_alunos):
        print("Opção inválida!")
        return

    if not lista_notas[escolha]:
        print(f"O aluno {lista_alunos[escolha]} ainda não tem notas cadastradas.")
        return
    média_min = 6  
    média_atual = sum(lista_notas[escolha]) / len(lista_notas[escolha])
    faltante = média_min * (len(lista_notas[escolha]) + 1) - sum(lista_notas[escolha])

    print(f"\nAluno: {lista_alunos[escolha]}")
    print(f"Notas atuais: {lista_notas[escolha]}")
    print(f"Média atual: {média_atual:.2f}")

    if média_atual >= 6:
        print("✅ O aluno já atingiu a média mínima!")
    elif faltante > 10:
        print("⚠️ Não é possível atingir a média mínima com a próxima nota.")
    else:
        print(f"Para atingir média {média_min}, o aluno precisa tirar {faltante:.2f} na próxima nota.")
    

def main():
    while True:
        menu()
        opção = input("Que função que usar?").lower().strip()
        match opção:
            case "1":
                cadastro_nome()
            case "2":
                cadastro_notas()
            case "3":
                situacao_aluno()
            case "4":
                media_faltante()
            case "5" | "sair":
                print("saindo do sistema...")
                break
            case _: 
                print("Opção inválida")

if __name__ == "__main__":
    main()
