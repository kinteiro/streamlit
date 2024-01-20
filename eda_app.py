
# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import pandas as pd	
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

_ROOT = Path(__file__).resolve().parent

def upload_dfs() -> dict[str, pd.DataFrame]: 
	"""Uploads the dataframes from the data folder."""
	return {
		"diabetes_data_upload": pd.read_csv(_ROOT / "data/diabetes_data_upload.csv"),
		"diabetes_data_upload_clean": pd.read_csv(_ROOT / "data/diabetes_data_upload_clean.csv"),
	}
dfs = upload_dfs()



def sub_menu():
	st.sidebar.title('Submenú')
	selected_sub_menu = st.sidebar.selectbox('Seleccione una opción', ['Descriptivo', 'Gráficos'])
	return selected_sub_menu


def carga_df(ruta):
	df = pd.read_csv(ruta)
	return df

def menu_descriptivo(df):
		st.subheader('Descriptivo')
		# Cargar el dataset
		# Mostrar el dataset
		st.dataframe(df.head(10))
		# expanders para mostrar el dataset
		with st.expander('Tipo de datos'):
			st.dataframe(df.dtypes)
		with st.expander('Resumen descriptivo'):
			st.dataframe(df.describe())
		with st.expander('Distribución por Género'):
			st.dataframe(df.groupby(df["Gender"]).count())
		with st.expander('Distribución por Clase (Class)'):
			st.dataframe(df.groupby(df["class"]).count())


def corr_heatmap(df):
	fig, ax = plt.subplots()
	sns.heatmap(df.corr(), annot=False, cmap="inferno")
	st.pyplot(fig)


def menu_graficos(df):
	st.subheader('Gráficos')
	with st.expander('Gráfico de distribución por Género'):
		fig, ax = plt.subplots()
		gender_counts = df["Gender"].value_counts()
		ax.bar(gender_counts.index, gender_counts)
		st.pyplot(fig)
	with st.expander('Gráfico de distribución por Clase (Class)'):
		fig, ax = plt.subplots()
		class_counts = df["class"].value_counts()
		ax.bar(class_counts.index, class_counts)
		st.pyplot(fig)
	with st.expander('Gráfico de distribución por Edad'):
		fig, ax = plt.subplots()
		sns.distplot(df["Age"])
		st.pyplot(fig)
	with st.expander("Mapa de calor de correlaciones"):
		corr_heatmap(df=dfs["diabetes_data_upload_clean"])
	# with st.expander("Boxplot con edades y géneros"):
	# 	fig, ax = plt.subplots()
	# 	# crea un boxplot con sns
	# 	# sns.boxplot(data=df[])
	# 	data = df[["Age", "Gender"]]
	# 	sns.boxplot(data)
	# 	st.pyplot(fig)



# --- MAIN --- 

def run_eda_app():	
	
	# Título de la APP
	st.title('Sección de Análisis de datos')
	st.subheader('Analisi descriptivo')
	# Submenú
	diabetes_data_upload = dfs["diabetes_data_upload"]
	selected_sub_menu = sub_menu()
	if selected_sub_menu == 'Descriptivo':
		menu_descriptivo(df=diabetes_data_upload)
	elif selected_sub_menu == 'Gráficos':
		menu_graficos(df=diabetes_data_upload)




	# Todo el código a escribir va aquí






# Fin de la FUNCION







