import ply.lex as lex
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Definição dos tokens
tokens = (
    'ID', 'NUMERO', 'SOMA_ASSIGN', 'SUBTRACAO_ASSIGN', 'MULTIPLICACAO_ASSIGN', 'DIVISAO_ASSIGN',
    'SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO',
    'ASSIGN', 'EQ', 'LE', 'GE', 'LT', 'GT', 'PAREN_ESQUERDO', 'PAREN_DIREITO', 'CHAVE_ESQUERDA', 'CHAVE_DIREITA',
    'WHILE', 'IF', 'ELIF', 'ELSE'
)

# Definições dos padrões dos tokens (ordem importante)
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_SOMA_ASSIGN = r'\+='
t_SUBTRACAO_ASSIGN = r'-='
t_MULTIPLICACAO_ASSIGN = r'\*='
t_DIVISAO_ASSIGN = r'/='

t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_ASSIGN = r'='
t_LT = r'<'
t_GT = r'>'
t_PAREN_ESQUERDO = r'\('
t_PAREN_DIREITO = r'\)'
t_CHAVE_ESQUERDA = r'\{'
t_CHAVE_DIREITA = r'\}'

# Para identificar palavras-chave
def t_WHILE(t):
    r'WHILE'
    return t

def t_IF(t):
    r'IF'
    return t

def t_ELIF(t):
    r'ELIF'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

# Para identificar números
def t_NUMERO(t):
    r'\d+(\.\d*)?'
    t.value = float(t.value)
    return t

# Para identificar identificadores (nomes de variáveis, funções, etc.)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Verificar se o identificador é uma palavra-chave
    if t.value.upper() in ('WHILE', 'IF', 'ELIF', 'ELSE'):
        t.type = t.value.upper()
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Ignorar comentários
def t_COMENTARIO(t):
    r'\#.*'
    pass  # Não retorna nada, simplesmente ignora o comentário

# Definir uma função para lidar com quebras de linha
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definir uma função para erros
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Função para criar o lexer
def criar_lexer():
    return lex.lex()

# Função para analisar o código e exibir os tokens encontrados
def analisar_codigo():
    codigo = texto_entrada.get("1.0", "end-1c")
    
    lexer = criar_lexer()
    lexer.input(codigo)
    
    tokens_encontrados = []
    for token in lexer:
        tokens_encontrados.append(f"{token.type}: {token.value}")
    
    texto_tokens.delete("1.0", "end-1c")
    texto_tokens.insert("1.0", "\n".join(tokens_encontrados))

# Função para salvar os tokens em um arquivo
def salvar_tokens():
    tokens = texto_tokens.get("1.0", "end-1c")
    
    if tokens:
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if arquivo:
            with open(arquivo, 'w') as f:
                f.write(tokens)
            messagebox.showinfo("Sucesso", "Tokens salvos com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Nenhum token encontrado para salvar.")

# Criando a janela principal
root = tk.Tk()
root.title("Analisador Léxico")

# Criando os elementos da interface
label_entrada = tk.Label(root, text="Código de Entrada:")
label_entrada.pack()

texto_entrada = tk.Text(root, height=10, width=50)
texto_entrada.pack()

botao_analisar = tk.Button(root, text="Analisar", command=analisar_codigo)
botao_analisar.pack()

label_tokens = tk.Label(root, text="Tokens Encontrados:")
label_tokens.pack()

texto_tokens = tk.Text(root, height=10, width=50)
texto_tokens.pack()

botao_salvar = tk.Button(root, text="Salvar Tokens", command=salvar_tokens)
botao_salvar.pack()

# Iniciando o aplicativo
root.mainloop()
