import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

st.set_page_config(page_title="Calculadora de Amortización", page_icon="images/finance.png", layout="centered")

st.title("📊 Calculadora de Amortización")
st.markdown("""
    Calcula tu tabla de amortización detallada para préstamos y descárgala en formato Excel.
""")

st.divider()

# --- Inputs de la calculadora ---
st.header("Datos del Préstamo")

# Usamos st.session_state para controlar los valores de los inputs
# Inicializamos los valores por defecto si no existen en session_state
if 'principal_amort' not in st.session_state:
    st.session_state.principal_amort = 50000.0
if 'annual_interest_rate_amort' not in st.session_state:
    st.session_state.annual_interest_rate_amort = 5.0
if 'loan_term_months_amort' not in st.session_state:
    st.session_state.loan_term_months_amort = 60
if 'payment_frequency_amort' not in st.session_state:
    st.session_state.payment_frequency_amort = "Mensual"

# Aseguramos que 'df_amortization_result' y 'payment_amount_result' siempre existan en session_state, incluso si es None
if 'df_amortization_result' not in st.session_state:
    st.session_state.df_amortization_result = None
if 'payment_amount_result' not in st.session_state:
    st.session_state.payment_amount_result = None

principal = st.number_input(
    "**Monto del Préstamo (Capital Inicial)**",
    min_value=100.0,
    max_value=100000000.0,
    value=st.session_state.principal_amort,
    key='principal_input_amort',
    step=1000.0,
    format="%.2f",
    help="El monto total del dinero prestado."
)

annual_interest_rate = st.number_input(
    "**Tasa de Interés Anual (%)**",
    min_value=0.1,
    max_value=100.0,
    value=st.session_state.annual_interest_rate_amort,
    key='annual_interest_input_amort',
    step=0.1,
    format="%.2f",
    help="La tasa de interés nominal anual del préstamo."
)

loan_term_months = st.number_input(
    "**Plazo del Préstamo (meses)**",
    min_value=1,
    max_value=600,
    value=st.session_state.loan_term_months_amort,
    key='loan_term_input_amort',
    step=1,
    help="El número total de meses para pagar el préstamo."
)

payment_frequency = st.selectbox(
    "**Frecuencia de Pago**",
    options=["Mensual", "Bimestral", "Trimestral", "Semestral", "Anual"],
    index=["Mensual", "Bimestral", "Trimestral", "Semestral", "Anual"].index(st.session_state.payment_frequency_amort),
    key='payment_frequency_input_amort',
    help="Define la periodicidad con la que se realizarán los pagos."
)

st.divider()

# --- Funciones de control de estado ---
def calculate_amortization():
    # Guarda los inputs actuales en session_state
    st.session_state.principal_amort = principal
    st.session_state.annual_interest_rate_amort = annual_interest_rate
    st.session_state.loan_term_months_amort = loan_term_months
    st.session_state.payment_frequency_amort = payment_frequency

    try:
        num_payments_total = loan_term_months

        if payment_frequency == "Mensual":
            num_payments = num_payments_total
            periodic_interest_rate = (annual_interest_rate / 100) / 12
        elif payment_frequency == "Bimestral":
            num_payments = num_payments_total / 2
            periodic_interest_rate = (annual_interest_rate / 100) / 6
        elif payment_frequency == "Trimestral":
            num_payments = num_payments_total / 3
            periodic_interest_rate = (annual_interest_rate / 100) / 4
        elif payment_frequency == "Semestral":
            num_payments = num_payments_total / 6
            periodic_interest_rate = (annual_interest_rate / 100) / 2
        elif payment_frequency == "Anual":
            num_payments = num_payments_total / 12
            periodic_interest_rate = (annual_interest_rate / 100) / 1
        
        num_payments = int(np.ceil(num_payments))

        if num_payments <= 0:
            st.error("El número de pagos debe ser al menos 1. Ajusta el plazo o la frecuencia.")
            st.session_state.df_amortization_result = None
            st.session_state.payment_amount_result = None
            return

        if periodic_interest_rate == 0:
            payment_amount = principal / num_payments
        else:
            denominator = 1 - (1 + periodic_interest_rate)**(-num_payments)
            if denominator == 0:
                st.error("Error en el cálculo de la cuota fija. La tasa de interés o el plazo pueden ser inválidos.")
                st.session_state.df_amortization_result = None
                st.session_state.payment_amount_result = None
                return
            payment_amount = (principal * periodic_interest_rate) / denominator

        st.session_state.payment_amount_result = payment_amount

        amortization_data = []
        remaining_principal = principal

        for i in range(1, int(num_payments) + 1):
            current_period_initial_principal = remaining_principal

            interest_payment = current_period_initial_principal * periodic_interest_rate
            principal_payment = payment_amount - interest_payment

            if i == num_payments:
                principal_payment = current_period_initial_principal
                payment_amount = principal_payment + interest_payment
                remaining_principal = 0.0
            else:
                remaining_principal -= principal_payment

            amortization_data.append({
                "Período": i,
                # --- CAMBIO CLAVE AQUÍ: Formatear como entero (sin .2f) ---
                "Capital Inicial del Período": f"{round(current_period_initial_principal):,}",
                "Cuota Fija": f"{round(payment_amount):,}",
                "Intereses": f"{round(interest_payment):,}",
                "Capital Amortizado": f"{round(principal_payment):,}",
                "Capital Pendiente": f"{round(remaining_principal):,}"
            })

        df_amortization = pd.DataFrame(amortization_data)
        st.session_state.df_amortization_result = df_amortization

    except Exception as e:
        st.error(f"Ocurrió un error al calcular la tabla de amortización. Por favor, revisa los valores ingresados. Detalles: {e}")
        st.session_state.df_amortization_result = None
        st.session_state.payment_amount_result = None


