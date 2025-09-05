import json
import pandas as pd
import boto3
from io import BytesIO

data_path = input("Уведіть шлях до json файла: ")
bucket_name = input("Уведіть назву S3 Bucket: ")
key = input("Уведіть назву файла для S3 (наприклад, output.csv): ")

with open(data_path, "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)

csv_buffer = BytesIO()
df.to_csv(csv_buffer, index=False, encoding="utf-8")

csv_buffer.seek(0)

s3 = boto3.client("s3")
s3.upload_fileobj(csv_buffer, bucket_name, key)

print(f"Дані з json завантажені на Amazon S3!")