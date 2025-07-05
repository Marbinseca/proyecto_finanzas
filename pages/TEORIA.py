import streamlit as st

st.set_page_config(page_title="Conceptos y Fórmulas Financieras", page_icon="images/finance.png", layout="centered")

st.title("📚 Conceptos y Fórmulas Financieras")
st.markdown("""
    Aquí encontrarás una explicación detallada de las herramientas y las fórmulas matemáticas
    que utilizamos en nuestras calculadoras financieras.
""")

st.divider()

# --- Explicación TIR y VAN ---
st.header("1. Calculadora TIR y VAN")
st.markdown("""
    Esta herramienta evalúa la **viabilidad y rentabilidad de proyectos de inversión** mediante el
    análisis de los flujos de caja a lo largo del tiempo.
""")

st.subheader("1.1. Valor Actual Neto (VAN / Net Present Value - NPV)")
st.markdown("""
    El VAN es el valor presente de los flujos de caja futuros de un proyecto, restándole la inversión inicial.
    Un VAN positivo indica que el proyecto es rentable y añade valor.
""")
st.latex(r"""
    VAN = \sum_{t=0}^{n} \frac{FC_t}{(1 + r)^t}
""")
st.markdown("""
    Donde:
    * $FC_t$: Flujo de caja en el período $t$. Para $t=0$, $FC_0$ es la **Inversión Inicial** (un valor negativo).
    * $r$: Tasa de descuento o costo de capital (expresada en decimal).
    * $t$: Período de tiempo (0, 1, 2, ..., n).
    * $n$: Número total de períodos.
""")

st.subheader("1.2. Tasa Interna de Retorno (TIR / Internal Rate of Return - IRR)")
st.markdown("""
    La TIR es la tasa de descuento que hace que el Valor Actual Neto (VAN) de todos los flujos de caja de un proyecto
    sea igual a cero. Representa la rentabilidad anualizada que genera una inversión.
    Si la TIR es mayor que la tasa de descuento requerida, el proyecto es aceptable.
""")
st.latex(r"""
    \sum_{t=0}^{n} \frac{FC_t}{(1 + TIR)^t} = 0 \quad \text{(Se busca TIR tal que el VAN sea cero)}
""")
st.markdown("""
    Donde:
    * $FC_t$: Flujo de caja en el período $t$.
    * $TIR$: La Tasa Interna de Retorno (expresada en decimal).
    * $t$: Período de tiempo.
    * $n$: Número total de períodos.
""")

st.divider()

# --- Explicación Calculadora de Amortización ---
st.header("2. Calculadora de Amortización (Sistema Francés)")
st.markdown("""
    Esta herramienta genera una tabla detallada de cómo se paga un préstamo a lo largo del tiempo,
    utilizando el **sistema de amortización francés** (cuotas fijas).
""")

st.subheader("2.1. Cuota Fija Periódica ($P$)")
st.markdown("""
    La cantidad constante que se paga en cada período para cubrir capital e intereses.
""")
st.latex(r"""
    P = \frac{C \cdot i}{1 - (1 + i)^{-n}}
""")
st.markdown("""
    Donde:
    * $P$: Cuota fija periódica.
    * $C$: Capital inicial del préstamo (Monto del Préstamo).
    * $i$: Tasa de interés periódica (Tasa de Interés Anual / Frecuencia de Pagos por Año).
    * $n$: Número total de pagos (Plazo del Préstamo en Años $\times$ Frecuencia de Pagos por Año).
""")

st.subheader("2.2. Cálculo de Intereses por Período")
st.markdown("""
    Los intereses se calculan sobre el saldo pendiente del capital al inicio de cada período.
""")
st.latex(r"""
    Intereses_t = CapitalPendiente_{t-1} \cdot i
""")
st.markdown("""
    Donde:
    * $Intereses_t$: Monto de intereses pagado en el período $t$.
    * $CapitalPendiente_{t-1}$: Capital pendiente al final del período anterior.
    * $i$: Tasa de interés periódica.
""")

st.subheader("2.3. Cálculo de Capital Amortizado por Período")
st.markdown("""
    Es la parte de la cuota fija que se destina a reducir el capital del préstamo.
""")
st.latex(r"""
    CapitalAmortizado_t = P - Intereses_t
""")
st.markdown("""
    Donde:
    * $CapitalAmortizado_t$: Monto del capital principal pagado en el período $t$.
    * $P$: Cuota fija periódica.
    * $Intereses_t$: Intereses pagados en el período $t$.
""")

st.subheader("2.4. Capital Pendiente (Saldo Restante)")
st.markdown("""
    El monto del préstamo que aún queda por pagar después de cada cuota.
""")
st.latex(r"""
    CapitalPendiente_t = CapitalPendiente_{t-1} - CapitalAmortizado_t
""")

st.divider()

# Enlace para regresar a la página principal
if st.button("Volver a Home"):
    st.switch_page("Home.py")

st.sidebar.info(
    "Esta sección explica los conceptos fundamentales y las fórmulas detrás de las calculadoras financieras. "
    "Un buen entendimiento de estos principios es clave para tomar decisiones financieras informadas."
)