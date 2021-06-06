# awsselect
S3 Select offered by AWS allows easy access to data in S3. It is a feature that enables users to retrieve a subset of data from S3 using simple SQL expressions. S3 is a large datastore that stores TBs of data. Without S3 Select, you would need to fetch all files in your application to process. However, with S3 Select, you can use a simple SQL expression to fetch only the data from the files you need in filtered and structured form instead of retrieving the entire object.

![aws s3 select](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2017/11/28/s3_select.png)

awsselect is a pyton wrapper which has been developed using aws python sdk where user just need pass certain parameter to access data.

# Quick Start
1. Install AWS CLI on your local laptop or on the machine where you want to run this script
2. Configure AWS CLI 
3. Install python3 on the machine
4. Install boto3 python package
5. run following command<br/>
   python3 s3select_csv.py --help
<pre>
s3select_csv.py [-h] [--bucket_name BUCKET_NAME]<br/>
                       [--file_name FILE_NAME] [--columnStr SELECT_COL]<br/>
                       [--filter_condition FILTER_CONDITION]<br/>

optional arguments:
  -h, --help            show this help message and exit
  --bucket_name BUCKET_NAME
                        S3 bucket name
  --file_name FILE_NAME
                        filename
  --columnStr COLUMNSTR
                        comma seprated string of output columns e.g-
                        empid,salary
  --sql_query SQL_QUERY
                        sql query
  --output_file OUTPUT_FILE
                        output file name e.g- output and file will be created
                        as output.zip

                        </pre>
                        
  ## for example
  upload employee.csv file into the bucket <br/>
  <pre>python3 s3select_csv.py --bucket_name spyglasslearning --file_name employee.csv --sql_query "select AVG(CAST(s.salary as float)) from s3object s" --columnStr avg --output_file avg_output
  
  python3 s3select_csv.py --bucket_name spyglasslearning --file_name employee.csv --sql_query "select s.salary,s.empid from s3object s" --columnStr salary,empid --output_file sample_output
  
  </pre>
  
  
  ## Dependencies Link
  * [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
  * [Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
  * [Install boto3](https://pypi.org/project/boto3/)
  * [Sql Function supported by S3](https://docs.amazonaws.cn/en_us/AmazonS3/latest/userguide/s3-glacier-select-sql-reference-aggregate.html)
  
