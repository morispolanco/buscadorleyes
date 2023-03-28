import os
import streamlit as st
import openai
import requests

# Configuración del API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# URL del buscador perplexity.ai
url_perplexity = "https://api.perplexity.ai/completions"

# Función para realizar consultas en el API de OpenAI y perplexity.ai
def buscar_legislacion_guatemala(query):
    payload = {
        "model": "gpt-3.5-turbo",
        "prompt": f"Consulta sobre legislación guatemalteca: {query}",
        "ppl_api_key": openai.api_key,
        "max_tokens": 2048,
        "temperature": 0,
        "top_p": 1,
        "n": 1,
        "stream": False,
        "logprobs": 0,
        "echo": True,
        "stop": None,
        "presence_penalty": 0,
        "frequency_penalty": 1,
        "best_of": 1,
        "logit_bias": {}
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.post(url_perplexity, json=payload, headers=headers)

    try:
        respuesta = response.json()["choices"][0]["text"].strip()
    except KeyError:
        st.write("Error en la respuesta del API. Por favor, inténtalo de nuevo.")
        st.write("Respuesta completa del API:", response.json())
        respuesta = None

    return respuesta

# Diseño de la aplicación de Streamlit
st.title("Buscador de Legislación Guatemalteca")
st.write("Ingrese su consulta relacionada con la legislación de Guatemala y obtenga respuestas usando la API de OpenAI y el buscador perplexity.ai.")
consulta = st.text_input("Consulta:")

if consulta:
    st.write("Buscando...")
    respuesta = buscar_legislacion_guatemala(consulta)
    
    if respuesta:
        st.write("Respuesta:")
        st.write(respuesta)
    else:
        st.write("No se pudo obtener una respuesta. Por favor, revise los mensajes de error e inténtelo de nuevo.")
else:
    st.write("Por favor, ingrese una consulta.")
