import re
import traceback
import logging
from google.cloud import bigquery
from google.api_core.exceptions import NotFound

logging.basicConfig(level=logging.DEBUG)

def streaming(event, context):
    try:
        # イベントデータの抽出
        data = event
        event_id = context.event_id
        event_type = context.event_type
        bucket_name = data['bucket']
        file_name = data['name']
        metageneration = data['metageneration']
        time_created = data['timeCreated']
        updated_time = data['updated']

        # ログ出力
        logging.debug(f"Event ID: {event_id}")
        logging.debug(f"Event type: {event_type}")
        logging.debug(f"Bucket: {bucket_name}")
        logging.debug(f"File: {file_name}")
        logging.debug(f"Metageneration: {metageneration}")
        logging.debug(f"Created: {time_created}")
        logging.debug(f"Updated: {updated_time}")
        logging.debug(f"Bucket name: {bucket_name}")
        logging.debug(f"File name: {file_name}")
        logging.debug(f"Time Created: {time_created}")

        # BigQueryテーブル設定
        config = [
            {
                'name': 'student',
                'schema': [
                    bigquery.SchemaField("Gender", "STRING"),
                    bigquery.SchemaField("Appearance", "STRING"),
                    bigquery.SchemaField("Expression", "STRING")
                ],
                'format': 'NEWLINE_DELIMITED_JSON'
            }
        ]
        
        client = bigquery.Client()
        for table in config:
            table_name = table['name']
            if re.search(table_name, file_name):
                table_schema = table['schema']
                dataset_name = 'e51l1vcvzyv8'
                _check_if_table_exists(client, dataset_name, table_name, table_schema)
                _load_table_from_uri(client, bucket_name, file_name, table_schema, dataset_name, table_name)
    except Exception as e:
        logging.error(f'Error streaming file. Cause: {traceback.format_exc()}')

def _check_if_table_exists(client, dataset_name, table_name, schema):
    project_id = client.project
    table_id = f"{project_id}.{dataset_name}.{table_name}"
    try:
        client.get_table(table_id)
        logging.debug(f"Table {table_name} already exists.")
    except NotFound:
        table = bigquery.Table(table_id, schema=schema)
        client.create_table(table)
        logging.debug(f"Created table {table_name}")

def _load_table_from_uri(client, bucket_name, file_name, schema, dataset_name, table_name):
    project_id = client.project
    table_id = f"{project_id}.{dataset_name}.{table_name}"
    job_config = bigquery.LoadJobConfig()
    job_config.schema = schema
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON

    uri = f"gs://{bucket_name}/{file_name}"
    job_config.max_bad_records = 10  # 許容される最大エラー数を設定

    load_job = client.load_table_from_uri(
        uri,
        table_id,
        location="US",
        job_config=job_config,
    )
    logging.debug(f"Starting job {load_job.job_id}")

    load_job.result()
    logging.debug("Job finished.")

    destination_table = client.get_table(table_id)
    logging.debug(f"Loaded {destination_table.num_rows} rows.")
