import streamlit as st

st.set_page_config(page_title="Bienestar integral🌿", page_icon="🧘", layout="centered")
st.title("Evaluación de Autocuidado❤️‍🩹")

st.write("Por favor, responde del 1 al 5 cada afirmación, donde:\n- **1 = Nunca**\n- **2 = Casi nunca**\n- **3 = A veces**\n- **4 = Casi siempre**\n- **5 = Siempre**")

# Preguntas
preguntas = [
    "1. Realizo actividad física de manera regular (al menos 3 veces por semana).",
    "2. Me siento con energía suficiente para cumplir con mis actividades cotidianas.",
    "3. Identifico cuándo estoy estresado(a) y puedo reconocer las causas.",
    "4. Utilizo estrategias para calmarme cuando me siento tenso(a).",
    "5. Me siento emocionalmente estable durante la mayor parte del tiempo.",
    "6. Tengo metas claras a corto y largo plazo.",
    "7. Siento que mi vida tiene un propósito que me motiva.",
    "8. Mantengo contacto frecuente con familiares o amigos.",
    "9. Me siento apoyado(a) por las personas que me rodean.",
    "10. Puedo recuperarme emocionalmente después de momentos difíciles.",
    "11. Confío en mis capacidades para resolver problemas.",
    "12. Tengo hábitos diarios que me ayudan a sentirme mejor.",
    "13. Me doy tiempo para mí y mis necesidades personales.",
    "14. Estoy atenta(o) a cambios en mi cuerpo, mente o emociones.",
    "15. Hago pausas para reflexionar cómo me siento y qué necesito mejorar."
]

respuestas = []

# Mostrar sliders
for pregunta in preguntas:
    valor = st.slider(pregunta, 1, 5, 3)
    respuestas.append(valor)
    st.markdown("<div style='margin-top: -10px; margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# Botón para calcular resultado
if st.button("Calcular promedio"):
    promedio = sum(respuestas) / len(respuestas)

    st.subheader("🔍 Resultado de la evaluación:")
    st.write(f"**Promedio obtenido:** {promedio:.2f} / 5")

    if promedio >= 4:
        st.success("✨ ¡Muy bien! Tienes un alto nivel de autocuidado. Sigue con esos buenos hábitos.")
    elif promedio >= 2.5:
        st.warning("⚠️ Tu nivel de autocuidado es moderado. Sería bueno reforzar algunas áreas.")
    else:
        st.error("❗Tu nivel de autocuidado es bajo. Considera hacer ajustes y buscar apoyo si es necesario.")

    st.caption("Gracias por tomarte un momento para reflexionar sobre tu bienestar.")
