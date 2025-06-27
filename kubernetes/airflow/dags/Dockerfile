FROM apache/airflow

USER root

RUN apt-get update

RUN apt-get install gcc -y

USER airflow

COPY ./requirements.txt \${AIRFLOW_HOME}/requirements.txt

RUN pip install --upgrade pip --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}"

RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r \${AIRFLOW_HOME}/requirements.txt

RUN pip install Cython --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}"

RUN pip install scikit-learn --no-build-isolation --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}"
