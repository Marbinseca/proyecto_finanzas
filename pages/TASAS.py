import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Calculadora de Tasas de Interés", page_icon="images/finance.png", layout="centered")

st.title("🔄 Calculadora de Tasas de Interés")
st.markdown("""
    Convierte tasas de interés entre nominales y efectivas con diferentes frecuencias.
""")

st.divider()

# --- Funciones de cálculo de tasas ---

def nominal_to_effective_annual(nominal_rate, compounding_frequency):
    """Convierte una tasa nominal a Tasa Efectiva Anual (TEA)."""
    if compounding_frequency == "Anual":
        periods_per_year = 1
    elif compounding_frequency == "Semestral":
        periods_per_year = 2
    elif compounding_frequency == "Cuatrimestral": # Agregamos cuatrimestral
        periods_per_year = 3
    elif compounding_frequency == "Trimestral":
        periods_per_year = 4
    elif compounding_frequency == "Bimestral":
        periods_per_year = 6
    elif compounding_frequency == "Mensual":
        periods_per_year = 12
    elif compounding_frequency == "Quincenal": # Agregamos quincenal
        periods_per_year = 24
    elif compounding_frequency == "Diario": # Agregamos diario
        periods_per_year = 365

    if periods_per_year == 0:
        return np.nan # Evitar división por cero

    periodic_rate = nominal_rate / periods_per_year
    tea = (1 + periodic_rate)**periods_per_year - 1
    return tea

def effective_annual_to_nominal(tea, compounding_frequency):
    """Convierte Tasa Efectiva Anual (TEA) a tasa nominal."""
    if compounding_frequency == "Anual":
        periods_per_year = 1
    elif compounding_frequency == "Semestral":
        periods_per_year = 2
    elif compounding_frequency == "Cuatrimestral":
        periods_per_year = 3
    elif compounding_frequency == "Trimestral":
        periods_per_year = 4
    elif compounding_frequency == "Bimestral":
        periods_per_year = 6
    elif compounding_frequency == "Mensual":
        periods_per_year = 12
    elif compounding_frequency == "Quincenal":
        periods_per_year = 24
    elif compounding_frequency == "Diario":
        periods_per_year = 365

    if periods_per_year == 0:
        return np.nan # Evitar división por cero

    nominal_rate = periods_per_year * ((1 + tea)**(1/periods_per_year) - 1)
    return nominal_rate

def effective_periodic_to_effective_annual(effective_periodic_rate, periodic_frequency):
    """Convierte una tasa efectiva periódica a Tasa Efectiva Anual (TEA)."""
    if periodic_frequency == "Anual":
        periods_per_year = 1
    elif periodic_frequency == "Semestral":
        periods_per_year = 2
    elif periodic_frequency == "Cuatrimestral":
        periods_per_year = 3
    elif periodic_frequency == "Trimestral":
        periods_per_year = 4
    elif periodic_frequency == "Bimestral":
        periods_per_year = 6
    elif periodic_frequency == "Mensual":
        periods_per_year = 12
    elif periodic_frequency == "Quincenal":
        periods_per_year = 24
    elif periodic_frequency == "Diario":
        periods_per_year = 365

    tea = (1 + effective_periodic_rate)**periods_per_year - 1
    return tea

def effective_annual_to_effective_periodic(tea, periodic_frequency):
    """Convierte Tasa Efectiva Anual (TEA) a tasa efectiva periódica."""
    if periodic_frequency == "Anual":
        periods_per_year = 1
    elif periodic_frequency == "Semestral":
        periods_per_year = 2
    elif periodic_frequency == "Cuatrimestral":
        periods_per_year = 3
    elif periodic_frequency == "Trimestral":
        periods_per_year = 4
    elif periodic_frequency == "Bimestral":
        periods_per_year = 6
    elif periodic_frequency == "Mensual":
        periods_per_year = 12
    elif periodic_frequency == "Quincenal":
        periods_per_year = 24
    elif periodic_frequency == "Diario":
        periods_per_year = 365
    
    if periods_per_year == 0:
        return np.nan # Evitar división por cero

    effective_periodic_rate = (1 + tea)**(1/periods_per_year) - 1
    return effective_periodic_rate

# --- Opciones de Frecuencia ---
frequency_options_compounding = ["Anual", "Semestral", "Cuatrimestral", "Trimestral", "Bimestral", "Mensual", "Quincenal", "Diario"]
frequency_options_periodic = ["Anual", "Semestral", "Cuatrimestral", "Trimestral", "Bimestral", "Mensual", "Quincenal", "Diario"]


st.header("Convertidor de Tasas")

# --- Selectores de conversión ---
conversion_type = st.radio(
    "**Selecciona el tipo de conversión:**",
    ["Nominal a Efectiva Anual (TEA)", "Efectiva Anual (TEA) a Nominal",
     "Efectiva Periódica a Efectiva Anual (TEA)", "Efectiva Anual (TEA) a Efectiva Periódica"]
)

