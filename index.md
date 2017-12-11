# What is Apache Spark

In big picture perspective, Apache Spark can be considered as an all in one package Lambda Architecture solution.

***Batch layer:***
-	Spark Core that includes high-level API and an optimized engine that supports general execution graphs.

***Serving Layer:***
-	Spark SQL for SQL and structured data processing.

***Speed Layer:***
-	Spark Streaming that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.

Batch processing using Spark might be quite expensive and will not fit for all scenarios and data volumes, but the easy integration with the Hadoop Ecosystem allow it to generalize into more use cases.

#### Example of a Lambda Architecture with Spark

![Example Lambda Architecture]({{site.baseurl}}//pipeline-2.png)

[Read More](https://dzone.com/articles/lambda-architecture-with-apache-spark)


## History

Apache Spark was first developed in 2009 by AMPLab at UC Berkeley as a research project. It started with the creation of Mesos (a cluster management tool) and wanting a system to be built on top of it by some of the original developers lead by Ion Stoica (UC Berkley Professor, and CEO of DataBricks). Requirements for Machine Learning on top of Hadoop was being introduced by the University, and many near-by tech companies, including Stoica’s company Conviva, had required interactive fast querying abilities. It was first released at May 30th, 2014 (only 3 years ago) and later donated to the Apache Software Foundation which has maintained it ever since.

[Interview with Ion Stoica](http://blog.madhukaraphatak.com/history-of-spark/)

## Functionalities

It is an open-source, fault-tolerant batch-computing framework like Hadoop. It provides us several APIs to manipulate a special kind of datasets called RDD (Resilient Distributed Dataset), a distributed memory abstraction that lets programmers perform in-memory computations on large clusters in a fault-tolerant manner. RDDs were motivated by the needs for iterative algorithms and interactive data mining tools. In both cases, keeping data in memory can improve performance by an order of magnitude.

![Spark Framework]({{site.baseurl}}//SparkFramework.png)
---
Spark Core is the foundational component:

- **Spark Core**
 
Spark Core provides distributed task dispatching, scheduling, basic I/O etc. All these functionalities are exposed through an application programming interface (for Java, Python, Scala, and R) called driver program. We tell the driver program what we want to do by passing a function. And it calls the Spark Core to do the low-level jobs for us.

Built on top of the Spark Core, Spark provide 4 higher-level libraries for special purpose jobs:

- **Spark SQL**
 
Spark SQL provides a data abstraction called DataFrames that support both structured or semi-structured data. 

- **Spark Streaming**
 
Spark Streaming is used for steaming analysis because of the speed of computation.

- **MLlib**
 
MLlib is used for machine learning jobs. Specifically, it includes following machine learning techniques and models:
    - Statistics like correlations, stratified sampling, hypothesis testing, random data generation.
    - Classificationa and Regression like SVM, logistic regression, linear regression, decisoon tree, naive Bayes.
    - Collaborativbe Filtering like alternating least squares
    - Cluster Analysis like kmeans and Latent Dirichletian Allocation
    - Dimension Reduction like SVD and PCA
    - Feature Extraction and Transformation
    - Optimization like SGD, L-BFGS.

- **GraphX**
 
GraphX is used for graph processing like PageRank and so on.

---

# What is special about Spark

All we do with data can be generalized as applying some operations on some dataset. Spark is designed in this way too.

## RDD
The special kind of datasets in Spark--**Resilient Distributed Datasets(RDDs)**--form the foundation of Spark. Basically, an RDD is a collection of tuples. What is special about RDD is that you can keep it in memories of machines by using ``persist()`` or ``cache()`` method. On addition to that, you can specify the storage level to control how it is saved. 

By default, Spark saves the RDD as de-serialized Java objects in memory. And if the RDD is too big, the part that doesn't fit will not be cached and will be recomputed on the fly every time they are needed. (For the full set of storage levels and their details, check [here.](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence))

This is the key difference between Spark and Hadoop. Because as we know, Hadoop dose not save any output in memory, even the intermediate key/value pairs coming out of map function are saved to local disk and being retrieved by reducer. The serialization/deserialization during I/O make the process very inefficient if we need to use the same dataset from time to time. (Think about tuning models in Machine Learning.) In contrast, the RDDs used in Spark can stay in memory thus allows up to use them iteratively and interactively repeatedly without having to read them from disk.

## Operations:
The operations to manipulate RDD in Spark are high level and flexible. It is high-level because it saves us from disk I/Os and provide a variety of high-level operations like JCascalog and other libraries for Hadoop. It is flexible because lots of the operations work with custom functions implemented for specific purpose by ourselves. In general, the operations are categorized into transformations and actions:

- **Transformations: all the operations take in RDD and return a new RDD are considered transformations.** Below are some of them:

    | Transformation | Meaning |
    | --- | --- |
    | map(function) | use the input function to process each row of RDD and return a new processed RDD|
    | filter(function) | use the input function to evaluate each row of RDD and remove the rows evaluated false |
    | union(otherDataset) | return the union of 2 data sets based on identical fields |
    | reduceByKey(function, [numTasks]) | return a new RDD in which values of same key are aggregated |
    | ... | ...|

- **Actions: all the operations take in RDD and return something that is not RDD are considered actions.** For example:

    | Actions | Meaning |
    | --- | --- |
    | reduce(function) | aggregate the elements of RDD using provided function|
    | collect() | return all the elements in RDD as an array |
    | rake(n) | return the elements of first n rows in RDD as an array |
    | saveAsSequenceFile(path) | with the elements of the dataset as a Hadoop SequenceFile in a given path in local filesystem |
    | ... | ...|

For more operations and details, check -> [https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations](https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations)

On addition to these basic, one-step type of operations, Spark offers more complex operations in those 4 specific purpose libraries we talked about in last section. And these complex operations are nothing more than a combination of basic operations.

# When should we use it
As we said, the main advantage of Spark is the RDD. It's fast for iterative algorithm and interactive developing environment. And it's convenient to use those 4 specific purpose libraries if they suit our needs.

### References
Apache Spark Documentation: [(https://spark.apache.org/docs/latest/index.html)](https://spark.apache.org/docs/latest/index.html)
Wikipedia: Apache Spark: ()
Apache Spark GitHub Repository: [(https://github.com/apache/spark)](https://github.com/apache/spark)

### The Apache spark project
More info: [The Apache Spark Project](https://spark.apache.org/)

---

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
$ docker run -it -p 8888:8888 jupyter/pyspark-notebook
```

2. Take note of the authentication token and open it in a browser.

The image lives [here.]( https://github.com/jupyter/docker-stacks/tree/master/pyspark-notebook)

It includes:
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

# Using Spark

## With Docker Image

1. After launching the image you should recive an output as shown below 

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
$ ./bin/pyspark --master local[4] --py-files yourScript.py
```

And if we would also like to import yourScript later in the shell, run: 
```
$ ./bin/pyspark --master local[4] --py-files yourScript.py
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


# Project Contributors:
#### [Caleb Hulburt](https://github.com/cmhulbert)
#### [Mohammad Azim](https://github.com/moazim1993)
#### [Xian Lai](https://github.com/Xianlai)
#### [Yao Jin](https://github.com/jinyaohh)


Group Project for Big Data Programming, Fall 2017

Project master repository: 
[Master Branch](<https://github.com/Xianlai/BigData_Spark>)