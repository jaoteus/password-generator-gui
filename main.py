from tkinter import *
import random
from tkinter import messagebox

# Configurações da janela:
janelaPrincipal = Tk()
janelaPrincipal.resizable(False, False)
janelaPrincipal.title("Password Generator")

# variavéis
quantidadeDeCaracteres = "0"
senhaGerada = ""
selecionadoLetras = IntVar()
selecionadoNumeros = IntVar()
selecionadoSimbolos = IntVar()


# Funções:
def gerarSenha():
    global senhaGerada, selecionadoLetras, selecionadoSimbolos, selecionadoNumeros
    senhaGerada = ""
    quantidadeDeCaracteres = localParaColocarQuantidadeDeCaracteres.get()

    try:
        quantidadeDeCaracteres = int(quantidadeDeCaracteres)
    except:
        messagebox.showerror(title="ERROR", message="VOCÊ NÃO PODE DEIXAR O INPUT VAZIO, COM LETRAS OU COM SÍMBOLOS!")
    else:
        pass

    # Checando se irá criar com numeros ou letras ou simbolos

    # Todos selecionados:
    if selecionadoSimbolos.get() == 1 and selecionadoNumeros.get() == 1 and selecionadoLetras.get() == 1:
        while len(senhaGerada) < quantidadeDeCaracteres:
            letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            simbolos = ['!', '@', '#', '$', '%', '&', '+', '=', ']', '[', '>', '<', ')', '(', '=', '-', '/', '*', '}',
                        '{']
            '''
            1 - numeros
            2 - letras
            3 - simbolos
            '''
            qualProximoNumero = random.randrange(1, 4)

            if qualProximoNumero == 1:
                algarismoAleatorio = random.choice(letras)
                senhaGerada = senhaGerada + algarismoAleatorio
            elif qualProximoNumero == 2:
                algarismoAleatorio = random.choice(numeros)
                senhaGerada = senhaGerada + algarismoAleatorio
            elif qualProximoNumero == 3:
                algarismoAleatorio = random.choice(simbolos)
                senhaGerada = senhaGerada + algarismoAleatorio
            localDaSenhaGerada.delete(1.0, END)
            localDaSenhaGerada.insert(END, senhaGerada)

    # Apenas numeros e simbolos:
    elif selecionadoSimbolos.get() == 1 and selecionadoNumeros.get() == 1 and selecionadoLetras.get() == 0:
        while len(senhaGerada) < quantidadeDeCaracteres:
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            simbolos = ['!', '@', '#', '$', '%', '&', '+', '=', ']', '[', '>', '<', ')', '(', '=', '-', '/', '*', '}',
                        '{']
            '''
            1 - numeros
            2 - simbolos
            '''
            qualProximoNumero = random.randrange(1, 3)

            if qualProximoNumero == 1:
                algarismoAleatorio = random.choice(numeros)
                senhaGerada = senhaGerada + algarismoAleatorio
            elif qualProximoNumero == 2:
                algarismoAleatorio = random.choice(simbolos)
                senhaGerada = senhaGerada + algarismoAleatorio

            localDaSenhaGerada.delete(1.0, END)
            localDaSenhaGerada.insert(END, senhaGerada)

    # Apenas simbolos e letras
    elif selecionadoSimbolos.get() == 1 and selecionadoNumeros.get() == 0 and selecionadoLetras.get() == 1:
        while len(senhaGerada) < quantidadeDeCaracteres:
            letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            simbolos = ['!', '@', '#', '$', '%', '&', '+', '=', ']', '[', '>', '<', ')', '(', '=', '-', '/', '*', '}',
                        '{']
            '''
            1 - letras
            2 - simbolos
            '''
            qualProximoNumero = random.randrange(1, 3)

            if qualProximoNumero == 1:
                algarismoAleatorio = random.choice(letras)
                senhaGerada = senhaGerada + algarismoAleatorio
            elif qualProximoNumero == 2:
                algarismoAleatorio = random.choice(simbolos)
                senhaGerada = senhaGerada + algarismoAleatorio
            localDaSenhaGerada.delete(1.0, END)
            localDaSenhaGerada.insert(END, senhaGerada)

    # Apenas números e letras
    elif selecionadoSimbolos.get() == 0 and selecionadoNumeros.get() == 1 and selecionadoLetras.get() == 1:
        while len(senhaGerada) < quantidadeDeCaracteres:
            letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            '''
            1 - numeros
            2 - letras
            '''
            qualProximoNumero = random.randrange(1, 3)

            if qualProximoNumero == 1:
                algarismoAleatorio = random.choice(numeros)
                senhaGerada = senhaGerada + algarismoAleatorio
            elif qualProximoNumero == 2:
                algarismoAleatorio = random.choice(letras)
                senhaGerada = senhaGerada + algarismoAleatorio
            localDaSenhaGerada.delete(1.0, END)
            localDaSenhaGerada.insert(END, senhaGerada)

    # Apenas letras:
    elif selecionadoSimbolos.get() == 0 and selecionadoNumeros.get() == 0 and selecionadoLetras.get() == 1:
        while len(senhaGerada) < quantidadeDeCaracteres:
            letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            '''
            1 - letras
            '''
            qualProximoNumero = random.randrange(1, 2)

            if qualProximoNumero == 1:
                algarismoAleatorio = random.choice(letras)
                senhaGerada = senhaGerada + algarismoAleatorio
            localDaSenhaGerada.delete(1.0, END)
            localDaSenhaGerada.insert(END, senhaGerada)


    # Apenas números:
    elif selecionadoSimbolos.get() == 0 and selecionadoNumeros.get() == 1 and selecionadoLetras.get() == 0:
        while len(senhaGerada) < quantidadeDeCaracteres:
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            '''
            1 - numeros
            '''
            qualProximoNumero = random.randrange(1, 2)

            if qualProximoNumero == 1:
                algarismoAleatorio = random.choice(numeros)
                senhaGerada = senhaGerada + algarismoAleatorio
            localDaSenhaGerada.delete(1.0, END)
            localDaSenhaGerada.insert(END, senhaGerada)

    # Apenas símbolos:
    elif selecionadoSimbolos.get() == 1 and selecionadoNumeros.get() == 0 and selecionadoLetras.get() == 0:
        while len(senhaGerada) < quantidadeDeCaracteres:
            simbolos = ['!', '@', '#', '$', '%', '&', '+', '=', ']', '[', '>', '<', ')', '(', '=', '-', '/', '*', '}',
                        '{']
            '''
            1 - simbolos
            '''
            qualProximoNumero = random.randrange(1, 2)

            if qualProximoNumero == 1:
                algarismoAleatorio = random.choice(simbolos)
                senhaGerada = senhaGerada + algarismoAleatorio
            localDaSenhaGerada.delete(1.0, END)
            localDaSenhaGerada.insert(END, senhaGerada)
    else:
        messagebox.showerror(title="ERROR", message="VOCÊ PRECISA SELECIONAR AO MENOS 1 OPÇÃO!")


