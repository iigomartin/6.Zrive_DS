import boto3 as boto3

def main():
    
    session = boto3.Session(aws_access_key_id="wont give you the key", aws_secret_access_key="nor the secret")
    #I prefer to upload the download_data script instead of putting it in gitignore.
    
    s3 = session.resource('s3')
    my_bucket = s3.Bucket('zrive-ds-data')
    
    #We check all data
    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)
        
    #We need to download all of it (sampled-datasets and box-builder-dataset),
    # we do it step by step
    s3_object1 = s3.Object(bucket_name='zrive-ds-data',key='groceries/sampled-datasets/abandoned_carts.parquet')
    s3_object1.download_file(Filename='src/module_2/abandoned_carts.parquet')
    s3_object2 = s3.Object(bucket_name='zrive-ds-data',key='groceries/sampled-datasets/inventory.parquet')
    s3_object2.download_file(Filename='src/module_2/inventory.parquet')
    s3_object3 = s3.Object(bucket_name='zrive-ds-data',key='groceries/sampled-datasets/orders.parquet')
    s3_object3.download_file(Filename='src/module_2/orders.parquet')
    s3_object4 = s3.Object(bucket_name='zrive-ds-data',key='groceries/sampled-datasets/regulars.parquet')
    s3_object4.download_file(Filename='src/module_2/regulars.parquet')
    s3_object5 = s3.Object(bucket_name='zrive-ds-data',key='groceries/sampled-datasets/users.parquet')
    s3_object5.download_file(Filename='src/module_2/users.parquet')
    s3_object6 = s3.Object(bucket_name='zrive-ds-data',key='groceries/box_builder_dataset/feature_frame.csv')
    s3_object6.download_file(Filename='src/module_2/feature_frame.csv')
    raise NotImplementedError

if __name__ == "__main__":
    main()