# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

 This model was developed by Jared Kline, beginning on December 13, 2025
 The version of this model is 1.0
 This is a random forest classifier model.
 It was created without a license.
 Please direct questions to jaredhkline@yahoo.com
 
## Intended Use

This model is intended to predict, based on a number of demographic factors found in a census data file, whether an individual makes more or less than $50,000 in a year.

## Training Data
This was generated using a standard 80-20 split from the full data set, 20% of that being the training data.
## Evaluation Data
Per https://archive.ics.uci.edu/dataset/20/census+income, this data was extracted from the 1994 Census database.
It includes 14 features, in addition to the salary column that determines whether an individual earns more or less than 50k. From the data.py comments: It was preproccessed using one hot encoding for the categorical features and a label binarizer for the labels, and the salary column was converted to a binary value.
## Metrics
Overall:
Precision: 0.7391 | Recall: 0.6365 | F1: 0.6840

Workclass:
workclass: ?, Count: 389
Precision: 0.6333 | Recall: 0.4524 | F1: 0.5278
workclass: Federal-gov, Count: 191
Precision: 0.7681 | Recall: 0.7571 | F1: 0.7626
workclass: Local-gov, Count: 387
Precision: 0.7647 | Recall: 0.7091 | F1: 0.7358
workclass: Private, Count: 4,578
Precision: 0.7333 | Recall: 0.6344 | F1: 0.6802
workclass: Self-emp-inc, Count: 212
Precision: 0.7759 | Recall: 0.7627 | F1: 0.7692
workclass: Self-emp-not-inc, Count: 498
Precision: 0.7264 | Recall: 0.4904 | F1: 0.5856
workclass: State-gov, Count: 254
Precision: 0.7500 | Recall: 0.6575 | F1: 0.7007
workclass: Without-pay, Count: 4
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000

Education:
education: 10th, Count: 183
Precision: 0.3333 | Recall: 0.1667 | F1: 0.2222
education: 11th, Count: 225
Precision: 1.0000 | Recall: 0.3636 | F1: 0.5333
education: 12th, Count: 98
Precision: 1.0000 | Recall: 0.4000 | F1: 0.5714
education: 1st-4th, Count: 23
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: 5th-6th, Count: 62
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
education: 7th-8th, Count: 141
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
education: 9th, Count: 115
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
education: Assoc-acdm, Count: 198
Precision: 0.6750 | Recall: 0.5745 | F1: 0.6207
education: Assoc-voc, Count: 273
Precision: 0.6415 | Recall: 0.5397 | F1: 0.5862
education: Bachelors, Count: 1,053
Precision: 0.7465 | Recall: 0.7200 | F1: 0.7330
education: Doctorate, Count: 77
Precision: 0.8525 | Recall: 0.9123 | F1: 0.8814
education: HS-grad, Count: 2,085
Precision: 0.6518 | Recall: 0.4232 | F1: 0.5132
education: Masters, Count: 369
Precision: 0.8310 | Recall: 0.8551 | F1: 0.8429
education: Preschool, Count: 10
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: Prof-school, Count: 116
Precision: 0.8105 | Recall: 0.9167 | F1: 0.8603
education: Some-college, Count: 1,485
Precision: 0.7005 | Recall: 0.5487 | F1: 0.6154

Marital-Status:
marital-status: Divorced, Count: 920
Precision: 0.7755 | Recall: 0.3689 | F1: 0.5000
marital-status: Married-AF-spouse, Count: 4
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
marital-status: Married-civ-spouse, Count: 2,950
Precision: 0.7320 | Recall: 0.6892 | F1: 0.7100
marital-status: Married-spouse-absent, Count: 96
Precision: 1.0000 | Recall: 0.2500 | F1: 0.4000
marital-status: Never-married, Count: 2,126
Precision: 0.8077 | Recall: 0.4078 | F1: 0.5419
marital-status: Separated, Count: 209
Precision: 1.0000 | Recall: 0.4211 | F1: 0.5926
marital-status: Widowed, Count: 208
Precision: 1.0000 | Recall: 0.1579 | F1: 0.2727

Occupation:
occupation: ?, Count: 389
Precision: 0.6333 | Recall: 0.4524 | F1: 0.5278
occupation: Adm-clerical, Count: 726
Precision: 0.6234 | Recall: 0.5000 | F1: 0.5549
occupation: Armed-Forces, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
occupation: Craft-repair, Count: 821
Precision: 0.6484 | Recall: 0.4586 | F1: 0.5372
occupation: Exec-managerial, Count: 838
Precision: 0.7989 | Recall: 0.7506 | F1: 0.7740
occupation: Farming-fishing, Count: 193
Precision: 0.6000 | Recall: 0.2143 | F1: 0.3158
occupation: Handlers-cleaners, Count: 273
Precision: 0.6667 | Recall: 0.3333 | F1: 0.4444
occupation: Machine-op-inspct, Count: 378
Precision: 0.5714 | Recall: 0.4255 | F1: 0.4878
occupation: Other-service, Count: 667
Precision: 0.8750 | Recall: 0.2692 | F1: 0.4118
occupation: Priv-house-serv, Count: 26
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
occupation: Prof-specialty, Count: 828
Precision: 0.7833 | Recall: 0.7653 | F1: 0.7742
occupation: Protective-serv, Count: 136
Precision: 0.7241 | Recall: 0.5000 | F1: 0.5915
occupation: Sales, Count: 729
Precision: 0.7314 | Recall: 0.6667 | F1: 0.6975
occupation: Tech-support, Count: 189
Precision: 0.7059 | Recall: 0.7059 | F1: 0.7059
occupation: Transport-moving, Count: 317
Precision: 0.6170 | Recall: 0.4531 | F1: 0.5225

