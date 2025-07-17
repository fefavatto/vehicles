# vehicles
Dashboard do Projeto da Sprint 5 da Tripleten </br>
URL: https://vehicles-jgpv.onrender.com

## Visão Geral

O aplicativo permite ao usuário explorar visualmente um conjunto de dados relacionados a anúncios de venda de veículos. A interface é simples e funcional, e as visualizações são construídas dinamicamente com base na interação do usuário.

## Funcionalidades

- **Histograma interativo**: visualiza a distribuição da quilometragem dos veículos (campo `odometer`).
- **Gráfico de dispersão**: relaciona o preço dos veículos com a quilometragem, destacando diferentes condições (campo `condition`).
- Interface interativa baseada em **Streamlit**, com uso de botões ou caixas de seleção para controlar o que é exibido.
- Visualizações geradas com **Plotly Express**, proporcionando gráficos responsivos e interativos.

## Tecnologias Utilizadas

- Python 3.x
- Streamlit
- Plotly Express
- Pandas

## Estrutura do Projeto

```text
├── app.py                # Script principal da aplicação
├── vehicles.csv          # Conjunto de dados de exemplo
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo