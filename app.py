import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Simulador de Série Geométrica",
    layout="centered"
)

st.title("Simulador de Série Geométrica")

st.write(
    """
    Informe o primeiro termo, a razão e a quantidade de termos
    para calcular uma série geométrica.
    """
)

st.subheader("Dados da série")

a1 = st.number_input(
    "Primeiro termo (a₁):",
    value=10.0,
    step=0.5
)

q = st.number_input(
    "Razão (q):",
    value=0.5,
    step=0.1
)

n = st.number_input(
    "Quantidade de termos (n):",
    min_value=1,
    value=5,
    step=1
)

calcular = st.button("Calcular série")

if calcular:
    termos = []

    for i in range(n):
        termo = a1 * (q ** i)
        termos.append(termo)

    if q == 1:
        soma = a1 * n
    else:
        soma = a1 * (1 - q ** n) / (1 - q)

    termos_formatados = " + ".join(
        f"{termo:g}" for termo in termos
    )

    st.success("Cálculo realizado!")

    st.subheader("Termos da série")
    st.write(termos_formatados)

    somas_acumuladas = []
    acumulado = 0

    for termo in termos:
        acumulado += termo
        somas_acumuladas.append(acumulado)

    dados = pd.DataFrame(
        {
            "Etapa": range(1, n + 1),
            "Valor do termo": termos,
            "Total acumulado": somas_acumuladas
        }
    )

    dados = dados.set_index("Etapa")

    st.subheader("Tabela de resultados")

    st.dataframe(
        dados,
        use_container_width=True
    )

    st.subheader("Evolução da série")
    st.line_chart(dados)

    st.subheader("Soma dos termos")

    st.metric(
        label=f"Soma dos {n} primeiros termos",
        value=f"{soma:g}"
    )

    st.divider()
    st.subheader("Análise da série infinita")

    if abs(q) < 1:
        soma_infinita = a1 / (1 - q)

        st.success(
            "A série infinita converge, porque |q| < 1."
        )

        st.metric(
            label="Soma infinita",
            value=f"{soma_infinita:g}"
        )

    else:
        st.warning(
            "A série infinita não converge, porque |q| é maior ou igual a 1."
        )