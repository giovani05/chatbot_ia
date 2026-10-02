# pip install streamlit openai
import streamlit as st
# streamlit run codigo.py
from openai import OpenAI

modelo_ia = OpenAI(api_key="AQ.Ab8RN6I2bBkj_aocmFOOtcj2ZnorY_GgHDmo9FSmfsMonhSJ8g",
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai",)

# TITULO
st.title("Chatbot de IA")

# cria o historico de mensagem
if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []

# CAMPO DE MENSAGEM (input)
mensagem_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagem in st.session_state["lista_mensagem"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)

if(mensagem_usuario):
    # exibir mensagem do usuario
    # user -> usuario
    # assistant -> chatbot
    st.chat_message("user").write(mensagem_usuario)
    mensagem1={"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagem"].append(mensagem1)

    # pegar a resposta do chatbot
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagem"],
        model="gemini-flash-lite-latest"
    )

    print(resposta_modelo)

    resposta_ia = resposta_modelo.choices[0].message.content

    # enviar a resposta do chatbot para a conversa
    st.chat_message("assistant").write(resposta_ia)
    mensagem2={"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem2)
# manter o historico da mensagem do usuario e do chatbot

# tornar as respostas inteligentes

# QUANDO O USUARIO ENVIA MENSAGEM
    # MOSTRAR A MENSAGEM NA CONVERSA
    # MANDAR A MENSAGEM PARA O CHATBOT
    # MOSTRAR A RESPOSTA DO CHATBOT NA CONVERSA

