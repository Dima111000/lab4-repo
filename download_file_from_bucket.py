import boto3

def download_file(bucket, file, local_file_path):
    s3 = boto3.client("s3")

    try:
        s3.download_file(bucket, file, local_file_path)
        print(f"Файл успішно завантажений як {local_file_path}")
    except Exception as e:
        print(f"Помилка завантаження файлу: {e}")

def main():
    bucket_name = input("Уведіть назву S3 bucket: ")
    file = input("Уведіть назву файла у S3: ")
    local_file_path = input("Уведіть локальний шлях для збереження файлу: ")

    download_file(bucket_name, file, local_file_path)

if __name__ == "__main__":
    main()