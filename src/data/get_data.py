# Using Python Boto3 to download files from the S3 bucket

import boto3

bfp = input('Enter the path of the bucket where you want to download the file:\n >')
fpts = input('\nEnter the path where you want the downloaded bucket file to be stored:\n >')

def download_file(bucket_file_path, file_path_to_save):
    
    # Create an S3 access object
    s3 = boto3.client("s3")

    s3.download_file(Bucket="team247-bucket", Key=bucket_file_path, Filename=file_path_to_save)

    print(f'\nFile {bucket_file_path} saved in the following path {file_path_to_save}')
    

download_file(bfp, fpts)

##Example
##import boto3
##
##s3 = boto3.client('s3')
##s3.download_file('team247-bucket', 'raw/tweets_2019_to_2022.csv', './file.csv')