# --- Controles para Nominal a Efectiva Anual ---
if conversion_type == "Nominal a Efectiva Anual (TEA)":
    st.subheader("Nominal a Efectiva Anual (TEA)")
    nominal_rate_input_n2e = st.number_input(
        "**Tasa Nominal Anual (%)**",
        min_value=0.0,
        max_value=500.0,
        value=5.0,
        step=0.1,
        format="%.2f",
        help="La tasa nominal anual a convertir."
    )
    compounding_frequency_n2e = st.selectbox(
        "**Frecuencia de Capitalización de la Tasa Nominal**",
        options=frequency_options_compounding,
        index=5, # Mensual
        key='compounding_freq_n2e',
        help="La periodicidad con la que se capitaliza la tasa nominal."
    )

    if st.button("Calcular TEA"):
        try:
            nominal_rate_decimal = nominal_rate_input_n2e / 100
            tea_calculated = nominal_to_effective_annual(nominal_rate_decimal, compounding_frequency_n2e)
            st.success(f"**Tasa Efectiva Anual (TEA):** {tea_calculated * 100:,.4f}%")
        except Exception as e:
            st.error(f"Error al calcular: {e}")

# --- Controles para Efectiva Anual a Nominal ---
elif conversion_type == "Efectiva Anual (TEA) a Nominal":
    st.subheader("Efectiva Anual (TEA) a Nominal")
    tea_input_e2n = st.number_input(
        "**Tasa Efectiva Anual (TEA) (%)**",
        min_value=0.0,
        max_value=500.0,
        value=5.0,
        step=0.1,
        format="%.2f",
        help="La Tasa Efectiva Anual (TEA) a convertir."
    )
    compounding_frequency_e2n = st.selectbox(
        "**Frecuencia de Capitalización para la Tasa Nominal Resultante**",
        options=frequency_options_compounding,
        index=5, # Mensual
        key='compounding_freq_e2n',
        help="La periodicidad deseada para la tasa nominal resultante."
    )

    if st.button("Calcular Tasa Nominal"):
        try:
            tea_decimal = tea_input_e2n / 100
            nominal_calculated = effective_annual_to_nominal(tea_decimal, compounding_frequency_e2n)
            st.success(f"**Tasa Nominal Anual ({compounding_frequency_e2n}):** {nominal_calculated * 100:,.4f}%")
        except Exception as e:
            st.error(f"Error al calcular: {e}")

# --- Controles para Efectiva Periódica a Efectiva Anual ---
elif conversion_type == "Efectiva Periódica a Efectiva Anual (TEA)":
    st.subheader("Efectiva Periódica a Efectiva Anual (TEA)")
    effective_periodic_rate_input_p2e = st.number_input(
        "**Tasa Efectiva Periódica (%)**",
        min_value=0.0,
        max_value=500.0,
        value=0.4, # Ejemplo: 0.4% mensual
        step=0.01,
        format="%.2f",
        help="La tasa efectiva para un período dado."
    )
    periodic_frequency_p2e = st.selectbox(
        "**Frecuencia de la Tasa Periódica**",
        options=frequency_options_periodic,
        index=5, # Mensual
        key='periodic_freq_p2e',
        help="La periodicidad de la tasa efectiva ingresada (ej. si es mensual, se capitaliza 12 veces al año)."
    )

    if st.button("Calcular TEA desde Periódica"):
        try:
            effective_periodic_rate_decimal = effective_periodic_rate_input_p2e / 100
            tea_calculated_from_periodic = effective_periodic_to_effective_annual(effective_periodic_rate_decimal, periodic_frequency_p2e)
            st.success(f"**Tasa Efectiva Anual (TEA):** {tea_calculated_from_periodic * 100:,.4f}%")
        except Exception as e:
            st.error(f"Error al calcular: {e}")

# --- Controles para Efectiva Anual a Efectiva Periódica ---
elif conversion_type == "Efectiva Anual (TEA) a Efectiva Periódica":
    st.subheader("Efectiva Anual (TEA) a Efectiva Periódica")
    tea_input_e2p = st.number_input(
        "**Tasa Efectiva Anual (TEA) (%)**",
        min_value=0.0,
        max_value=500.0,
        value=5.0,
        step=0.1,
        format="%.2f",
        help="La Tasa Efectiva Anual (TEA) a convertir."
    )
    periodic_frequency_e2p = st.selectbox(
        "**Frecuencia de la Tasa Periódica Resultante**",
        options=frequency_options_periodic,
        index=5, # Mensual
        key='periodic_freq_e2p',
        help="La periodicidad deseada para la tasa efectiva resultante."
    )

    if st.button("Calcular Tasa Efectiva Periódica"):
        try:
            tea_decimal = tea_input_e2p / 100
            effective_periodic_calculated = effective_annual_to_effective_periodic(tea_decimal, periodic_frequency_e2p)
            st.success(f"**Tasa Efectiva Periódica ({periodic_frequency_e2p}):** {effective_periodic_calculated * 100:,.4f}%")
        except Exception as e:
            st.error(f"Error al calcular: {e}")


st.markdown("---")

# --- Botón para regresar a Home.py (en el cuerpo principal) ---
col_back1, col_back2, col_back3 = st.columns([1, 2, 1])

with col_back2:
    if st.button("Volver a Herramientas Financieras", key="back_to_home_tasas"):
        st.switch_page("HOME.py")

# --- Información Adicional/Ayuda y Navegación (en la barra lateral) ---
st.sidebar.header("Acerca de esta Calculadora")
st.sidebar.info(
    "Esta herramienta te permite convertir diferentes tipos de tasas de interés "
    "para entender su equivalencia en distintas periodicidades. "
    "Recuerda que las tasas nominales requieren una frecuencia de capitalización, "
    "mientras que las tasas efectivas periódicas ya la implican."
)