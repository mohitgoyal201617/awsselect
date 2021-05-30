import boto3
import io
import pandas as pd
import argparse

def query_csv_s3(s3, bucket_name, filename, sql_exp):

    header = "Use"
    #  query and create response
    resp = s3.select_object_content(
        Bucket=bucket_name,
        Key=filename,
        ExpressionType='SQL',
        Expression=sql_exp,
        InputSerialization = {'CSV': {"FileHeaderInfo": header}},
        OutputSerialization = {'CSV': {}},
    )
    
    #  upack query response
    records = []
    for event in resp['Payload']:
        if 'Records' in event:
            records.append(event['Records']['Payload'])  
        
    #  store unpacked data as a CSV format
    file_str = ''.join(req.decode('utf-8') for req in records)
    
    return file_str



parser=argparse.ArgumentParser()

parser.add_argument('--bucket_name', help='S3 bucket name')
parser.add_argument('--file_name', help='filename')
parser.add_argument('--select_col', help='comma separated column list with s. as prefix with every column name e.g s.empid')
parser.add_argument('--filter_condition', help='filter condition like  e.g s.empid \> \'2\'')
args=parser.parse_args()

#  start client with s3
s3 = boto3.client('s3')

# column selection
columStr=args.select_col

#filter condition
filter=args.filter_condition

#  define file location and name
bucket_name = args.bucket_name
filename = args.file_name

#  create SQL expression to query by date using column names
sql_exp = ("SELECT "+columStr+" FROM s3object s where "+filter) 

#  should we use header names to filter
#use_header = True

#  return CSV of unpacked data
file_str = query_csv_s3(s3, bucket_name, filename, sql_exp)
print(file_str)

#create column list
colList=columStr.replace("s.","").split()
df = pd.read_csv(io.StringIO(file_str), names=colList)
print(df)


