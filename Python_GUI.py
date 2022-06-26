#NO TERMINAL:  pip install PySimpleGUI


import PySimpleGUI as infinity
#Pode colocar qualquer nome depois do "as"

#Tela inicial - FRONTEND
infinity.theme('Reddit')


#Tela
ColunasLinhas = [
    [infinity.Text("Login")],
    [infinity.Input(key='login', size=(15,1))]
    [infinity.Text("Senha"), infinity.Input(key='senha', size=(15,1), password_char="*")],
    [infinity.Checkbox("Salvar Senha")],
    [infinity.Button("ENTRAR"), infinity.Button("SAIR")]
]

#Criar uma janela
janela = infinity.Window("Tela de Login do Usuário", ColunasLinhas)

#CODIGO - BACKEND

while True:
    evento, valores = janela.read()
    if evento == "SAIR":
        break
    if evento == "ENTRAR":
        if valores['login'] == "Germanna" and valores['senha'] == '123':
            print(("Você venceu!"))
        else:
            print("TENTE DE NOVO!")
