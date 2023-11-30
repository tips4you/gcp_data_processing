# Data Transfer to Google Cloud Storage (GCS)

Transfer data from a partner's cloud to a Google Cloud Storage (GCS) bucket using either `gsutil` or the Transfer Appliance.

## Using gsutil

`gsutil` is a command-line tool for GCS that can be used to perform a variety of tasks, including uploading, downloading, and deleting objects. 

To transfer the dataset to the GCS bucket, use the `gsutil cp` command. The `-o GSUtil:parallel_composite_upload_threshold=150M` option enables parallel composite uploads for files larger than 150MB, which can make the upload process faster.

```bash
gsutil -o GSUtil:parallel_composite_upload_threshold=150M cp file*/*.tsv.gz gs://our-gcs-bucket/
```

We can monitor the transfer progress using `gsutil ls` or `gsutil du` and verify that all files are successfully uploaded to the GCS bucket.


## Using the Transfer Appliance

The Transfer Appliance is a hardware appliance that can be used to securely and efficiently transfer large volumes of data (100TB or more) to GCS. The appliance is shipped to us, We can load the data onto it, and then ship it back to Google, where the data is uploaded to GCS.

For transferring such a large amount of data (10TB compressed, 100TB uncompressed), the Transfer Appliance might be a more suitable option. It’s designed for one-time data transfers of large amounts of data and can be more cost-effective and efficient for such scenarios.

The cost for using the Transfer Appliance starts around $500 USD. More details can be found [https://cloud.google.com/transfer-appliance/pricing].
