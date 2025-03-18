import boto3

client = boto3.client('rekognition')

def recognize_image(bucket, image_key):
    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': image_key}},
        MaxLabels=10
    )
    return response['Labels']

if __name__ == "__main__":
    labels = recognize_image('your-bucket', 'path/to/image.jpg')
    print("Detected labels:", labels)
