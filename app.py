
#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
from eda_app import run_eda_app
from ml_app import run_ml_app



def home_page():
	# Título de la APP con una caja azul  y el texto en blanco centrado en la pantalla con el texto: Diabetes Predictor

	st.title('App para la detección temprana de Diabetes')
	st.text('Esta aplicación permite predecir la diabetes en pacientes')
	st.markdown('## fuentes de información')
	st.code("""- https://www.kaggle.com/uciml/pima-indians-diabetes-database 
	          \n- https://www.kaggle.com/uciml/pima-indians-diabetes-database""", language='markdown')
	st.markdown('## Contenido de la aplicación')
	st.code("""- https://www.kaggle.com/uciml/pima-indians-diabetes-database 
	          \n- https://www.kaggle.com/uciml/pima-indians-diabetes-database""", language='markdown')





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