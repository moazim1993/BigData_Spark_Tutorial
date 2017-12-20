# Getting Started

## Software Downloading and configuring for Mac OSX
We have 2 ways to config Spark environment before starting using it. The hard way is to install Java, Scala and Spark one by one. And the easy way is to install docker and pull an existing image from the internet.

## Easy way:
### Installing Docker
1. Download the Docker Community Edition for Mac from -> [https://store.docker.com/editions/community/docker-ce-desktop-mac](https://store.docker.com/editions/community/docker-ce-desktop-mac)

2. Double click it and follow the guide.

3. Open a command-line terminal, and try:
```
$ docker version
$ docker run hello-world
```
The first one check the version of docker. And the 2nd one verifies that Docker is pulling images and running as expected.

### Pulling Spark image
1. Run:
```
$ docker run -it -p 8888:8888 xianlai/spark_project
```

2. Take note of the authentication token and open it in a browser.

The image is built based on the image lives [here.]( https://github.com/jupyter/docker-stacks/tree/master/pyspark-notebook)

It includes:
- tweepy
- Bokeh
- Jupyter Notebook 5.2.x
- Conda Python 3.x environment
- pyspark, pandas, matplotlib, scipy, seaborn, scikit-learn
- Spark 2.2.0 with Hadoop 2.7
- Mesos client 1.2
- and so on


## Hard way:
### Installing Java
1. Download Java SE(standard edition)-JDK(Java developement kit) 9.0.1 from -> [http://www.oracle.com/technetwork/java/javase/downloads/jdk9-downloads-3848520.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk9-downloads-3848520.html)

2. Double click it and follow the guide.

### Installing Scala
1. Download the Scala binaries for osx from -> [http://www.scala-lang.org/download/](http://www.scala-lang.org/download/)

2. Extract the Scala tar file:
```$ tar xvf scala-2.12.3.tgz```

3. Move the extracted Scalar software files to /usr/local/scala (admin privilege needed):
```
    $ su -
    Password:
    # mkdir /usr/local/scala
    # cd /Users/YourUserName/Downloads
    # mv scala-2.12.3 /usr/local/scala
    # exit
```

4. Set path for Scala so the shell knows where to find the software when executing scala script:
```
    $ vim ~/.bash_profile
    append the following export command: 
    export PATH=$PATH:/usr/local/scala-2.12.3/bin
    save and quit
```

5. Verify your Scala is successfully installed:
```
    $ source ~/.bash_profile
    $ scala -version
```
If success, you should enter the scala REPL shell.

### Installing Spark
1. Download the Spark binaries for osx from -> https://spark.apache.org/downloads.html

2. Extract the Spark tar file:
```$ tar xvf spark-2.2.0-bin-hadoop2.7.tgz```

3. Move the extracted Spark software files to /usr/local/spark (admin privilege needed):
```
    $ su -
    Password:
    # mkdir /usr/local/spark
    # cd /Users/YourUserName/Downloads
    # mv spark-2.2.0-bin-hadoop2.7 /usr/local/spark
    # exit
```

4. Set path for Spark so the shell knows where to find the software when executing Spark script:
```
    $ vim ~/.bash_profile
    append the following export command: 
        export PATH = $PATH:/usr/local/spark/spark-2.2.0-bin-hadoop2.7/bin
    save and quit
```

5. Verify your Spark is successfully installed:
```
    $ source ~/.bash_profile
    $ spark-shell
```
If success, you should see a bunch of stuff and enter the spark shell in scala.

#### Install pyspark package
```
$ pip install pyspark
```
---
# Using Spark

## With Docker Image

1. After launching the image by running `$docker run -it -p 8888:8888 xianlai/spark_project`, you should receive an output as shown below 

```
C 18:56:29.415 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=Ab324539896c7a54bf0132dd43de342659c98573a89
 ```

2. As instructed, pasting the URL should open a fully equipt jyputer notebook.

## With full installation
1. go to where your spark installation folder is, for example: 
/usr/local/spark/spark-2.2.0-bin-hadoop2.7/

2. Use Spark either by coding in shell or directly launching our applications with spark-submit. Either way, we are able to tell the spark which master machine we want to connect to and what the configuration of Spark we would like to use.

### Coding in shell
You can set which master the context connects to using the --master argument, and you can add Python .zip, .egg or .py files to the runtime path by passing a comma-separated list to --py-files.

For example to run bin/pyspark locally on exactly four cores, run: 
```
$ ./bin/pyspark --master local[4]
```

And if we would also like to import yourScript later in the shell, run: 
```
$ ./bin/pyspark --master local[4] --py-files yourScript1.py, yourScript2.py
```

##### Using IPython instead of Python for spark-shell
```
$ PYSPARK_DRIVER_PYTHON=ipython
```

##### Using Jupyter instead of Python for spark-shell
```
$ PYSPARK_DRIVER_PYTHON=jupyter
```

### Running Python script
```
$ ./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key>=<value> \
  ... # other options
  <application-zip> \
  [application-arguments]
```

* --class: The entry point for your application (e.g. org.apache.spark.examples.SparkPi)

* --master: The master URL for the cluster (e.g. spark://23.195.26.187:7077 or local) 

* --deploy-mode: Whether to deploy your driver on the worker nodes (cluster) or locally as an external client (client) (default: client)

* --conf: Arbitrary Spark configuration property in key=value format. 

* application-zip: Path to a bundled zip file including your application and all dependencies. The URL must be globally visible inside of your cluster, for instance, an hdfs:// path or a file:// path that is present on all nodes.

* application-arguments: Arguments passed to the main method of your main class, if any.

For additional details, refer to the [docs.]( https://spark.apache.org/docs/latest/submitting-applications.html)

---

# Project Contributors:
#### [Caleb Hulburt](https://github.com/cmhulbert)
#### [Mohammad Azim](https://github.com/moazim1993)
#### [Xian Lai](https://github.com/Xianlai)
#### [Yao Jin](https://github.com/jinyaohh)


Group Project for Big Data Programming, Fall 2017

Project master repository: 
[Master Branch](<https://github.com/Xianlai/BigData_Spark>)
