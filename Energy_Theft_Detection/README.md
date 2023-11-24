# Energy Theft Detection

Energy Production and Consumption is a multi billion dollar industry worldwide. One of the major challenges this industry faces is energy theft.
The energy theft problem not only leads to financial losses for the energy company but also leads to various problems with the grid system itself.
As per a report in Forbes(https://www.forbes.com/sites/forbestechcouncil/2022/09/06/why-energy-theft-is-preventing-global-decarbonization/?sh=e7fc1e24ff4b) Electricity fraud cost the energy industry as much as $96 billion dollar.

The energy theft can happen in 3 different ways.

First a Direct theft where the meter is partially or completely bypassed so actual consumption not recorded.

Second Tariff misuse a customer’s electricity use type is mischaracterized, and an incorrect lower tariff is applied (i.e., energy use is misrepresented as a residential property even though it is used for commercial purposes).


Third meter tampering When the meter itself is tampered with to prevent consumption from registering. 

To tackle the problem AI enabled meter intelligence or 'Smart Meter' installation is needed But there are billions of consumers who has not installed smart meter. For those cases theft detection pipeline can be developed using Machine Learning or Deep Learning method.


https://ieeexplore.ieee.org/abstract/document/8610248 is a paper which discusses feature engineering and applying gradient boosting base classifiers on theft detection problem.

https://iarjset.com/wp-content/uploads/2021/01/IARJSET.2020.71203.pdf paper discusses many approaches to solve this problem.

Energy Theft Detection problem is essentially an anomaly detection problem because For an energy provider there are millions of customer and only few hundred thousand theft cases can be confirmed. Hence, the problem presents itself as a severely imbalanced classification problem where positive to negative class ratio would be essentially less than 1%.

Analysing the consumption pattern is the key component for solving this problem. Because energy theft can not be detected using any other parameter. The distribution of energy consumption of a consumer with theft will be different than a consumer with no theft.

The data set which would reflect the complexity and real world challenges is not available online. For this repo the data set is taken from https://www.kaggle.com/datasets/avinemmatty/theft-data and does not have the complexity of real time data.
But the approaches taken here can be applied to real life problems of energy detection and is scalable.

