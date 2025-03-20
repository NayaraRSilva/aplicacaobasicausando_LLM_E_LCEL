# Projeto de Tradução com LangChain e Groq

Este projeto utiliza o modelo **Gemma2-9b-it** da **Groq** para realizar traduções de frases. Ele usa a biblioteca **LangChain** para criação de prompts e processamento de respostas do modelo de linguagem. O código também carrega as variáveis de ambiente para a chave da API da Groq e executa a tradução de um texto com base em um template de prompt.

## Bibliotecas Utilizadas

- **LangChain**: Biblioteca para manipulação de modelos de linguagem e criação de pipelines de IA.
- **Groq**: API de IA para interação com o modelo **Gemma2-9b-it**.
- **Dotenv**: Para carregar variáveis de ambiente de um arquivo `.env`.

## Como Usar

### Passo 1: Instalar as dependências

Antes de rodar o código, você precisa instalar as dependências. Para isso, crie um ambiente virtual e instale as bibliotecas necessárias com o comando:

```bash
pip install -r requirements.txt

### Passo 2: Definir as variáveis de ambiente
Crie um arquivo .env na raiz do projeto e defina a variável GROQ_API_KEY com sua chave de API da Groq

´GROQ_API_KEY=your_api_key_here´

### Passo 3: Executar o código
Este é o código completo para realizar a tradução de uma frase usando o modelo Groq e LangChain:

´# IMPORTAÇÃO DAS BIBLIOTECAS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv, find_dotenv
import os 

# CARREGAMENTO DAS VARIAVEIS DE AMBIENTE
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")  # Corrigido: sem espaço extra

# CRIAR O MODELO GROQ
llm = ChatGroq(
    model="Gemma2-9b-it",  # MODELO DE LLM UTILIZADO
    groq_api_key=groq_api_key  # CHAVE DE API DO GROQ
)

# CRIAR O PROMPT TEMPLATE USANDO LCEL
generic_template = "Translate the following sentence into {language}"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])

# PARSER DE SAÍDA
parser = StrOutputParser()

# Criar a Chain
chain = prompt | llm | parser

# Executar a chain
print(chain.invoke({"language": "German", "text": "Hello"}))´

### Explicação do Código:
Importação das Bibliotecas:

langchain_core.prompts.ChatPromptTemplate: Usado para criar e estruturar o template do prompt.
langchain_core.output_parsers.StrOutputParser: Usado para processar a resposta da execução do modelo.
langchain_groq.ChatGroq: Usado para interagir com a API Groq e chamar o modelo Gemma2-9b-it.
dotenv.load_dotenv: Usado para carregar as variáveis de ambiente de um arquivo .env.
Carregamento das Variáveis de Ambiente:

O arquivo .env deve conter a chave da API da Groq para autenticação.
A variável de ambiente GROQ_API_KEY é carregada para ser usada na inicialização do modelo.
Criação do Modelo Groq:

O modelo Gemma2-9b-it é inicializado utilizando a chave da API da Groq.
Criação do Template de Prompt:

Um template simples de tradução é criado, no qual a frase a ser traduzida é passada para o modelo junto com o idioma de destino (por exemplo, "German").
Criação e Execução da Chain:

A chain é criada unindo o template do prompt, o modelo Groq e o parser.
O código finaliza invocando a chain com a frase "Hello" e o idioma de destino sendo o alemão ("German").

### Passo 4: Exemplo de Saída
Quando você executar o código, ele imprimirá a tradução da frase "Hello" para o idioma solicitado (no exemplo, Alemão). A saída pode ser algo como:
`Hallo´
