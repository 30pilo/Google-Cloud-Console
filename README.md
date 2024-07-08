# BigQuery JSON Upload Example

This repository provides a step-by-step guide to upload a JSON file to Google Cloud Storage, create a BigQuery table, and run SQL queries on the table.

## Prerequisites

- Google Cloud account
- Google Cloud SDK installed
- BigQuery and Google Cloud Storage enabled in your Google Cloud project
- JSON file to be uploaded

## Steps

### 1. Upload JSON file to Google Cloud Storage

1. Open [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to **Storage** > **Browser**.
3. Create a new bucket or select an existing bucket.
4. Click **Upload files** and select your JSON file.
5. Note the bucket name and the file name.

### 2. Create a BigQuery Table

1. Open [BigQuery Console](https://console.cloud.google.com/bigquery).
2. In the Explorer panel, select your project.
3. Click **Create dataset** and enter a dataset name.
4. Within your dataset, click **Create table**.
5. In the **Create table** form, specify the following:
    - **Source**: Google Cloud Storage
    - **Select file**: Browse to the JSON file in your bucket
    - **File format**: JSON
    - **Table name**: Enter a name for your table
    - **Schema**: Auto-detect or provide a schema manually
6. Click **Create table**.

### 3. Run SQL Queries

1. Open [BigQuery Console](https://console.cloud.google.com/bigquery).
2. In the Explorer panel, navigate to your dataset and table.
3. Click on the table and then click **Query table**.
4. Write and execute your SQL queries.

```sql
SELECT * FROM `your-project.your-dataset.your-table`
