FROM apache/airflow:2.3.0-python3.8

USER root

RUN apt-get update \
    && apt-get install -y python3-opencv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY airflow/dags /opt/airflow/dags
COPY airflow/logs /opt/airflow/logs
COPY airflow/plugins /opt/airflow/plugins
