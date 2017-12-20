# Connecting pyspark to a aws cluster
Using spark on a remote cluster is more complicated than on local machine.

## 1. Set up a cluster
First we need to have a cluster of slaves available for pyspark. Here we will use AWS EC2 machines. 

### 1.1 Create a AWS account
-> https://aws.amazon.com/free/

### 1.2 Set up Identity and Access Management(IAM)
- Once you have your account, go to the [aws management console](https://aws.amazon.com/console/) and sign in.

- Go to IAM service, this service help you secure your aws account. [More information here](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 

- Create a user, a group and a role when needed. 
[More information here](http://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)

- Take note of Security Credentials under the Users section.

### 1.3 Use EC2 service
Go to EC2 service in management cosole. We can set up EC2 instances and manage them from here. But for convinience, we will use the aws commandline tools and flintrock.

#### install awscli and flintrock
For Max and Linux, run `$ pip install awscli` and `$ pip3 install flintrock`
[awscli webpage](https://aws.amazon.com/cli/)
[flintrock webpage](https://github.com/nchammas/flintrock)

#### Set up aws configuration
- run `$ aws configure` in your terminal and enter your account credential information. (Your note from 1.2):
```
AWS Access Key ID [****************WBKQ]: 
AWS Secret Access Key [****************dVIp]: 
Default region name [us-east-1]: 
Default output format [None]: 
```

- create a key-pair permission by run 
```
aws ec2 create-key-pair \
--key-name [MyKeyPair] \
--query 'KeyMaterial' \
--output text > [MyKeyPair].pem
```

- change the file permission of the private key file by run `$ chmod 400 MyKeyPair.pem`

[More information here](http://docs.aws.amazon.com/cli/latest/userguide/cli-ec2-keypairs.html)

#### Set up cluster using flintrock
- set up flintrock configuration by run `$ flintrock configure`. And then enter your key-name, key file path, instance-type and region in the configuration YAML file.

Your YAML file should look similar to this:
```
...
providers:
  ec2:
    key-name: YourKeyName
    identity-file: YourKeyFile
    instance-type: t2.micro(choose the instance type you like)
    region: us-east-1(shoud match with the region setting in aws configure)
    ...
    ami: ami-a4c7edb2   # Amazon Linux, us-east-1
    user: ec2-user
    ...
launch:
  num-slaves: 5
  ...
...
```

- initialize a AWS cluster by run `$ flintrock launch spark-test`.
If lucky, the cluster will be set up and you will see the following result:
```
...
launch finished in 0:04:52.
Cluster master: ec2-52-90-93-178.compute-1.amazonaws.com
Login with: flintrock login spark-test
```

- When the cluster is lauched, you can get information about this cluster by using flintrock command: `flintrock describe spark-test`
```
spark-test:
  state: running
  node-count: 6
  master: ec2-52-90-93-178.compute-1.amazonaws.com
  slaves:
    - ec2-52-91-188-159.compute-1.amazonaws.com
    - ec2-54-235-230-209.compute-1.amazonaws.com
    - ec2-52-90-79-28.compute-1.amazonaws.com
    - ec2-34-227-20-146.compute-1.amazonaws.com
    - ec2-54-174-146-59.compute-1.amazonaws.com
```
or you can monitor the instances through AWS console 
or you can visit http://<master-public-dns>:8080.

- Login with: `$ flintrock login spark-test`


## 2. Install required softwares on the cluster
- update the existing softwares by run `[aws-master]$ sudo yum update -y`

- install Anaconda3-5.0.1-Linux-x86.sh by run 
```
[aws-master]$ wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh

[aws-master]$ sh Anaconda3-5.0.1-Linux-x86_64.sh

[aws-master]$ export PATH=/home/EC2-user/path/to/anaconda3/bin:$PATH
```
on the remote machine.

- install pyspark by run `[aws-master]$ conda install -c conda-forge pyspark`

- exit and login again


## 3. Run jupter notebook remotely and open it locally

- run `[aws-master]$ jupyter notebook` on the remote machine to start the jupyter notebook and take note of the token given.

- open a new terminal on your local machine, run:
```
$ ssh -i YourPemFile.pem \
  -L 8000:localhost:8888 \
  ec2-user@ec2-52-90-93-178.compute-1.amazonaws.com
```
to allow your local machine listen to the remote machine.

- open localhost:8000 in your browser on your local machine and enter the token. You will enter the jupyter notebook on the remote machine.


## 4. Set up SparkContext
Inside the Jupyter notebook, you should tell the spark where master machine is:
```
from pyspark import SparkContext, SparkConf
MASTER = "spark://<master-public-dns>:7077"
conf = SparkConf().setAppName("spark-test").setMaster(MASTER)
sc = SparkContext(conf=conf)
```


## 5. Exit from remote master and stop the running cluster
run `exit` to exit the remote shell.
run `flintrock stop spark-test` to stop the cluster.


## 6. Destroy the cluster
run `flintrock destroy spark-test`


## 7. References
[1] http://spark.apache.org/docs/latest/quick-start.html

[2] http://spark.apache.org/docs/latest/configuration.html#dynamically-loading-spark-properties

[2] http://spark.apache.org/docs/1.4.1/submitting-applications.html

[3] http://spark.apache.org/docs/1.4.1/cluster-overview.html

[4] https://github.com/PiercingDan/spark-Jupyter-AWS

[5] Setting up and using Jupyter Notebooks on AWS https://towardsdatascience.com/setting-up-and-using-jupyter-notebooks-on-aws-61a9648db6c5

[6] How to Run Spark Application https://www.cs.duke.edu/courses/fall15/compsci290.1/TA_Material/jungkang/how_to_run_spark_app.pdf

[7] https://github.com/nchammas/flintrock




















