const { google } = require('googleapis');
const dataflow = google.dataflow('v1b3');

exports.triggerDataflow = async (event, context) => {
  try {
    const file = event;

    // Check if the file is not a temporary file
    if (!file.name.includes('temp')) {
      // Parameterize constants
      const projectId = 'your-project-id';
      const region = 'us-central1';
      const templateGcsPath = 'gs://path-to-your-template';
      const jobName = 'my-dataflow-job';

      // Authenticate with the service account
      const auth = new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform']
      });
      const authClient = await auth.getClient();
      google.options({ auth: authClient });

      // Set up the request body
      const requestBody = {
        projectId: projectId,
        jobName: jobName,
        parameters: {
          inputFile: `gs://${file.bucket}/${file.name}`,
          // Add any other parameters your template requires
        },
        environment: {
          tempLocation: 'gs://your-temp-location',
          zone: region
        }
      };

      // Make the request to the Dataflow API
      const request = {
        projectId: projectId,
        resource: requestBody,
        gcsPath: templateGcsPath
      };
      const response = await dataflow.projects.templates.launch(request);

      // Log job ID if successful
      console.log(`Dataflow job started: ${response.data.job.id}`);
    }
  } catch (error) {
    // Log detailed error information
    console.error(`Error starting Dataflow job: ${error}`);
    console.error(error.stack);
  }
};