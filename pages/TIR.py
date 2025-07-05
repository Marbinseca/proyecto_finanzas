import streamlit as st
import numpy_financial as npf

st.set_page_config(page_title="Calculadora TIR y VAN", page_icon="images/finance.png", layout="centered")

st.title("📊 Calculadora de TIR y VAN")
st.markdown("""
    Calcula la **Tasa Interna de Retorno (TIR)** y el **Valor Actual Neto (VAN)**
    para evaluar la viabilidad de tus proyectos de inversión.
""")

st.divider()

# --- Inputs de la calculadora ---
st.header("Datos de la Inversión")

# Usamos st.session_state para controlar los valores de los inputs
# Inicializamos los valores por defecto si no existen en session_state
if 'initial_investment_tir' not in st.session_state:
    st.session_state.initial_investment_tir = -10000.0
if 'cf1_tir' not in st.session_state:
    st.session_state.cf1_tir = 3000.0
if 'cf2_tir' not in st.session_state:
    st.session_state.cf2_tir = 4000.0
if 'cf3_tir' not in st.session_state:
    st.session_state.cf3_tir = 5000.0
if 'cf4_tir' not in st.session_state:
    st.session_state.cf4_tir = 6000.0
if 'discount_rate_tir' not in st.session_state:
    st.session_state.discount_rate_tir = 10.0

# Inversión Inicial
initial_investment = st.number_input(
    "**Inversión Inicial** (valor negativo, ej: -10000)",
    min_value=-10000000000.0,
    max_value=0.0,
    value=st.session_state.initial_investment_tir, # Usar valor de session_state
    key='initial_investment_input_tir', # Clave única
    step=1000.0,
    format="%.2f",
    help="El desembolso inicial del proyecto. Debe ser un valor negativo."
)

st.subheader("Flujos de Caja Futuros")

# Flujos de Caja individuales
cash_flow_1 = st.number_input(
    "**Flujo de Caja Año 1**",
    value=st.session_state.cf1_tir,
    key='cf1_input_tir',
    step=100.0,
    format="%.2f",
    help="Ganancia o pérdida del proyecto en el Año 1."
)
cash_flow_2 = st.number_input(
    "**Flujo de Caja Año 2**",
    value=st.session_state.cf2_tir,
    key='cf2_input_tir',
    step=100.0,
    format="%.2f",
    help="Ganancia o pérdida del proyecto en el Año 2."
)
cash_flow_3 = st.number_input(
    "**Flujo de Caja Año 3**",
    value=st.session_state.cf3_tir,
    key='cf3_input_tir',
    step=100.0,
    format="%.2f",
    help="Ganancia o pérdida del proyecto en el Año 3."
)
cash_flow_4 = st.number_input(
    "**Flujo de Caja Año 4**",
    value=st.session_state.cf4_tir,
    key='cf4_input_tir',
    step=100.0,
    format="%.2f",
    help="Ganancia o pérdida del proyecto en el Año 4."
)

st.subheader("Tasa de Descuento")
discount_rate_input_percentage = st.slider(
    "**Tasa de Descuento Anual (%)**",
    min_value=0.0,
    max_value=50.0,
    value=st.session_state.discount_rate_tir,
    key='discount_rate_input_tir',
    step=0.1,
    format="%.1f %%",
    help="La tasa de interés o rentabilidad mínima que esperas del proyecto."
)
discount_rate_for_calculation = discount_rate_input_percentage / 100

st.divider()

# --- Funciones de control de estado ---
def calculate_tir_van():
    st.session_state.initial_investment_tir = initial_investment
    st.session_state.cf1_tir = cash_flow_1
    st.session_state.cf2_tir = cash_flow_2
    st.session_state.cf3_tir = cash_flow_3
    st.session_state.cf4_tir = cash_flow_4
    st.session_state.discount_rate_tir = discount_rate_input_percentage

    if initial_investment > 0:
        st.error("La Inversión Inicial debe ser un valor negativo (desembolso).")
        if 'tir_result' in st.session_state: del st.session_state.tir_result
        if 'van_result' in st.session_state: del st.session_state.van_result
    else:
        cash_flows = [initial_investment, cash_flow_1, cash_flow_2, cash_flow_3, cash_flow_4]
        try:
            tir = npf.irr(cash_flows) * 100
            van = npf.npv(discount_rate_for_calculation, cash_flows)
            st.session_state.tir_result = tir
            st.session_state.van_result = van
            st.session_state.tir_comparison_rate = discount_rate_input_percentage

        except Exception as e:
            st.error(f"Ocurrió un error al calcular la TIR o el VAN. Asegúrate de que los flujos de caja son válidos (por ejemplo, debe haber al menos un flujo positivo después de la inversión inicial negativa para calcular la TIR). Detalles del error: {e}")
            if 'tir_result' in st.session_state: del st.session_state.tir_result
            if 'van_result' in st.session_state: del st.session_state.van_result

