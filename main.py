# IMPORTAÇÃO DAS BIBLIOTECAS
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
print(chain.invoke({"language": "German", "text": "Hello"}))





