ejemplo sencillo para verificar el funcionamiento de airflow en windows 10

Como instalar Airflow en Windows

Instalar AIRFLOW en Windows


![image](https://github.com/user-attachments/assets/2fb876e8-7525-4501-9091-0fdaf7b18963)



Se habilita la opcion de subsistema de windows para linux...

![image](https://github.com/user-attachments/assets/876ad2d9-946d-4e05-8571-64ed8445b74c)

descargamos ubuntu en la microsoft store

iniciamos el ubuntu y esperamos hasta que inicie 
![image](https://github.com/user-attachments/assets/b9fe147e-801f-47b9-bd54-b56be4902dab)

despues de un tiempo ya estamos en esto

![image](https://github.com/user-attachments/assets/37ee99f8-234a-4b2f-95d4-6c928f155107)

![image](https://github.com/user-attachments/assets/2a608e92-f553-4335-8863-4276c57f75e1)

Ponemos los siguientes comandos

sudo apt-get install software-properties-common
add-repository universe
sudo apt-add-repository universe

add-repository universe
sudo apt-get update
revision version python
python3 --version
instalacion pip
sudo apt-get install python3-pip

exportar variable
export SLUGIFY_USES_TEXT_UNIDECODE=yes

![image](https://github.com/user-attachments/assets/106ad01c-b37c-4bc9-a7a1-a2770fe03df6)

instalacion sql alquemy compatible con airflow 2.20
sudo pip install SQLAlchemy==1.3.24

![image](https://github.com/user-attachments/assets/27b69eb2-a2ae-4665-8efa-8caf71abdc69)

![image](https://github.com/user-attachments/assets/4b04affa-4c01-4c83-a984-6f6948068d44)

instalacion airflow
sudo pip install apache-airflow
tuvo un error al instalar el airflow

![image](https://github.com/user-attachments/assets/f4d0ec88-bc4e-4fea-a03f-7bc2ec319b86)

por falta de recursos tendremos que usar estos comandos
sudo apt update && sudo apt upgrade -y

![image](https://github.com/user-attachments/assets/c147fcfe-3d0a-4d58-9dc3-6d8f3602eed6)

instalar las dependencias
sudo apt install -y python3-pip python3-dev build-essential \
libssl-dev libffi-dev python3-venv libpq-dev \
libcurl4-openssl-dev libmysqlclient-dev libsasl2-dev \
libldap2-dev libssl-dev libkrb5-dev

![image](https://github.com/user-attachments/assets/2ad2f2b0-b17c-4a1d-b5a4-c8d27219d387)

sudo apt install -y abseil-cpp
error al usar el comando para lo que se piensa instalar no esta en los repositorios del sistema
entonces se usar un entorno virtual de ubuntu

sudo apt install python3-venv -y
python3 -m venv airflow-venv
source airflow-venv/bin/activate

pip install --upgrade pip setuptools wheel
AIRFLOW_VERSION=2.9.1
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW
_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
con esto ya tendremos instalado el airflow en teoria

![image](https://github.com/user-attachments/assets/b0e18750-95dd-4f29-9be0-f1ef8027426d)

airflow db init

![image](https://github.com/user-attachments/assets/e722dd13-020f-4580-88ba-2e9d5ca8a96e)

airflow users create \
--username admin \
--firstname Admin \
--lastname User \
--role Admin \
--email admin@example.com

Crea un usuario para acceder a la pagina web

para luego usar el comando para levantar el sitio web
airflow webserver --port 8080
y vamos a esta direccion URL en nuestro navegador preferido
http://localhost:8080

![image](https://github.com/user-attachments/assets/867a0e31-1532-4a62-aa44-90d2314ae8a4)

luego de ingresar los datos se ingresara ya a la pagina de airflow

![image](https://github.com/user-attachments/assets/d75c27a6-d0b6-4588-b000-52638003557f)

en otra terminal necesito un proceso para ejecutar las tareas abrimos nueva terminal y añadimos
lo siguiente

source airflow-venv/bin/activate
airflow scheduler

![image](https://github.com/user-attachments/assets/96d00aa8-dbe5-49cb-9231-e907d0eba4c5)

en una nueva terminal
ponemos source airflow-venv/bin/activate para activar el entorno virtual
y luego
mkdir -p ~/airflow/dags
nano ~/airflow/dags/mi_primer_dag.py
para crear la carpeta y el DAG

ponemos el siguiente codigo para comprobar que si esta funcionando (esta en el repositorio)

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
schedule_interval="@daily", # Se ejecuta una vez al día
catchup=False, # No se ejecuta retroactivamente
tags=["ejemplo"],
) as dag:
tarea_saludo = PythonOperator(
task_id="saludar",
python_callable=saludar
)

![image](https://github.com/user-attachments/assets/ff91b140-6c21-4b41-90d6-efdb6716840c)

le damos guardar Ctrl+O ENTER
y salir CTRL+X

![image](https://github.com/user-attachments/assets/720b46a4-ed9f-4e43-8610-609a4f52e5d3)

en la pagina buscamos mi_primer_dag que es el archivo de python que guardamos el codigo lo
activamos y lo ejecutamos

![image](https://github.com/user-attachments/assets/fc771077-25f7-4825-bf5b-f004fb63bac4)

como podemos ver se esta ejecutando correctamente todos los pasos es un problema ya que
depende de la version del sistema, equipo, componentes y SO, ya que es un programa de LINUX,
pero pudimos utilizarla usando windows
para activar modo tienes que tener 3 terminales usar source airflow-venv/bin/activate para
activar el entorno virtual

nano ~/airflow/dags/mi_primer_dag.py una terminal para crear con este comando el archivo de
Python de DAG
pero antes debes levantar el sitio y el proceso
airflow webserver --port 8080 este para levantar el sitio web
y este airflow scheduler para levantar el proceso

y entrar a esta direccion URL http://localhost:8080


















