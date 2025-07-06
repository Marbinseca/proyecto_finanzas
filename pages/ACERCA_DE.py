import streamlit as st

st.set_page_config(page_title="Acerca de Herramientas Financieras", page_icon="images/finance.png", layout="centered")

st.title("ℹ️ Acerca de Nosotros")
st.markdown("""
    Descubre el propósito de estas herramientas financieras y cómo puedes contactarnos.
""")

st.divider()

# --- Sección Acerca del Proyecto ---
st.header("Nuestro Propósito")
st.markdown("""
Bienvenido a **Herramientas Financieras**, un proyecto diseñado para democratizar el acceso a cálculos financieros complejos de una manera **sencilla, intuitiva y accesible**. Nuestro objetivo es empoderar a estudiantes, profesionales y cualquier persona interesada en finanzas, proporcionándoles calculadoras precisas y explicaciones claras sobre conceptos clave.

Creemos firmemente que comprender cómo funciona el dinero es fundamental para tomar decisiones informadas, ya sea al planificar inversiones, gestionar deudas o simplemente entender mejor el panorama económico personal.

Esta aplicación ha sido desarrollada utilizando **Python y Streamlit**, lo que nos permite ofrecer una interfaz de usuario interactiva y moderna directamente en tu navegador.
""")

st.markdown("---")

# --- Sección Herramientas Disponibles ---
st.header("Herramientas que Ofrecemos")
st.markdown("""
En Herramientas Financieras, encontrarás calculadoras especializadas para tus necesidades:

* **Calculadora TIR y VAN:** Evalúa la rentabilidad de tus proyectos de inversión.
* **Calculadora de Amortización:** Visualiza el desglose de tus pagos de préstamos y la reducción de tu deuda.
* **Calculadora de Tasas de Interés:** Convierte entre tasas nominales y efectivas con diferentes frecuencias.
* **Calculadora de Interés Compuesto:** Proyecta el crecimiento de tus inversiones a largo plazo con aportes periódicos.
* **Teoría Financiera Esencial:** Explora los conceptos y fórmulas detrás de cada herramienta para un aprendizaje profundo.
""")

st.markdown("---")

# --- Sección Contacto ---
st.header("Contacto y Soporte")
st.markdown("""
Valoramos tu opinión y estamos aquí para ayudarte. Si tienes preguntas, sugerencias para nuevas herramientas, encuentras algún error o simplemente quieres saludar, no dudes en contactarnos.

**Correo Electrónico:**
[marbinsecagomez@gmail.com](mailto:herramientas.financieras.app@gmail.com)

**¡Tu feedback nos ayuda a mejorar!**
""")

st.markdown("---")

# --- Nota Legal/Descargo de Responsabilidad (Opcional, pero recomendable) ---
st.header("Descargo de Responsabilidad")
st.markdown("""
**Importante:** Las calculadoras y la información proporcionada en esta aplicación tienen fines **meramente educativos e informativos**. No constituyen asesoramiento financiero, de inversión, fiscal o legal. Te recomendamos encarecidamente consultar a un profesional cualificado antes de tomar cualquier decisión financiera importante. No asumimos responsabilidad alguna por las decisiones tomadas con base en la información o los cálculos presentados aquí.
""")

st.markdown("---")

# --- Botón para regresar a Home.py (en el cuerpo principal) ---
col_back1, col_back2, col_back3 = st.columns([1, 2, 1])

with col_back2:
    if st.button("Volver a Herramientas Financieras", key="back_to_home_about"):
        st.switch_page("HOME.py")

# --- Información Adicional/Ayuda y Navegación (en la barra lateral) ---
st.sidebar.header("Conoce más")
st.sidebar.info(
    "Explora nuestra misión y cómo estas herramientas pueden ayudarte en tu camino financiero."
)