def reset_amortization():
    st.session_state.principal_amort = 50000.0
    st.session_state.annual_interest_rate_amort = 5.0
    st.session_state.loan_term_months_amort = 60
    st.session_state.payment_frequency_amort = "Mensual"
    st.session_state.df_amortization_result = None
    st.session_state.payment_amount_result = None


# --- Estilo para los botones ---
st.markdown(
    """
    <style>
    /* Estilo general para los botones principales */
    .stButton > button {
        display: block;
        margin: 0 auto;
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
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Botones de Acción (Generar y Limpiar) ---
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.button("Generar Tabla", on_click=calculate_amortization)

with col3:
    st.button("Limpiar Valores", on_click=reset_amortization)

# --- Salida de la Cuota Fija ---
if st.session_state.payment_amount_result is not None:
    st.markdown("---")
    # --- CAMBIO CLAVE AQUÍ: Formatear como entero (sin .2f) ---
    st.success(f"**Cuota Fija Periódica:** $ {round(st.session_state.payment_amount_result):,}")
    st.markdown("---")

# --- Mostrar Resultados de la Tabla (si existen en session_state) ---
if st.session_state.df_amortization_result is not None:
    st.subheader("Detalle de la Tabla de Amortización")
    st.dataframe(st.session_state.df_amortization_result)

    # --- Botón para descargar Excel ---
    @st.cache_data
    def to_excel(df):
        output = BytesIO()
        df_for_excel = df.copy()
        for col in ["Capital Inicial del Período", "Cuota Fija", "Intereses", "Capital Amortizado", "Capital Pendiente"]:
            if col in df_for_excel.columns:
                # Remove any formatting (like commas) and convert back to numeric
                # Since they are strings now like "1,234", we need to remove comma before converting to float/int
                df_for_excel[col] = df_for_excel[col].str.replace(',', '').astype(float) # Keep as float for excel
        
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_for_excel.to_excel(writer, index=False, sheet_name='Amortizacion')
        writer.close()
        processed_data = output.getvalue()
        return processed_data

    excel_data = to_excel(st.session_state.df_amortization_result)
    st.download_button(
        label="Descargar Tabla en Excel",
        data=excel_data,
        file_name="tabla_amortizacion.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        help="Descarga la tabla de amortización completa como un archivo de Excel."
    )

st.markdown("---")

# --- Botón para regresar a Home.py (en el cuerpo principal) ---
col_back1, col_back2, col_back3 = st.columns([1, 2, 1])

with col_back2:
    if st.button("Volver a Home", key="back_to_home_amort"):
        st.switch_page("Home.py")

# --- Información Adicional/Ayuda y Navegación (en la barra lateral) ---
st.sidebar.header("Acerca de esta Calculadora")
st.sidebar.info(
    "Esta herramienta te permite generar una tabla de amortización detallada para tu préstamo. "
    "Muestra cómo cada pago se divide entre capital e intereses a lo largo del tiempo."
)