# LABELS
labelQuantidadeDeCaracteres = Label(janelaPrincipal, text="Quantidade de caracteres:")
labelQuantidadeDeCaracteres.grid(row=0, column=0, padx=10, pady=10, sticky="W")

# ENTRADAS
localParaColocarQuantidadeDeCaracteres = Entry(janelaPrincipal, width=5)
localParaColocarQuantidadeDeCaracteres.grid(row=0, column=0, padx=10, pady=10, sticky="SE")

# BOTÕES
botaoGerarSenha = Button(janelaPrincipal, text="Gerar senha", command=gerarSenha)
botaoGerarSenha.grid(row=4, column=0, padx=0, pady=6, columnspan=2)

# TEXTOS
localDaSenhaGerada = Text(janelaPrincipal, state="normal", width=30, height=2)  # DEPOIS MUDAR PARA NORMAL
localDaSenhaGerada.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

# CHECK BUTTONS
checkButtonOpcaoNumeros = Checkbutton(janelaPrincipal, text="Adicionar números", variable=selecionadoNumeros)
checkButtonOpcaoNumeros.grid(row=1, column=0, padx=0, pady=0)

checkButtonOpcaoLetras = Checkbutton(janelaPrincipal, text="Adicionar letrasﾠﾠﾠ", variable=selecionadoLetras)
checkButtonOpcaoLetras.grid(row=2, column=0, padx=0, pady=0)

checkButtonOpcaoSimbolos = Checkbutton(janelaPrincipal, text="Adicionar símbolos", variable=selecionadoSimbolos)
checkButtonOpcaoSimbolos.grid(row=3, column=0, padx=0, pady=0)

# Loop da janela
janelaPrincipal.mainloop()
