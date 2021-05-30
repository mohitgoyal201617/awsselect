# awsselect
S3 Select offered by AWS allows easy access to data in S3. It is a feature that enables users to retrieve a subset of data from S3 using simple SQL expressions. S3 is a large datastore that stores TBs of data. Without S3 Select, you would need to fetch all files in your application to process. However, with S3 Select, you can use a simple SQL expression to fetch only the data from the files you need in filtered and structured form instead of retrieving the entire object.

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
                       [--file_name FILE_NAME] [--select_col SELECT_COL]<br/>
                       [--filter_condition FILTER_CONDITION]<br/>

optional arguments:<br/>
  -h, --help            show this help message and exit<br/>
  --bucket_name BUCKET_NAME
                        S3 bucket name<br/>
  --file_name FILE_NAME
                        filename<br/>
  --select_col SELECT_COL
                        comma separated column list with s. as prefix with
                        every column name e.g s.empid<br/>
  --filter_condition FILTER_CONDITION
                        filter condition like e.g s.empid \> '2' 
                        </pre>
                        
  ## for example
  upload employee.csv file into the bucket <br/>
  <pre>python3 s3select_csv.py --bucket_name <bucketname> --file_name employee.csv --select_col s.empid,s.salary --filter_condition s.empid\>\'2\'</pre>
  
  ## Dependencies Link
  * [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
  * [Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
  * [Install boto3](https://pypi.org/project/boto3/)
  
