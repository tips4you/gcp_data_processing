# Daily Load (Incremental Load)

To incrementally load data from a partner's cloud to a Google Cloud Storage (GCS) bucket using `gsutil` and Google Cloud Dataflow.

## Transfer Data to GCS

Transfer the data to Google Cloud Storage through a service account environment from outside GCP. When uploading large amounts of data or large files, consider using `gsutil rsync` or `gsutil cp -m` for a more efficient transfer.

```bash
gsutil -m cp -r data gs://our-bucket/data
```

Replace `"data"` and `"gs://our-bucket/data"` with our actual directory and bucket names.

## Set Up a Cloud Function

Write a Cloud Function that will be triggered by the file creation. In the Cloud Function code, added logic to trigger the Dataflow batch job whenever the function is invoked. We can use the Dataflow API within the Cloud Function.

This setup allows us to leverage the cost efficiency of batch processing while still achieving a level of event-driven processing.

## Create a Dataflow Batch Pipeline

Developed a batch processing pipeline using Google Cloud Dataflow. This can be similar to the batch processing pipeline. Pipeline reading data directly from Cloud Storage as a batch source.

## Deploy the Batch Pipeline

Deploy the Dataflow batch job using the cloud build. This allows us to process each file as it arrives, while still using a batch processing model. This can be more cost-effective than a streaming pipeline, especially if the files arrive less frequently or at predictable intervals.

## CICD

Push our code to a Git repository. We can use GitHub. When we push to the master branch (or merge a pull request), this will trigger the Cloud Build pipeline.

Create a build trigger in the Cloud Build through terraform. This trigger will start the pipeline whenever we push to the master branch of our Git repository.

Run our pipeline. We can do this by pushing to the master branch of our Git repository