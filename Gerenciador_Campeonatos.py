# Mini Projeto SW
# Pablo Estevam Godoy Miranda   RGM:  11251505821 
# Matheus Barros Moreira da Silva RGM: 11252100741 
# Alexandre Moura da Silva RGM: 11242100327 
# Ana Clara Vilela dos Santos RGM: 11251104715 
# Controle Básico de Campeonato - Cadastro de Jogadores


# OBS IMPORTANTE: Ter instalado as bibliotecas: 'tkinter', 'os', 'PIL' e 'ttkbootstrap' para rodar sem problemas o código

# Bibliotecas
from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import os
from PIL import Image, ImageTk
from Cores import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
 


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Carrega Dados TXT
def Load_Txt():
    global D1
    L0 = []
    caminho = os.path.join(BASE_DIR, "dados.txt")
    
    # Verifica se o arquivo existe, se não existir, cria um vazio
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as Dados:
            pass
        return {}
    
    with open(caminho, "r", encoding="utf-8") as Dados:
        for i in Dados:
            linha = i.rstrip().split(",")
            if len(linha) >= 5:  # Verifica se a linha tem pelo menos 5 campos
                L0.append(linha)

    # Transforma Lista em Dict
    D1_temp = {}
    for i in L0:
        if len(i) >= 5:
            D1_temp[i[0]] = [i[1], i[2], i[3], i[4]]
    return D1_temp

# Grava TXT
def Save_Txt(Dict):
    caminho = os.path.join(BASE_DIR, "dados.txt")

    with open(caminho, "w", encoding="utf-8") as Dados:
        for chave, dados in Dict.items(): 
            Dados.write(f"{chave},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")

# Função para Logotipo
def Logo():
    try:
        caminho_logo = os.path.join(BASE_DIR, "lg.png")
        if os.path.exists(caminho_logo):
            image = Image.open(caminho_logo)
            resize_image = image.resize((130,130))
            img = ImageTk.PhotoImage(resize_image, master=Janela)
            Logo = Label(Janela, image=img, bg="#1A1A1A")
            Logo["bg"] = ("#1A1A1A")
            Logo.image = img
            Logo.place(x=20,y=160)
    except Exception as e:
        print(f"Erro ao carregar logo: {e}")

# Função para popular o Widget TreeView
def List_Func(): # Listar Jogadores
    tree.delete(*tree.get_children()) # limpa TreeView
    L1 = []
    for chave, dados in D1.items():
        L1.append([chave, dados[0], dados[1], dados[2], dados[3]])
    for i in L1:
        tree.insert('', END, values=i)

# Rotinas de Inclusão
def Inc_func():
     # Limpando os Widgets de entrada
     Matr.delete(0, END)
     Nome.delete(0, END)
     Nick.delete(0, END)
     Time.delete(0, END)
     Posicao.delete(0, END)
     # Escondendo a TreeView,Labels e Botões
     tree.place_forget() # esconde widgets
     lbl_role.place_forget()
     lbl_sel.place_forget()
     BT_List['state'] = DISABLED # desabilita botões
     BT_Inc['state'] = DISABLED
     BT_Exc['state'] = DISABLED
     BT_Alt['state'] = DISABLED
     Sair['state'] = DISABLED
     # Mostrando os widgets de entrada de dados
     lbl_matr.place(x=180,y=25)
     lbl_nome.place(x=180,y=50) 
     lbl_nick.place(x=180,y=75)
     lbl_time.place(x=180,y=100)
     lbl_posicao.place(x=180,y=125)
     Matr.place(x=300,y=25) 
     Nome.place(x=300,y=50)
     Nick.place(x=300,y=75)
     Time.place(x=300,y=100)
     Posicao.place(x=300,y=125)
     BT_Save.place(x=180,y=150)
     BT_Retorno.place(x=300,y=150)