Relationship:
relationship: Husband, Count: 2,590
Precision: 0.7343 | Recall: 0.6897 | F1: 0.7113
relationship: Not-in-family, Count: 1,702
Precision: 0.7766 | Recall: 0.3883 | F1: 0.5177
relationship: Other-relative, Count: 178
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
relationship: Own-child, Count: 1,019
Precision: 1.0000 | Recall: 0.1765 | F1: 0.3000
relationship: Unmarried, Count: 702
Precision: 1.0000 | Recall: 0.3111 | F1: 0.4746
relationship: Wife, Count: 322
Precision: 0.7122 | Recall: 0.6923 | F1: 0.7021

Race:
race: Amer-Indian-Eskimo, Count: 71
Precision: 0.6250 | Recall: 0.5000 | F1: 0.5556
race: Asian-Pac-Islander, Count: 193
Precision: 0.7833 | Recall: 0.7581 | F1: 0.7705
race: Black, Count: 599
Precision: 0.7755 | Recall: 0.5846 | F1: 0.6667
race: Other, Count: 55
Precision: 0.8000 | Recall: 0.6667 | F1: 0.7273
race: White, Count: 5,595
Precision: 0.7360 | Recall: 0.6345 | F1: 0.6815

Sex:
sex: Female, Count: 2,126
Precision: 0.7246 | Recall: 0.5193 | F1: 0.6050
sex: Male, Count: 4,387
Precision: 0.7411 | Recall: 0.6570 | F1: 0.6965

Native-Country:
native-country: ?, Count: 125
Precision: 0.6897 | Recall: 0.6452 | F1: 0.6667
native-country: Cambodia, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Canada, Count: 22
Precision: 0.8000 | Recall: 1.0000 | F1: 0.8889
native-country: China, Count: 18
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Columbia, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Cuba, Count: 19
Precision: 0.7143 | Recall: 1.0000 | F1: 0.8333
native-country: Dominican-Republic, Count: 8
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Ecuador, Count: 5
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
native-country: El-Salvador, Count: 20
Precision: 0.5000 | Recall: 1.0000 | F1: 0.6667
native-country: England, Count: 14
Precision: 0.6667 | Recall: 0.5000 | F1: 0.5714
native-country: France, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Germany, Count: 32
Precision: 0.7692 | Recall: 0.7692 | F1: 0.7692
native-country: Greece, Count: 7
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Guatemala, Count: 13
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Haiti, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Honduras, Count: 4
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Hong, Count: 8
Precision: 0.5000 | Recall: 1.0000 | F1: 0.6667
native-country: Hungary, Count: 3
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
native-country: India, Count: 21
Precision: 0.7000 | Recall: 0.8750 | F1: 0.7778
native-country: Iran, Count: 12
Precision: 0.5000 | Recall: 0.4000 | F1: 0.4444
native-country: Ireland, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Italy, Count: 14
Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
native-country: Jamaica, Count: 13
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Japan, Count: 11
Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
native-country: Laos, Count: 4
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Mexico, Count: 114
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
native-country: Nicaragua, Count: 7
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Peru, Count: 5
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Philippines, Count: 35
Precision: 1.0000 | Recall: 0.7500 | F1: 0.8571
native-country: Poland, Count: 14
Precision: 0.5000 | Recall: 0.5000 | F1: 0.5000
native-country: Portugal, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Puerto-Rico, Count: 22
Precision: 0.8333 | Recall: 0.8333 | F1: 0.8333
native-country: Scotland, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: South, Count: 13
Precision: 0.5000 | Recall: 0.5000 | F1: 0.5000
native-country: Taiwan, Count: 11
Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
native-country: Thailand, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Trinadad&Tobago, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: United-States, Count: 5,870
Precision: 0.7375 | Recall: 0.6286 | F1: 0.6787
native-country: Vietnam, Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Yugoslavia, Count: 2
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000

## Ethical Considerations
As always, but especially when looking at data related to race, national origin, sex, or any other category by which people might be marginalized, we need to be careful that we are not confusing correlation with causation.

## Caveats and Recommendations
This was created by a student, which honestly means it shouldn't be used for anything other than evaluating the student's ability to complete the assignment. Certainly it shouldn't be used for any manner of policy decision. Also, this was a relatively small subset of census data. Some groups were over- or under-represented: for example, the group was two-thirds male, overwhelmingly native-born, and had eight times as many husbands as wives.

