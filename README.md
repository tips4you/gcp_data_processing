# Data Transfer to Google Cloud Storage (GCS) and BigQuery

To perform a one-time, cost-efficient load of data from a partner's cloud to a Google Cloud Storage (GCS) bucket, and how to perform an incremental load for daily or regular updates to the data.

## One-Time Full Load

To perform a one-time, cost-efficient load of data from a partner's cloud to a GCS bucket, refer to the directory `one_time_full_load`. This directory contains scripts and instructions for transferring the data.

## Data Verification and Loading into BigQuery

After the full load, verify the data and create a table in BigQuery. Load the data into BigQuery to improve performance. Detailed steps and scripts for this process can be found in the `bigquery` directory.

## Incremental Load

For daily or regular updates to our data, an incremental load approach is more cost-efficient than transferring the entire dataset each time. Instructions and scripts for performing an incremental load from a partner's cloud to a GCS bucket can be found in the `incremental_load` directory.

## Provisioning and CICD

Refer: `infra_cicd_creation.md`

## Cost and Service Choice

Considering cost as a primary concern, we have opted for Cloud Function and Dataflow batch jobs instead of Cloud Composer. 

This decision represents a trade-off for handling large amounts of data transfer to Google Cloud Storage (GCS). While using gsutil requires more manpower, the Transfer Appliance simplifies the process, albeit at a slightly higher cost. This approach ensures efficient data management while balancing cost-effectiveness and simplicity.