# Rotinas Inclusão - Salvando Novo Registro
def Save_Func(): # inclusão de registro TXT e Dicionário
        my_matr = Matr.get() # captura dados dos widget Entry
        my_name = Nome.get()
        my_nick = Nick.get()
        my_time = Time.get()
        my_posicao = Posicao.get()
        
        if my_matr in D1:
            showinfo(title='Atenção', message='Matrícula já existe')
        elif len(my_name) == 0:
            showinfo(title='Atenção', message='Nome em branco')
        elif len(my_nick) == 0:
            showinfo(title='Atenção', message='Nickname em branco')
        elif len(my_time) == 0:
            showinfo(title='Atenção', message='Time em branco')
        elif len(my_posicao) == 0:
            showinfo(title='Atenção', message='Posição em branco')
        else:
            answer = askyesno(title='confirmation',
                                message='Você tem certeza que deseja incluir este registro?')
            if answer:
                D1[my_matr] = [my_name, my_nick, my_time, my_posicao] # inclusão dicionário
                Save_Txt(D1) # inclusão .TXT
                Retorno()
            else:
                showinfo(title='Atenção', message='Operação Cancelada')

# rotinas de Alteração
def Alt_func():
    if not tree.focus(): # verifica se há item selecionado na TreeView
        showinfo(title='ERRO', message='Selecione um item para Alteração')
    else:
        # Escondendo a TreeView
        tree.place_forget()
        # Limpando os Widgets de entrada
        Matr.delete(0, END)
        Nome.delete(0, END)
        Nick.delete(0, END)
        Time.delete(0, END)
        Posicao.delete(0, END)
        # Esconde Labels de info para usuário
        lbl_role.place_forget()
        lbl_sel.place_forget()
        BT_List['state'] = DISABLED
        BT_Inc['state'] = DISABLED
        BT_Alt['state'] = DISABLED
        BT_Exc['state'] = DISABLED
        Sair['state'] = DISABLED
        # Mostrando os widgets de alteração
        lbl_matr_alt.place(x=180,y=25)
        lbl_nome.place(x=180,y=50) 
        lbl_nick.place(x=180,y=75)
        lbl_time.place(x=180,y=100)
        lbl_posicao.place(x=180,y=125)
        Matr.place(x=300,y=25)
        Nome.place(x=300,y=50)
        Nick.place(x=300,y=75)
        Time.place(x=300,y=100)
        Posicao.place(x=300,y=125)
        BT_Save_Alt.place(x=180,y=150)
        BT_Retorno.place(x=300,y=150)
        # Mostrando item selecionado
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        # inclusão dos dados selecionados no widget Entry
        Matr.insert(0, (rowid["values"][0]))
        Matr['state'] = DISABLED # Matricula não pode ser alterada
        Nome.insert(0, (rowid["values"][1]))
        Nick.insert(0, (rowid["values"][2]))
        Time.insert(0, (rowid["values"][3]))
        Posicao.insert(0, (rowid["values"][4]))

def Save_Alt_Func():
        # capturando dados do Widget Entry para as variáveis
        my_matr = Matr.get() 
        my_name = Nome.get()
        my_nick = Nick.get()
        my_time = Time.get()
        my_posicao = Posicao.get()
        
        if len(my_name) == 0: # verifica se nome está em branco
            showinfo(title='Atenção', message='Nome em branco')
        elif len(my_nick) == 0:
            showinfo(title='Atenção', message='Nickname em branco')
        elif len(my_time) == 0:
            showinfo(title='Atenção', message='Time em branco')
        elif len(my_posicao) == 0:
            showinfo(title='Atenção', message='Posição em branco')
        else:
            answer = askyesno(title='confirmation',
                                message='Você tem certeza que deseja alterar este registro?')
            if answer:
                D1[my_matr] = [my_name, my_nick, my_time, my_posicao]
                Save_Txt(D1)
                Retorno()
            else:
                showinfo(title='Atenção', message='Operação Cancelada')

