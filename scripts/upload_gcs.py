from google.cloud import storage
import os
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def upload_to_gcs(file_path, bucket_name, blob_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)
    logging.info(f"Đã upload {file_path} lên gs://{bucket_name}/{blob_path}")
