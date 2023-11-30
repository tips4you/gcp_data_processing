# CICD - Automating API Enabling & GCS creation in GCP

We can automate the process of enabling APIs in Google Cloud Platform (GCP) using Terraform and cloud build. 

In Terraform, we can use the google_project_service resource to enable an API.
```bash
resource "google_project_service" "service" {
  project = "our-project-id"
  service = "serviceusage.googleapis.com"
}
```

To enable multiple APIs
```bash
variable "services" {
  default = ["iam.googleapis.com", "cloudresourcemanager.googleapis.com"]
}

resource "google_project_service" "project" {
  count   = length(var.services)
  project = "our-project-id"
  service = var.services[count.index]
}
```
And also we can use Terraform to create a Google Cloud Storage (GCS) bucket.

```bash
provider "google" {
  project = "our-project-id"
  region  = "our-region"
}

resource "google_storage_bucket" "bucket" {
  name     = "our-bucket-name"
  location = "our-location"
}
```

```bash
steps:
# Retrieve key
  - name: gcr.io/cloud-builders/gcloud
    id: retrieve-read-key
    entrypoint: bash
    dir: ${_DIR}
    args:
      - '-c'
      - >
        gcloud secrets versions access ${_VERSION} --secret=${_KEY} --project=${_PROJECT}  > /root/.ssh/id_rsa;
    volumes:
      - name: ssh
        path: /root/.ssh

...
...
...

substitutions:
    _PROJECT: gcp-demo-project
    _VERSION: "latest"
    _KEY: "sec_key"

```

Please refer my setup: https://github.com/tips4you/gcp-tf