# Rotinas de Retorno
def Retorno():
    lbl_matr.place_forget()
    lbl_matr_alt.place_forget()
    lbl_nome.place_forget()
    lbl_nick.place_forget()
    lbl_time.place_forget()
    lbl_posicao.place_forget()
    Matr.place_forget()
    Nome.place_forget()
    Nick.place_forget()
    Time.place_forget()
    Posicao.place_forget()
    BT_Save.place_forget()
    BT_Retorno.place_forget()
    BT_Save_Alt.place_forget()
    tree.place(x=180,y=25)  # posiciona 
    lbl_role.place(x=180,y=260) 
    lbl_sel.place(x=180,y=280)
    BT_List['state'] = NORMAL
    BT_Inc['state'] = NORMAL
    BT_Exc['state'] = NORMAL
    BT_Alt['state'] = NORMAL
    Sair['state'] = NORMAL
    Matr['state'] = NORMAL
    List_Func()

# Rotina de Exclusão
def Exc_Func(): # Excluir Jogador
    if not tree.focus(): # verifica se existe linha selecionada na TreeView 
        showinfo(title='ERRO', message='Selecione um item para Exclusão')
    else:
        # Coletando qual item está selecionado.
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        
        # Verifica se há valores no item selecionado
        if not rowid["values"]:
            showinfo(title='ERRO', message='Nenhum dado encontrado no item selecionado')
            return
            
        Matr_Exc = str(rowid["values"][0])  # Convertendo para string para garantir
        
        # Verifica se a matrícula existe no dicionário
        if Matr_Exc not in D1:
            showinfo(title='ERRO', message=f'Matrícula {Matr_Exc} não encontrada no sistema')
            return
            
        answer = askyesno(title='confirmation', 
                          message=f'Você tem certeza que deseja excluir o jogador {D1[Matr_Exc][0]}?')
        if answer:
            del D1[Matr_Exc]
            Save_Txt(D1)
            List_Func()
            showinfo(title='Atenção', message='Registro Excluído')
        else:
            showinfo(title='Atenção', message='Operação Cancelada')

#### Carrega txt
D1 = Load_Txt()

#### Instancia a classe TK e Mostra Container
Janela = tb.Window(themename="darkly")
Janela.title("Sistema de Cadastro de Jogadores - Campeonato")
Janela.geometry('740x320') # Dimensiona a janela
Janela["bg"] = ("#1A1A1A")
Janela.iconbitmap("logoIC.ico")


#### Título do Aplicativo - Widgets Label
Tit = Label(Janela, text="Selecione uma das opções abaixo")
Tit.place(x=10,y=0) # posiona o widgets no container
Tit["font"] = ("Verdana", "10", "italic", "bold",)
Tit["fg"] = ("#B463FF")
Tit["bg"] = ("#1A1A1A")

#### Botão List
BT_List = Button(Janela, text="Relatório Geral", width=15)
BT_List.place(x=30,y=25)
BT_List['command'] = List_Func
BT_List["fg"] = ("white")
BT_List["bg"] = ("#2E2E2E")
#### TreeView
# Define columns Treeview - 5 colunas
columns = ('Mat', 'Nm', 'Nick', 'Time', 'Pos')
tree = ttk.Treeview(Janela, columns=columns, show='headings')

style = ttk.Style(Janela)
style.theme_use("default")

style.configure(
    "Treeview",
    background="#2E2E2E",
    fieldbackground="#2E2E2E",
    foreground="white"
)
style.configure(
    "Treeview.Heading",
    background="#1A1A1A",
    foreground="#B771F8"
)

# define headings e tamanhos
tree.column('#1', width=80)   # Matrícula
tree.column('#2', width=150)  # Nome
tree.column('#3', width=100)  # Nickname
tree.column('#4', width=100)  # Time
tree.column('#5', width=100)  # Posição

# cabeçalhos
tree.heading('Mat', text='Matrícula')
tree.heading('Nm', text='Nome do Jogador')
tree.heading('Nick', text='Nickname')
tree.heading('Time', text='Time')
tree.heading('Pos', text='Posição')

tree.delete(*tree.get_children()) # limpa TreeView
tree.place(x=180,y=25)  # posiciona


#### Rotinas de Inclusão
# Botão Inclusão
BT_Inc = Button(Janela, text="Incluir Jogador", width=15)
BT_Inc.place(x=30,y=50)
BT_Inc['command'] = Inc_func
BT_Inc["fg"] = ("white")
BT_Inc["bg"] = ("#2E2E2E")

