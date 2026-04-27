import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="🦹‍♀️")

st.title("🦹‍♀️ Trivia: Villanas de Disney")

# Preguntas
preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de La Sirenita?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Yzma"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana puede convertirse en dragón?",
        "opciones": ["Maléfica", "Reina Grimhilde", "Lady Tremaine", "Madre Gothel"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Quién odia a los dálmatas?",
        "opciones": ["Cruella de Vil", "Úrsula", "Yzma", "Maléfica"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Qué villana aparece en Enredados?",
        "opciones": ["Madre Gothel", "Yzma", "Reina Roja", "Cruella"],
        "respuesta": "Madre Gothel"
    },
    {
        "pregunta": "¿Quién es la villana de Las locuras del emperador?",
        "opciones": ["Yzma", "Maléfica", "Úrsula", "Cruella"],
        "respuesta": "Yzma"
    }
]

# Inicializar estado
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.preguntas_mezcladas = random.sample(preguntas, len(preguntas))
    st.session_state.opciones_mezcladas = []

# Obtener pregunta actual
if st.session_state.indice < len(preguntas):
    pregunta_actual = st.session_state.preguntas_mezcladas[st.session_state.indice]

    # Mezclar opciones cada vez que inicia nueva pregunta
    if len(st.session_state.opciones_mezcladas) <= st.session_state.indice:
        opciones = pregunta_actual["opciones"].copy()
        random.shuffle(opciones)
        st.session_state.opciones_mezcladas.append(opciones)

    opciones = st.session_state.opciones_mezcladas[st.session_state.indice]

    st.subheader(f"Pregunta {st.session_state.indice + 1}")
    respuesta_usuario = st.radio(pregunta_actual["pregunta"], opciones)

    if st.button("Responder"):
        if respuesta_usuario == pregunta_actual["respuesta"]:
            st.success("¡Correcto!")
            st.session_state.puntaje += 1
        else:
            st.error(f"Incorrecto. La respuesta era: {pregunta_actual['respuesta']}")

        st.session_state.indice += 1
        st.rerun()

else:
    st.subheader("Resultado final")

    st.write(f"Tu puntaje: {st.session_state.puntaje}/5")

    if st.session_state.puntaje == 5:
        st.balloons()
        st.success("🎉 ¡Perfecto! ¡Conoces a todas las villanas!")
        st.snow()
    else:
        st.info("Sigue intentando para lograr el puntaje perfecto 😈")

    if st.button("Reiniciar"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
