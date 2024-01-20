
#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
from eda_app import run_eda_app
from ml_app import run_ml_app



def home_page():
	# Título de la APP con una caja azul  y el texto en blanco centrado en la pantalla con el texto: Diabetes Predictor

	st.title('App para la deteccion temprana de DM')
	st.text('Dataset que contiene señales y sintomas que pueden indicar diabetes o posibilidad de diabetes.')
	st.markdown('## fuentes de datos')
	st.code("""
			https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dat""", 
			language='markdown')
	st.markdown('## Contenido de la aplicación')
	st.code("""- EDA Section: Análisis exploratorio de los datos
			\n- ML Section: Predicción de Diabetes basada en ML (Machine Learning)""", 
language='markdown')





# Función main()
def main():
	selected_option = st.sidebar.selectbox('Seleccione una opción', ['Home','Análisis de datos', 'Machine Learning', 'Info'])
    
	if selected_option == 'Home':
		home_page()
	elif selected_option == 'Análisis de datos':  
		run_eda_app()
	elif selected_option == 'Machine Learning':
		run_ml_app()


if __name__ == '__main__':
	main()