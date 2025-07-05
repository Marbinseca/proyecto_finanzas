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

# --- Sección de Tasas de Interés ---
st.header("3. Tasas de Interés")
st.markdown("""
Las tasas de interés son el precio del dinero en el tiempo. Representan el costo de pedir prestado dinero o la recompensa por prestarlo (o invertirlo). Entender los diferentes tipos de tasas es crucial en cualquier análisis financiero.

### 3.1 Tasa Nominal y Tasa Efectiva Anual (TEA)

* **Tasa Nominal (TNA):**
    * Es la tasa de interés que se anuncia para un período de tiempo (usualmente un año), pero que se capitaliza o compone más de una vez al año.
    * No representa el costo real o el rendimiento verdadero de una operación, ya que no tiene en cuenta el efecto de la capitalización de los intereses.
    * Siempre viene acompañada de una **frecuencia de capitalización** (ej., 12% anual capitalizable mensualmente, 10% anual capitalizable semestralmente).

* **Tasa Efectiva Anual (TEA):**
    * Es la tasa de interés que realmente se paga o se gana en un año, considerando el efecto de la capitalización de los intereses.
    * Refleja el rendimiento o costo real de una inversión o un préstamo.
    * Es la tasa que te permite comparar el costo real de diferentes opciones de financiamiento o el rendimiento real de distintas inversiones, independientemente de su frecuencia de capitalización nominal.
""")

st.subheader("Fórmula para convertir Tasa Nominal a Tasa Efectiva Anual (TEA):")
st.latex(r"""
    \text{TEA} = \left(1 + \frac{\text{Tasa Nominal}}{m}\right)^m - 1
""")
st.markdown("""
Donde:
* $\text{TEA}$: Tasa Efectiva Anual (en decimal).
* $\text{Tasa Nominal}$: Tasa Nominal Anual (en decimal).
* $m$: Número de períodos de capitalización al año (ej., para capitalización mensual $m=12$, para trimestral $m=4$, para semestral $m=2$, etc.).
""")

st.subheader("Fórmula para convertir Tasa Efectiva Anual (TEA) a Tasa Nominal:")
st.latex(r"""
    \text{Tasa Nominal} = m \times \left((1 + \text{TEA})^{1/m} - 1\right)
""")
st.markdown("""
Donde las variables son las mismas que en la fórmula anterior.

### 3.2 Tasa Efectiva Periódica y Tasa Efectiva Anual (TEA)

* **Tasa Efectiva Periódica (TEP):**
    * Es la tasa de interés que se aplica directamente en un período de tiempo específico (ej., una tasa efectiva mensual, una tasa efectiva trimestral).
    * A diferencia de la nominal, esta tasa ya incluye el efecto de la capitalización dentro de su propio período.

* **Tasa Efectiva Anual (TEA):** (Como se explicó anteriormente, es la tasa anual real)
""")

st.subheader("Fórmula para convertir Tasa Efectiva Periódica (TEP) a Tasa Efectiva Anual (TEA):")
st.latex(r"""
    \text{TEA} = (1 + \text{TEP})^k - 1
""")
st.markdown("""
Donde:
* $\text{TEA}$: Tasa Efectiva Anual (en decimal).
* $\text{TEP}$: Tasa Efectiva Periódica (en decimal).
* $k$: Número de períodos en un año (ej., para una TEP mensual $k=12$, para trimestral $k=4$, para semestral $k=2$, etc.).
""")

st.subheader("Fórmula para convertir Tasa Efectiva Anual (TEA) a Tasa Efectiva Periódica (TEP):")
st.latex(r"""
    \text{TEP} = (1 + \text{TEA})^{1/k} - 1
""")
st.markdown("""
Donde las variables son las mismas que en la fórmula anterior.

**Tabla de Frecuencias de Capitalización/Períodos por Año ($m$ o $k$):**

| Frecuencia            | Valor de $m$ o $k$ |
| :-------------------- | :----------------: |
| Anual                 |         1          |
| Semestral             |         2          |
| Cuatrimestral         |         3          |
| Trimestral            |         4          |
| Bimestral             |         6          |
| Mensual               |         12         |
| Quincenal             |         24         |
| Diario                |        365         |

Es fundamental comprender estas equivalencias para tomar decisiones financieras informadas, ya sea al comparar rendimientos de inversiones o al analizar el costo real de un crédito.
""")

st.divider()

# Enlace para regresar a la página principal
if st.button("Volver a Home"):
    st.switch_page("HOME.py")

st.sidebar.info(
    "Esta sección explica los conceptos fundamentales y las fórmulas detrás de las calculadoras financieras. "
    "Un buen entendimiento de estos principios es clave para tomar decisiones financieras informadas."
)