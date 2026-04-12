Project: Vehicle Listings EDA and Streamlit App
=============================================

Breve descrição
---------------
Aplicativo Streamlit para exploração de um conjunto de anúncios de carros (histograma e gráfico de dispersão).

Arquivos no repositório
------------------------
- README.md
- app.py
- vehicles.csv
- requirements.txt
- notebooks/EDA.ipynb
- .streamlit/config.toml

Como executar localmente
------------------------
1. Instale as dependências:

```
pip install -r requirements.txt
```

2. Execute o app Streamlit:

```
streamlit run app.py
```

Deploy no Render
-----------------
Crie um serviço web no Render ligado ao repositório GitHub e use o comando de build:

```
pip install --upgrade pip && pip install -r requirements.txt
```

Start Command:

```
streamlit run app.py
```

Adicione a URL do app no Render aqui quando disponível.
