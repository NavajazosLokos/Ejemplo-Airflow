from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Función que se ejecutará como tarea
def saludar():
    print("¡Hola desde mi primer DAG!")

# Definimos el DAG
with DAG(
    dag_id="mi_primer_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",  # Se ejecuta una vez al día
    catchup=False,               # No se ejecuta retroactivamente
    tags=["ejemplo"],
) as dag:
    
    tarea_saludo = PythonOperator(
        task_id="saludar",
        python_callable=saludar
    )