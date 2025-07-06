# Herramientas Financieras con Streamlit

Una aplicación web interactiva construida con Streamlit que proporciona un conjunto de calculadoras financieras para ayudar en la toma de decisiones de inversión y préstamos.


## ✨ Características

*   **Calculadora de TIR y VAN:** Evalúa la rentabilidad de un proyecto de inversión calculando la Tasa Interna de Retorno (TIR) y el Valor Actual Neto (VAN).
*   **Calculadora de Amortización:** Genera tablas de amortización detalladas para préstamos utilizando el sistema francés (cuotas fijas). Permite descargar los resultados en formato Excel.
*   **Conceptos y Fórmulas:** Una sección teórica que explica los conceptos financieros y las fórmulas matemáticas utilizadas en las calculadoras.
*   **Interfaz Interactiva:** Interfaz de usuario limpia e intuitiva para una fácil entrada de datos y visualización de resultados.

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### Prerrequisitos

Asegúrate de tener instalado lo siguiente:
*   [Python 3.8+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/downloads/) (opcional, para clonar el repositorio de forma sencilla)

### Pasos de Instalación

1.  **Clona el repositorio:**
    Abre tu terminal o línea de comandos y ejecuta el siguiente comando para clonar el proyecto.
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd proyecto_finanzas
    ```
    Si no usas Git, puedes descargar el proyecto como un archivo ZIP y descomprimirlo.

2.  **Crea y activa un entorno virtual (Recomendado):**
    Es una buena práctica aislar las dependencias del proyecto para evitar conflictos con otros proyectos de Python.

    *   **En Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

    *   **En macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instala las dependencias:**
    Con tu entorno virtual activado, instala todas las librerías necesarias que se encuentran en el archivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ Cómo Ejecutar la Aplicación

Una vez que hayas instalado todas las dependencias, puedes iniciar la aplicación Streamlit con el siguiente comando:

```bash
streamlit run home.py
```

Esto iniciará un servidor local y abrirá automáticamente una nueva pestaña en tu navegador web con la aplicación en funcionamiento.

## 🛠️ Tecnologías Utilizadas

*   **Framework:** Streamlit
*   **Cálculos:** Pandas, Numpy, Numpy-Financial
*   **Exportación:** XlsxWriter

## ▶️ Demo aplicación
Puede ver una demo de la aplicación en el siguiente enlace: [Demo de la Aplicación](https://proyecto-finanzas.streamlit.app/)

## 📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.