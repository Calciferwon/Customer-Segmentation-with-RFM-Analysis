# Health Data-Analysis
Data is provided from a state that includes 4 regions: Souhtheast, Southwest, Northeast and Northwest.
People live in this state are tracked with age, body index via BMI, smoking status (yes or no), how many children they have and which region they live in specifically.
I. Descriptive Statistical Analysis
1. Data Characteristics:
Data field 1: age (integer)
Data field 2: sex (female/male - text)
Data field 3: bmi index (float)
Data field 4: children - number of children (integer)
Data field 5: smoker (yes/no - text)
Data field 6: region - where living (text)
Data field 7:charges - cost for healthcare
Observation: 1338
2. Data Groups:
2.1. Region:
Patients recorded in this data are distributed in 4 areas. Set dummies for regions:
- Southeast: 364 patients ~ 27.20% - 4
- Southwest: 325 petients ~ 24.29% - 2
- Northeast: 324 patients ~ 24.22% - 3
- Northwest: 325 patients ~ 24.29% - 1
2.2 Sex:
Set dummies for sex with new data field: Gender
Female - 0
Male - 1
2.3 Smoker:
Set dummies for smoker with new data field: Smoking
Yes - 1
No - 0
2.4. Children:
Group data in this field to 4 group:
- Have no child: 1
- Have from 1 to 3 child/childrens: 2
- Have 4 children: 3
- Have 5 children: 4
2.5. BMI
Based on the definition of CDC - United States, we can group bmi data field to 4 groups:
- Skinny group - bmie under 18.5: 1
- Balanced group - bmi from 18.5 to 25: 2
- Over weight group - bmi from 26 to 30: 3
- Highly over weight group - bmie over 30: 4
2.6. Age:
Following to aging conditions, we can devide our data to 4 groups of age:
- From 18 to 29 year-old - early adulthood: 1
- From 30 to 39 year-old - adulthood: 2
- From 40 to 50 year-old - middle age: 3
- Above 50 year-old: old age: 4
2.7 Charges:
From the dataset, we can have 4 groups following to 4 quartiles:
Group 1: under 4,738.27
Group 2: from 4746.34 – 9377.90
Group 3: from 9386.16 – 16586.50
Group 4: Above 16657.72

II. Inferential Statistical Analysis
From the dataset, we can predict that the healthcare cost may depend on some independent variables such as age, sex, bmi index, smoker or not, region where living and number of children. Therefore we set up a linear regression model to check if there is any relationship between variables above.
To see the results, check Python code: health_cost_analysis_linear regression.py

III. RFM Analysis
From the linear regression model, we remove 2 variables that do not affect on the healthcare cost: region and gender
After run the Python code: health_cost_analysis_rfm.py
We 're able to segment all the patients in the dataset to the following groups with scores:
1. Patient group with a lot of health problems. They will have to pay much for healthcare and be target 
Best Customers:  47 patients
2. Patients who get at least one health problem (smoking/overweight) and pay much for healthcare:
Potential Customers:  276 patients
3. Smoking group needed to be warned about the danger of smoking
Smoking Warning:  274 patients
4. Overwight group needed to be warned about the danger of overweight
Weight Warning:  705 patients
5. Patients who spend a lot of money for healthcare
Big Health Spenders:  335 patients
6. Patients who pay least for healthcare
Small Health Spenders:  46 patients
7. Patients who are strong and not willing to pay for healthcare:
Least Potential Customer:  54 patients
8. Others
Normal Customers:  739 patient
