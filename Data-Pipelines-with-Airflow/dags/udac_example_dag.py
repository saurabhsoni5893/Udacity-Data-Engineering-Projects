from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator,
                              PostgresOperator)
from helpers import SqlQueries

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'Saurabh',
    'start_date': datetime(2019, 1, 12),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'email_on_retry': False
}

dag = DAG('udacity_airflow_project',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='0 * * * *',
          max_active_runs=3
        )

# start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

start_operator = PostgresOperator(
    task_id='Begin_execution', 
    dag=dag,
    sql=['create_table.sql'],
    postgres_conn_id='redshift',
    autocommit=True)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
    s3_bucket="udacity-dend",
    s3_key="log_data",
    table="public.staging_events",
#     create_stmt=SqlQueries.create_table_staging_events,
    json="s3://udacity-dend/log_json_path.json"
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
    s3_bucket="udacity-dend",
    s3_key="song_data/A/A/A",
    table="public.staging_songs",
#     create_stmt=SqlQueries.create_table_staging_songs,
    json="auto"
)

load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
#     create_stmt=SqlQueries.create_table_songplays,
    sql_query=SqlQueries.songplay_table_insert,
    table="public.songplays",
    truncate_table=True
)

load_user_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dim_table',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
#     create_stmt=SqlQueries.create_table_users,
    sql_query=SqlQueries.user_table_insert,
    table="public.users",
    truncate_table=True
    
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
#     create_stmt=SqlQueries.create_table_songs,
    sql_query=SqlQueries.song_table_insert,
    table="public.songs",
    truncate_table=True
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
#     create_stmt=SqlQueries.create_table_artist,
    sql_query=SqlQueries.artist_table_insert,
    table="public.artists",
    truncate_table=True
)

load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
#     create_stmt=SqlQueries.create_table_time,
    sql_query=SqlQueries.time_table_insert,
    table="public.time",
    truncate_table=True
)


run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    provide_context=True,
    aws_credentials_id="aws_credentials",
    redshift_conn_id='redshift',
    tables=["songplay","users","song","artist","time"]
)
end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> [stage_events_to_redshift, stage_songs_to_redshift]
[stage_events_to_redshift, stage_songs_to_redshift] >> load_songplays_table
load_songplays_table >> [load_song_dimension_table, load_user_dimension_table, load_artist_dimension_table, load_time_dimension_table]
[load_song_dimension_table, load_user_dimension_table, load_artist_dimension_table, load_time_dimension_table] >> run_quality_checks
run_quality_checks >> end_operator
