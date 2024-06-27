from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from project.video_extract import VideoExtract

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'video_classification_dag',
    default_args=default_args,
    description='A pipeline to generate image datasets from videos for marine animal classification',
    schedule=None,
)

generate_dataset_task = PythonOperator(
    task_id='generate_image_dataset',
    python_callable=VideoExtract().generate_image_dataset,
    op_kwargs={
        'video_path': '5548408-uhd_3840_2160_25fps.mp4',
        'size': (224, 224),
    },
    dag=dag,
)
generate_dataset_task
