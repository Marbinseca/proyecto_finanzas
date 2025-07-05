import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

st.set_page_config(page_title="Calculadora de Interés Compuesto", page_icon="images/finance.png", layout="centered")

st.title("📈 Calculadora de Interés Compuesto")
st.markdown("""
    Proyecta el crecimiento de tus inversiones con interés compuesto,
    considerando aportes iniciales y periódicos.
""")

st.divider()

# --- Inputs de la calculadora ---
st.header("Datos de la Inversión")

# Usamos st.session_state para controlar los valores de los inputs
if 'initial_investment' not in st.session_state:
    st.session_state.initial_investment = 10000.0
if 'annual_contribution' not in st.session_state:
    st.session_state.annual_contribution = 100.0
if 'annual_interest_rate_ic' not in st.session_state:
    st.session_state.annual_interest_rate_ic = 7.0
if 'investment_term_years' not in st.session_state:
    st.session_state.investment_term_years = 10
if 'compounding_frequency_ic' not in st.session_state:
    st.session_state.compounding_frequency_ic = "Mensual"
if 'contribution_frequency' not in st.session_state:
    st.session_state.contribution_frequency = "Mensual"

# Aseguramos que 'df_compound_result' y 'final_value_result' siempre existan en session_state
if 'df_compound_result' not in st.session_state:
    st.session_state.df_compound_result = None
if 'final_value_result' not in st.session_state:
    st.session_state.final_value_result = None
if 'total_invested_result' not in st.session_state:
    st.session_state.total_invested_result = None
if 'total_interest_result' not in st.session_state:
    st.session_state.total_interest_result = None


initial_investment = st.number_input(
    "**Monto de Inversión Inicial**",
    min_value=0.0,
    max_value=100000000.0,
    value=st.session_state.initial_investment,
    key='initial_investment_input',
    step=100.0,
    format="%.2f",
    help="El capital inicial que se invierte."
)

annual_contribution = st.number_input(
    "**Aporte Periódico (Anual)**",
    min_value=0.0,
    max_value=1000000.0,
    value=st.session_state.annual_contribution,
    key='annual_contribution_input',
    step=10.0,
    format="%.2f",
    help="Monto que se añade a la inversión cada año."
)

annual_interest_rate = st.number_input(
    "**Tasa de Interés Anual (%)**",
    min_value=0.1,
    max_value=100.0,
    value=st.session_state.annual_interest_rate_ic,
    key='annual_interest_input_ic',
    step=0.1,
    format="%.2f",
    help="La tasa de rendimiento anual esperada de la inversión."
)

investment_term_years = st.number_input(
    "**Plazo de la Inversión (años)**",
    min_value=1,
    max_value=100,
    value=st.session_state.investment_term_years,
    key='investment_term_input',
    step=1,
    help="El número total de años que durará la inversión."
)

compounding_frequency = st.selectbox(
    "**Frecuencia de Capitalización**",
    options=["Anual", "Semestral", "Trimestral", "Mensual", "Diario"],
    index=["Anual", "Semestral", "Trimestral", "Mensual", "Diario"].index(st.session_state.compounding_frequency_ic),
    key='compounding_freq_ic',
    help="La frecuencia con la que los intereses se suman al capital."
)

contribution_frequency = st.selectbox(
    "**Frecuencia del Aporte**",
    options=["Anual", "Semestral", "Trimestral", "Mensual", "Ninguno"],
    index=["Anual", "Semestral", "Trimestral", "Mensual", "Ninguno"].index(st.session_state.contribution_frequency),
    key='contribution_freq_ic',
    help="La frecuencia con la que se realizan los aportes adicionales. 'Anual' significa el monto total del 'Aporte Periódico (Anual)'."
)

st.divider()

# --- Funciones de cálculo ---

