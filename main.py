"""
OPERAÇÃO DE DEPÓSITO
    Deve ser possível depositar valores positivos para a minha conta bancária.
    A v1 do projeto trabalha apenas com um usuário, dessa forma não precisamos nos preocupar 
    em identificar qual é o número da agência e conta bancária.
    Todos os depósitivos devem ser armazenados em uma variável e exibidos na operação de extrato.

OPERAÇÃO DE SAQUE
    O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
    Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que 
    não será possível sacar o dinheiro por falta de saldo.
    Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

OPERAÇÃO DE EXTRATO
    Essa operação deve listar todos os depósitos e saques realizados na conta. 
    No fim da listagem deve ser exibido o saldo atual da conta.
    Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
    Exemplo: R$ 1500.45
"""
saldo = 300.00
LIMITE_QTD_SAQUE = 3
LIMITE_VALOR_SAQUE = 500.00
saque_realizado = 0
opcao = ""
extrato = " EXTRATO ".center(30, "=")

while opcao != "x":
    opcao = input("""
Informe uma das opções a seguir:
                  
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

==> """).lower()
    if opcao == "d":
        deposito = float(input("informe o valor do depósito: "))

        if (deposito <= 0):
            print("Por favor, informe um valor maior que zero para depósito.")

        else:
            saldo += deposito
            print(f"O saldo atual em conta é de R$ {saldo:.2f}")
            extrato += f"\nDEPÓSITO: R$ {deposito:.2f}"
    
    elif opcao == "s":
        
        saque = float(input("Informe o valor do saque: "))

        if saque > LIMITE_VALOR_SAQUE:
            print(f"O valor máximo para saque é de R$ {LIMITE_VALOR_SAQUE:.2f}")
        
        elif saque_realizado >= LIMITE_QTD_SAQUE:
            print(f"Você já ultrapassou o limite diário de saques. O limite é de {LIMITE_QTD_SAQUE} saques.")
       
        elif saque >= saldo:
            print(f"Não há saldo suficiente para realizar o saque. Saldo atual é de R$ {saldo:.2f}")
        
        else:
            saldo -= saque
            print(f"Saque realizado com sucesso! O valor atual do saldo é de {saldo:.2f}")
            extrato += f"\nSAQUE: R$ {saque:.2f}"
            saque_realizado += 1
    
    elif opcao == "e":
        print(f"{extrato} \n\nSALDO: R$ {saldo:.2f}")
        print("==".center(30,"="))
    
    elif opcao == "x":
        print("Obrigado! Volte sempre. :-)")
    
    else:
        print("Opção inválida!")