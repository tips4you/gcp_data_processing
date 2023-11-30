CREATE EXTERNAL TABLE dataset_name.table_name
OPTIONS (
  format = 'FORMAT',
  uris = ['gs://gcs-bucket/our-data/*.csv'],
  compression = 'COMPRESSION_TYPE',
  schema = 'FIELD_NAME:DATA_TYPE, ...'
);