def reset_tir_van():
    st.session_state.initial_investment_tir = -10000.0
    st.session_state.cf1_tir = 3000.0
    st.session_state.cf2_tir = 4000.0
    st.session_state.cf3_tir = 5000.0
    st.session_state.cf4_tir = 6000.0
    st.session_state.discount_rate_tir = 10.0
    if 'tir_result' in st.session_state:
        del st.session_state.tir_result
    if 'van_result' in st.session_state:
        del st.session_state.van_result

# --- Estilo para los botones ---
st.markdown(
    """
    <style>
    /* Estilo general para los botones principales */
    .stButton > button {
        display: block;
        margin: 0 auto; /* Centra los botones en sus columnas */
        border: 2px solid #4a69bd;
        border-radius: 50px;
        background-color: transparent;
        color: #4a69bd;
        font-weight: 600;
        padding: 0.8rem 1.5rem;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #4a69bd;
        color: white;
        transform: scale(1.05);
    }
    /* Estilo específico para el botón de regreso, si se necesita un ajuste extra */
    .stButton.back-button > button {
        margin-top: 20px; /* Espacio superior para separarlo de otros elementos */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Botones de Acción (Calcular y Limpiar) ---
# Reorganizados en una sola fila con tres columnas para centrar mejor
col1, col2, col3 = st.columns([1, 1, 1]) # Ajusta las proporciones si es necesario

with col1:
    # Botón de cálculo
    st.button("Calcular TIR y VAN", on_click=calculate_tir_van)

with col3: # Colocamos el botón de limpiar en la tercera columna
    # Botón "Limpiar"
    st.button("Limpiar Valores", on_click=reset_tir_van)

# --- Mostrar Resultados (si existen en session_state) ---
if 'tir_result' in st.session_state and 'van_result' in st.session_state:
    st.success("Cálculos Realizados con Éxito:")
    st.metric(label="**Tasa Interna de Retorno (TIR)**", value=f"{st.session_state.tir_result:.2f} %")
    st.metric(label="**Valor Actual Neto (VAN)**", value=f"{st.session_state.van_result:.2f}")

    st.markdown("---")
    st.subheader("Interpretación de Resultados:")
    if st.session_state.van_result > 0:
        st.info(f"**El VAN ({st.session_state.van_result:.2f}) es positivo.** El proyecto es financieramente atractivo y debería aceptarse, ya que se espera que genere ganancias por encima de la tasa de descuento.")
    elif st.session_state.van_result < 0:
        st.warning(f"**El VAN ({st.session_state.van_result:.2f}) es negativo.** El proyecto no es rentable a la tasa de descuento dada y debería rechazarse.")
    else:
        st.info(f"**El VAN es cero.** El proyecto es indiferente, ya que solo cubriría la tasa de descuento esperada.")

    if st.session_state.tir_result > st.session_state.tir_comparison_rate:
        st.info(f"**La TIR ({st.session_state.tir_result:.2f}%) es mayor que la tasa de descuento ({st.session_state.tir_comparison_rate:.1f}%).** Esto refuerza que el proyecto es viable y rentable.")
    else:
        st.warning(f"**La TIR ({st.session_state.tir_result:.2f}%) es menor o igual que la tasa de descuento ({st.session_state.tir_comparison_rate:.1f}%).** El proyecto podría no ser rentable o apenas cubriría el costo de oportunidad.")

st.markdown("---") # Un separador antes del botón de regreso

# --- Botón para regresar a Home.py (en el cuerpo principal) ---
# Usamos un contenedor de columnas para centrar el botón de regreso
col_back1, col_back2, col_back3 = st.columns([1, 2, 1]) # Ajusta las proporciones para centrarlo

with col_back2: # Colocamos el botón en la columna central
    if st.button("Volver a Home", key="back_to_home_tir", help="Regresar a la página principal de herramientas financieras."):
        st.switch_page("HOME.py")

# --- Información Adicional/Ayuda y Navegación (en la barra lateral) ---
st.sidebar.header("Acerca de esta Calculadora")
st.sidebar.info(
    "Esta herramienta te ayuda a evaluar proyectos de inversión usando dos métricas financieras clave: "
    "la **Tasa Interna de Retorno (TIR)** y el **Valor Actual Neto (VAN)**. "
    "Recuerda que la **Inversión Inicial** debe ser un valor negativo (un egreso)."
)

# NOTA: El botón "Volver a Herramientas Financieras" en el sidebar está comentado para evitar duplicidad.
# if st.sidebar.button("Volver a Herramientas Financieras"):
#    st.switch_page("Home.py")