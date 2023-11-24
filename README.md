# Anomaly_detection

 an anomaly is something that differs from a norm: a deviation, an exception. In software engineering, by anomaly we understand a rare occurrence or event that doesn’t fit into the pattern, and, therefore, seems suspicious. Some examples are:

a.sudden burst or decrease in activity;

b.error in the text;

c.sudden rapid drop or increase in temperature.


The various reasons for anomaly in the data

1.noise
2.fraud
3.attacks
4.theft


Anomaly Detection:
Identifying anomalies or outliers are one of the most common use cases of Machine Learning and Deep Learning problems.


Types of Anomalies (source: https://www.knowledgehut.com/blog/data-science/machine-learning-for-anomaly-detection#what-is-an-anomaly? )
1. Global or Point Outliers: These anomalies are discrete data points that stand out from the rest of the dataset in a significant way. They are singular occurrences that stand out because of their strong ideals or peculiar traits. By taking into account the statistical characteristics of the entire dataset, global outliers are frequently found.

2. Contextual Outliers: Contextual outliers are data points that differ from the predicted behavior within a particular context or subgroup. They are sometimes referred to as conditional or contextual abnormalities. When studied within a certain context or scenario, these anomalies may appear normal when viewed in the context of the larger dataset.

3. Collective Outliers: Collective outliers are anomalies that exist inside a subset or group of data points, also known as group anomalies or structural anomalies. It is the relationship or combination of data points that deviates from what is expected, not the individual data points, which are anomalous. Analyzing the patterns, dependencies, or linkages among the data points is necessary to spot collective outliers.


Why do You Need Machine Learning for Anomaly Detection? 

Machine learning plays a crucial role in anomaly detection for several reasons:

Complexity and Volume of Data: Traditional rule-based or statistical methods may not be adequate to detect anomalies efficiently due to the growing volume and complexity of data. Anomaly detection jobs benefit from machine learning algorithms' ability to process vast volumes of data and automatically identify patterns.

Unlabeled Data: It can be difficult to develop precise rules or thresholds for detection when abnormalities are not explicitly marked or specified. Machine learning algorithms can gain knowledge from unlabeled data, revealing hidden patterns and spotting deviations from the norm.

Adaptive Learning: Machine learning models can adjust to new data and learn from it, continuously enhancing their ability to spot anomalies. By modifying their understanding of typical behaviors considering new information, they can spot developing or previously undetected anomalies.

Feature Extraction: Extraction of pertinent features or attributes from the data is a common step in anomaly detection. The accuracy and effectiveness of anomaly detection can be improved by using machine learning techniques to automatically recognize and extract valuable features from complicated datasets.

Detection of Complex Anomalies: Anomalies can take on many different forms, making it challenging to detect them with conventional techniques. Deep learning models and other machine learning algorithms may identify complicated correlations and patterns in data, allowing for the detection of complex anomalies.