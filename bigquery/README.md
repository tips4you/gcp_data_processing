# One-Time Load Verification and Data Loading

To verify the data after a one-time load using an external table in BigQuery, and then load the data into BigQuery with partitioning and clustering.

## Verify Data

After the one-time load, verify the data using an external table in BigQuery. You can refer to the `one_time_load_verify.sql` script for this step.

## Create table in BigQuery

Next, create table in dataset BigQuery with partitioning and clustering. You can refer to the `create_table.sql` script for this step.

## Load our data into BigQuery: 

Once our data is in GCS, We can load it into BigQuery. 
```bash
bq load --source_format=FORMAT dataset.table gs://our-bucket/data/*
```