# Widgets para entrada de dados
lbl_matr = Label(Janela, text="Matrícula:")
lbl_matr["fg"] = ("white")
lbl_matr["bg"] = ("#1A1A1A")
Matr = Entry(Janela, width=10)
Matr["fg"] = ("#1A1A1A")
Matr["bg"] = ("#C9C9C9")
lbl_nome = Label(Janela, text="Nome:")
lbl_nome["fg"] = ("white")
lbl_nome["bg"] = ("#1A1A1A")
Nome = Entry(Janela, width=30)
Nome["fg"] = ("#1A1A1A")
Nome["bg"] = ("#C9C9C9")
lbl_nick = Label(Janela, text="Nickname:")
lbl_nick["fg"] = ("white")
lbl_nick["bg"] = ("#1A1A1A")
Nick = Entry(Janela, width=30)
Nick["fg"] = ("#1A1A1A")
Nick["bg"] = ("#C9C9C9")
lbl_time = Label(Janela, text="Time:")
lbl_time["fg"] = ("white")
lbl_time["bg"] = ("#1A1A1A")
Time = Entry(Janela, width=30)
Time["fg"] = ("#1A1A1A")
Time["bg"] = ("#C9C9C9")
lbl_posicao = Label(Janela, text="Posição:")
lbl_posicao["fg"] = ("white")
lbl_posicao["bg"] = ("#1A1A1A")
Posicao = Entry(Janela, width=30)
Posicao["fg"] = ("#1A1A1A")
Posicao["bg"] = ("#C9C9C9")

BT_Save = Button(Janela, text="Incluir Jogador", width=15)
BT_Save['command'] = Save_Func
BT_Save["fg"] = ("white")
BT_Save["bg"] = ("#2E2E2E")
BT_Retorno = Button(Janela, text="Retornar", width=15, command=Retorno)
BT_Retorno["fg"] = ("white")
BT_Retorno["bg"] = ("#2E2E2E")

#### Rotinas para Alteração
BT_Alt = Button(Janela, text="Alterar Informações", width=15)
BT_Alt.place(x=30,y=75)
BT_Alt["fg"] = ("white")
BT_Alt['command'] = Alt_func
BT_Alt["bg"] = ("#2E2E2E")
BT_Save_Alt = Button(Janela, text="Salvar Alteração", width=15)
BT_Save_Alt["fg"] = ("white")
BT_Save_Alt['command'] = Save_Alt_Func
BT_Save_Alt["bg"] = ("#2E2E2E")

# Label alteração
lbl_matr_alt = Label(Janela, text="Matrícula Selecionada")
lbl_matr_alt["fg"] = ("white")
lbl_matr_alt["bg"] = ("#1A1A1A")

#### Botão Excluir
BT_Exc = Button(Janela, text="Excluir Jogador", width=15)
BT_Exc.place(x=30,y=100)
BT_Exc['command'] = Exc_Func
BT_Exc["fg"] = ("white")
BT_Exc["bg"] = ("#2E2E2E")


#### Botão Sair
Sair = Button(Janela, text="Sair da Aplicação", command=Janela.destroy, width=15)
Sair.place(x=30,y=125)
Sair["fg"] = ("white")
Sair["bg"] = ("#2E2E2E")

#### Orientações para o usuário
lbl_role = Label(Janela, text="Role a tela para baixo com o Mouse")
lbl_role.place(x=180,y=260) 
lbl_role["font"] = ("Arial","8","bold",)
lbl_role["fg"] = ("#B96EFF")
lbl_role["bg"] = ("#1A1A1A")

lbl_sel = Label(Janela, text="Selecione o registro para Alterar / Excluir")
lbl_sel.place(x=180,y=280)
lbl_sel["font"] = ("Arial","8","bold",)
lbl_sel["fg"] = ("red")
lbl_sel["bg"] = ("#1A1A1A")

#### Exibe a Tela
Logo()
Janela.mainloop()