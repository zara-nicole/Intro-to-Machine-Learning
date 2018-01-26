""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data)) #number of people
print(len(enron_data.values()[0])) #number of features per person

#count number of POIs in the E+F dataset
count = 0
for user in enron_data:
    if enron_data[user]['poi'] == 1:
        count+=1
print count

#stock value of James Prentice
print(enron_data["PRENTICE JAMES"]['total_stock_value'])

#number of emails from Wesley Colwell to POIs
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

#value of stock options exercised by Jeffrey K Skilling
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

#how much money did they take hojme
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])

# How is an unfilled feature denoted?
print(enron_data['FASTOW ANDREW S']['deferral_payments'])

# How many folks in this dataset have a quantified salary?
# What about a known email address?
count_salary = 0
count_email = 0
for key in enron_data:
    if enron_data[key]['salary'] != 'NaN':
        count_salary += 1

print count_salary
dict1 = dict((key, value) for key, value in enron_data.items() if value["email_address"] != 'NaN')
print len(dict1)

# How many people have no stated total payments
# percentage of whole

count_Nan_payments = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        count_Nan_payments += 1
print(count_Nan_payments)
print (float(count_Nan_payments)/len(enron_data))

# How many POIs have no stated total payments
# percentage of whole

count_Nan_payments = 0
for person in enron_data.keys():
    if enron_data[person]['poi'] == True and enron_data[person]['total_payments'] == 'NaN':
            count_Nan_payments += 1
print(count_Nan_payments)
print (float(count_Nan_payments)/18)
