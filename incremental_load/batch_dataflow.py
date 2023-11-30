import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class ProcessAndLoad(beam.DoFn):
    def process(self, element):
       
        # Data is tab-separated
        fields = element.split('\t')

        # Handle optional fields
        sub_id_3 = fields[3] if len(fields) > 3 else None
        fp4 = fields[9] if len(fields) > 9 else None
        fp5 = fields[10] if len(fields) > 10 else None

        # Generate the unique ID
        unique_id = '_'.join([fields[1], fields[2], sub_id_3, fields[0]])

        # Parse the FP field as floats
        fp_values = [float(value) for value in fields[11].split(',')]

        row = {
            'ID': unique_id,
            'Library_ID': fields[0],
            'Sub_ID_1': fields[1],
            'Sub_ID_2': fields[2],
            'Sub_ID_3': sub_id_3,
            'MW': float(fields[4]),
            'LogP': float(fields[5]),
            'FP1': fields[6],
            'FP2': fields[7],
            'FP3': fields[8],
            'FP4': fp4,
            'FP5': fp5,
            'FP': fp_values  # Store the parsed FP field as a list of floats
        }
        yield row

def run(source_path, bq_table):

    pipeline_options = PipelineOptions()
    

    with beam.Pipeline(options=pipeline_options) as pipeline:
        # Read data from your source
        input_data = pipeline | 'ReadFromSource' >> beam.io.ReadFromText(source_path)

        # Process and transform the data
        processed_data = input_data | 'ProcessData' >> beam.ParDo(ProcessAndLoad())

        # Write the data to BigQuery
        processed_data | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
            bq_table,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            schema='ID:STRING,Library_ID:STRING,Sub_ID_1:STRING,Sub_ID_2:STRING,Sub_ID_3:STRING,MW:FLOAT,LogP:FLOAT,FP1:STRING,FP2:STRING,FP3:STRING,FP4:STRING,FP5:STRING,FP:FLOAT[]'
        )

if __name__ == '__main__':
    # Specify the source path and BigQuery table
    run('gs://your-source-path/*.tsv', 'your_dataset.your_table')