def calculate_compound_interest():
    # Guarda los inputs actuales en session_state
    st.session_state.initial_investment = initial_investment
    st.session_state.annual_contribution = annual_contribution
    st.session_state.annual_interest_rate_ic = annual_interest_rate
    st.session_state.investment_term_years = investment_term_years
    st.session_state.compounding_frequency_ic = compounding_frequency
    st.session_state.contribution_frequency = contribution_frequency

    try:
        rate_decimal = annual_interest_rate / 100

        # Determinar periodos de capitalización por año (m)
        if compounding_frequency == "Anual":
            m = 1
        elif compounding_frequency == "Semestral":
            m = 2
        elif compounding_frequency == "Trimestral":
            m = 4
        elif compounding_frequency == "Mensual":
            m = 12
        elif compounding_frequency == "Diario":
            m = 365
        else: # Default a Mensual si hay un valor inesperado
            m = 12
        
        # Tasa de interés periódica
        periodic_rate = rate_decimal / m
        
        # Determinar frecuencia de aportes
        if contribution_frequency == "Anual":
            contribution_multiplier = 1
        elif contribution_frequency == "Semestral":
            contribution_multiplier = 2
        elif contribution_frequency == "Trimestral":
            contribution_multiplier = 4
        elif contribution_frequency == "Mensual":
            contribution_multiplier = 12
        elif contribution_frequency == "Ninguno":
            contribution_multiplier = 0 # No hay aportes periódicos

        # Calcular el aporte periódico real si no es anual
        # annual_contribution es el monto TOTAL anual. Si se hace mensual, se divide.
        periodic_contribution_amount = 0
        if contribution_multiplier > 0:
            periodic_contribution_amount = annual_contribution / contribution_multiplier


        data = []
        current_balance = initial_investment
        total_contributed = initial_investment # Suma de la inversión inicial y los aportes periódicos
        
        # Convertir el plazo total a número de periodos de capitalización
        total_compounding_periods = investment_term_years * m

        # Ajustar el total de aportes adicionales
        total_additional_contributions = 0


        for year in range(1, investment_term_years + 1):
            balance_start_of_year = current_balance
            interests_this_year = 0
            contributions_this_year = 0

            for period_in_year in range(1, m + 1): # Bucle para cada período de capitalización dentro del año
                # Calcular interés del período
                interest_for_period = current_balance * periodic_rate
                interests_this_year += interest_for_period
                current_balance += interest_for_period

                # Añadir aportes periódicos si aplica
                # Sólo añade si el periodo actual es un multiplo de la frecuencia de aporte
                if contribution_multiplier > 0 and (period_in_year % (m / contribution_multiplier) == 0):
                    current_balance += periodic_contribution_amount
                    contributions_this_year += periodic_contribution_amount
                    total_additional_contributions += periodic_contribution_amount

            total_contributed += contributions_this_year # Suma los aportes del año al total
            
            data.append({
                "Año": year,
                "Saldo Inicial del Año": f"{round(balance_start_of_year):,}",
                "Aportes del Año": f"{round(contributions_this_year):,}",
                "Intereses Ganados en el Año": f"{round(interests_this_year):,}",
                "Saldo Final del Año": f"{round(current_balance):,}"
            })

        df_compound = pd.DataFrame(data)
        st.session_state.df_compound_result = df_compound
        st.session_state.final_value_result = current_balance
        st.session_state.total_invested_result = initial_investment + total_additional_contributions
        st.session_state.total_interest_result = current_balance - (initial_investment + total_additional_contributions)


    except Exception as e:
        st.error(f"Ocurrió un error al calcular el interés compuesto. Por favor, revisa los valores ingresados. Detalles: {e}")
        st.session_state.df_compound_result = None
        st.session_state.final_value_result = None
        st.session_state.total_invested_result = None
        st.session_state.total_interest_result = None


def reset_compound():
    st.session_state.initial_investment = 10000.0
    st.session_state.annual_contribution = 100.0
    st.session_state.annual_interest_rate_ic = 7.0
    st.session_state.investment_term_years = 10
    st.session_state.compounding_frequency_ic = "Mensual"
    st.session_state.contribution_frequency = "Mensual"
    st.session_state.df_compound_result = None
    st.session_state.final_value_result = None
    st.session_state.total_invested_result = None
    st.session_state.total_interest_result = None


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
    st.button("Calcular Proyección", on_click=calculate_compound_interest)

with col3:
    st.button("Limpiar Valores", on_click=reset_compound)

# --- Salida de los Resultados ---
if st.session_state.final_value_result is not None:
    st.markdown("---")
    st.success(f"**Valor Futuro de la Inversión:** $ {round(st.session_state.final_value_result):,}")
    st.info(f"**Capital Total Aportado:** $ {round(st.session_state.total_invested_result):,}")
    st.info(f"**Intereses Totales Ganados:** $ {round(st.session_state.total_interest_result):,}")
    st.markdown("---")

# --- Mostrar Resultados de la Tabla (si existen en session_state) ---
if st.session_state.df_compound_result is not None:
    st.subheader("Detalle del Crecimiento Anual")
    st.dataframe(st.session_state.df_compound_result, height=300) # Altura fija para la tabla

    # --- Botón para descargar Excel ---
    @st.cache_data
    def to_excel_compound(df):
        output = BytesIO()
        df_for_excel = df.copy()
        # Convertir columnas numéricas a float antes de exportar
        for col in ["Saldo Inicial del Año", "Aportes del Año", "Intereses Ganados en el Año", "Saldo Final del Año"]:
            if col in df_for_excel.columns:
                df_for_excel[col] = df_for_excel[col].str.replace(',', '').astype(float)
        
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_for_excel.to_excel(writer, index=False, sheet_name='Interes_Compuesto')
        writer.close()
        processed_data = output.getvalue()
        return processed_data

    excel_data_compound = to_excel_compound(st.session_state.df_compound_result)
    st.download_button(
        label="Descargar Proyección en Excel",
        data=excel_data_compound,
        file_name="proyeccion_interes_compuesto.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        help="Descarga la tabla de proyección de interés compuesto como un archivo de Excel."
    )

st.markdown("---")

# --- Botón para regresar a Home.py (en el cuerpo principal) ---
col_back1, col_back2, col_back3 = st.columns([1, 2, 1])

with col_back2:
    if st.button("Volver a Herramientas Financieras", key="back_to_home_compound"):
        st.switch_page("HOME.py")

# --- Información Adicional/Ayuda y Navegación (en la barra lateral) ---
st.sidebar.header("Acerca de esta Calculadora")
st.sidebar.info(
    "Esta herramienta te ayuda a visualizar el poder del interés compuesto. "
    "Puedes proyectar cómo crecerá tu dinero con una inversión inicial y aportes periódicos. "
    "¡Pequeños aportes constantes pueden generar grandes resultados a largo plazo!"
)