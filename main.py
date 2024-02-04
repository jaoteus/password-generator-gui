from tkinter import *
import random
from tkinter import messagebox

# Configurações da janela:
janelaPrincipal = Tk()
janelaPrincipal.resizable(False, False)
janelaPrincipal.title("PG")

# variavéis
quantidadeDeCaracteres = "0"
senhaGerada = ""

# Funções:
def gerarSenha():
    global senhaGerada
    senhaGerada = ""
    quantidadeDeCaracteres = localParaColocarQuantidadeDeCaracteres.get()
    try:
        quantidadeDeCaracteres = int(quantidadeDeCaracteres)
    except:
        messagebox.showerror(title="ERROR",
                             message="VOCÊ NÃO PODE DEIXAR O INPUT VAZIO, COM LETRAS OU COM SÍMBOLOS!"
                             )
    else:
        pass
    while len(senhaGerada) < quantidadeDeCaracteres:
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        simbolos = ['!', '@', '#', '$', '%', '&']
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

# Corpo da janela:

# LABELS
labelQuantidadeDeCaracteres = Label(janelaPrincipal,
                                    text="Quantidade de caracteres:"
                                    )
labelQuantidadeDeCaracteres.grid(row=0,
                                 column=0,
                                 padx=10,
                                 pady=10
                                 )
# ENTRADAS
localParaColocarQuantidadeDeCaracteres = Entry(janelaPrincipal,
                                               width=5
                                               )
localParaColocarQuantidadeDeCaracteres.grid(row=0,
                                            column=1,
                                            padx=10,
                                            pady=10,
                                            columnspan=1
                                            )
# BOTÕES
botaoGerarSenha = Button(janelaPrincipal,
                         text="Gerar senha",
                         command=gerarSenha
                         )
botaoGerarSenha.grid(row=1,
                     column=0,
                     padx=10,
                     pady=10,
                     columnspan=2
                     )

# TEXTOS
localDaSenhaGerada = Text(janelaPrincipal,
                          state="normal",  # DEPOIS MUDAR PARA NORMAL
                          width=30,
                          height=2
                          )
localDaSenhaGerada.grid(row=2,
                        column=0,
                        padx=10,
                        pady=10,
                        columnspan=2
                        )


# Loop da janela
janelaPrincipal.mainloop()
