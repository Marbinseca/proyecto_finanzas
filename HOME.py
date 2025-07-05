import streamlit as st

st.set_page_config(page_title="Herramientas Financieras", page_icon="images/finance.png", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
    /* Estilos Generales */
    .main {
        /* Nuevo degradado de fondo: de un azul claro a un morado suave */
        background: linear-gradient(to right, #e0f2f7, #e6e6fa); /* Colores: Light Blue (muy claro) a Lavender (muy claro) */
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stApp {
        font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        color: #343a40;
    }

    /* Títulos y Subtítulos */
    h1 {
        font-size: 3.5rem;
        font-weight: 700;
        color: #1a202c;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -0.05em;
        /* Degradado en el texto para el título, ajustado para combinar con el nuevo fondo */
        background: -webkit-linear-gradient(45deg, #4a69bd, #6a5acd); /* Azul medio a Púrpura medio */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    p {
        font-size: 1.2rem;
        color: #555c6e;
        text-align: center;
        margin-bottom: 3rem;
        line-height: 1.6;
    }

    /* Estilos para las tarjetas de herramientas */
    .card {
        background: #ffffff;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        padding: 2.5rem 2rem;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 100%;
        border: 1px solid #e0e0e0;
        margin-bottom: 2rem; /* Mantener un margen inferior para separar las filas de tarjetas */
    }
    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
    }
    .card-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2d3a4b;
        margin-bottom: 1.5rem;
        letter-spacing: -0.02em;
    }
    .card-link {
        display: inline-block;
        font-size: 1.1rem;
        font-weight: 600;
        /* Color del botón ajustado para combinar con el nuevo esquema */
        color: #4a69bd; /* Un azul similar al del degradado del título */
        text-decoration: none;
        padding: 0.8rem 1.5rem;
        border: 2px solid #4a69bd;
        border-radius: 50px;
        transition: all 0.3s ease;
    }
    .card-link:hover {
        background-color: #4a69bd; /* El botón se rellena con el azul al pasar el mouse */
        color: white;
        text-decoration: none;
        transform: scale(1.05);
    }

    /* Separador decorativo */
    .divider-fancy {
        width: 80px;
        height: 4px;
        /* Color del separador ajustado */
        background-color: #6a5acd; /* Un morado similar al del degradado del título */
        border-radius: 2px;
        margin: 2rem auto 4rem auto;
    }

    /* Footer sutil */
    .footer {
        text-align: center;
        padding-top: 3rem;
        color: #7f8c8d;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Añadir imagen a la barra lateral ---
st.sidebar.image("images/finance.png", use_container_width=True)

# Puedes añadir un título o slogan debajo de la imagen si quieres
st.sidebar.markdown("<h3 style='text-align: center; color: #4a69bd;'>Herramientas Pro</h3>", unsafe_allow_html=True)
st.sidebar.markdown("---") # Un separador sutil

# --- Contenido Principal ---
st.markdown("<h1 class='animate__animated animate__fadeInDown'>Herramientas Financieras</h1>", unsafe_allow_html=True)
st.markdown("<p>Accede a nuestras calculadoras financieras especializadas para optimizar tus decisiones.</p>", unsafe_allow_html=True)

# Separador decorativo
st.markdown("<div class='divider-fancy'></div>", unsafe_allow_html=True)

# --- Tarjetas de Herramientas ---

# Primera fila de dos tarjetas
col1, col2 = st.columns(2, gap="large") # Dos columnas para la primera fila

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Calculadora TIR y VAN</div>
            <a class="card-link" href="/TIR" target="_self">Ir a la calculadora</a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Calculadora de Amortización</div>
            <a class="card-link" href="/AMORTIZACION" target="_self">Ir a la calculadora</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Segunda fila de dos tarjetas
col3, col4 = st.columns(2, gap="large") # Dos columnas para la segunda fila

with col3:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Calculadora de Tasas de Interes</div>
            <a class="card-link" href="/TASAS" target="_self">Ir a la calculadora</a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Conceptos y Fórmulas empleados en las Calculadoras</div>
            <a class="card-link" href="/TEORIA" target="_self">Explorar</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("""
<div class="footer">
    © 2025 Herramientas Financieras. Todos los derechos reservados.
</div>
""", unsafe_allow_html=True)