import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
from typing import Optional


"""
Aplicativo Streamlit para EDA (Análise Exploratória de Dados) de anúncios de veículos.

Funcionalidades:
- Carregar CSV (padrão: `vehicles.csv`)
- Criar histograma da coluna `odometer`
- Criar gráfico de dispersão de `price` vs `odometer` com coluna de cor apropriada
"""


@st.cache_data
def load_data(path: str = 'vehicles.csv') -> pd.DataFrame:
	"""Carrega um CSV para um DataFrame do pandas.

	Retorna um DataFrame vazio se o carregamento falhar e exibe a mensagem de erro no Streamlit.
	"""
	try:
		return pd.read_csv(path)
	except Exception as e:
		st.error(f"Erro ao carregar dados: {e}")
		return pd.DataFrame()


def choose_color_column(df: pd.DataFrame) -> Optional[str]:
	"""Escolhe uma coluna adequada para colorir os gráficos.

	Ordem de preferência: `model`, `manufacturer`, `type`, `condition`.
	Retorna ``None`` se nenhuma coluna apropriada estiver presente.
	"""
	candidates = ['model', 'manufacturer', 'type', 'condition']
	for c in candidates:
		if c in df.columns:
			return c
	return None


def make_histogram(df: pd.DataFrame, col: str = 'odometer') -> object:
	"""Retorna um histograma Plotly para a coluna `col`.

	O chamador deve verificar se `col` existe antes de chamar.
	"""
	fig = px.histogram(df, x=col, nbins=30, title=f'Distribuição de {col}')
	return fig


def make_scatter(df: pd.DataFrame, x: str = 'odometer', y: str = 'price', color: Optional[str] = None) -> object:
	"""Retorna um gráfico de dispersão Plotly para `x` vs `y`.

	`color` pode ser ``None`` para desativar agrupamento por cor.
	"""
	fig = px.scatter(df, x=x, y=y, color=color, title=f'{y} vs {x}')
	return fig


df = load_data()

st.header('Vehicle Listings - EDA App')

if df.empty:
	st.warning('O conjunto de dados `vehicles.csv` está vazio ou não pôde ser carregado.')
else:
	st.write('Dados carregados com', len(df), 'linhas.')

	# Histogram button
	if st.button('Criar histograma'):
		st.write('Criando um histograma para a coluna `odometer`')
		if 'odometer' in df.columns:
			fig = make_histogram(df, 'odometer')
			st.plotly_chart(fig, use_container_width=True)
		else:
			st.error('Coluna `odometer` não encontrada no dataset.')

	# Scatter button
	if st.button('Criar gráfico de dispersão'):
		st.write('Criando um gráfico de dispersão (price vs odometer)')
		if {'price', 'odometer'}.issubset(df.columns):
			color_col = choose_color_column(df)
			fig = make_scatter(df, x='odometer', y='price', color=color_col)
			st.plotly_chart(fig, use_container_width=True)
		else:
			st.error('Colunas `price` e/ou `odometer` não encontradas no dataset.')

	# Checkbox alternative for histogram
	st.write('---')
	if st.checkbox('Mostrar histograma (caixa de seleção)'):
		if 'odometer' in df.columns:
			fig = make_histogram(df, 'odometer')
			st.plotly_chart(fig, use_container_width=True)
		else:
			st.error('Coluna `odometer` não encontrada no dataset.')
