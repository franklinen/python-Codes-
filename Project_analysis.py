# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:48:59 2019

@author: MAIN
"""

import os 
os.getcwd()
os.chdir(r'C:\Users\MAIN\Desktop\Python')
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

Lending_file = pd.read_csv("Loan_Directory1.csv", na_values=" ")
type(Lending_file)
Lending_file.shape
Lending_file.ndim
Lending_file.size
Lending_file.head()

#subsetting som colums of the data for analytucal focus on customer identity
cust_ID = pd.read_csv("Loan_Directory1.csv", na_values=" ",
                      usecols=[0,1,2,7,8,9,10,13,14,15], header=0,
                      names=['Loan_ID', 'Member_ID','Loan_Amount','Emp_Title',
                      'Emp_length','Home_ownership','Annual_Income','Loan_Purpose','State','Obligations'], 
                      dtype={'annual_Inc':np.float64})
cust_ID.head(10)
cust_ID.describe()

#was hoping to check the frequency of the loan taken up by individual customers.
#result showed that the data contained loan details for unique customers
Loan_Freq = cust_ID['Member_ID']
Loan_Freq
y = Loan_Freq.value_counts()
y.sort_values()
v = Loan_Freq.tolist()
v
plt.hist(v,5, histtype='bar', align='mid', color='g', label='Loan Frequency')
plt.legend(loc=2)
plt.title('Customer Retention')
plt.show()

cust_ID.describe()

####################################################################
#Found out there was no much difference in the mean loan amount received by each individal based on the 
#home ownership criteria. other factors like credit card history played a big part in the loan amount received
m = cust_ID.groupby(['Home_ownership',])['Loan_Amount'].mean()
m.head(20)

y= m.tolist()
x= m.keys().tolist()
pos = np.arange(len(m))

plt.bar(pos,y,color='blue',edgecolor='black')
plt.xticks(pos, x)
plt.xlabel('Home_ownership', fontsize=16)
plt.ylabel('Loan_Amount', fontsize=16)
plt.title('Barchart - Amount_Received',fontsize=20)
plt.show()

#sorting and grouping data by loan purpose and loan amount. Wanted to find the correlation between those values
y=cust_ID.sort_values(by = 'Loan_Purpose', na_position='first') #place any missing value first
y=cust_ID.sort_index(axis=1)
y=cust_ID.sort_index(axis=1, ascending= False)
y.head(10)

x=cust_ID.sort_values(['Loan_Purpose']) #place any missing value first
x.head(10)

z = x.groupby(['Loan_Purpose'])['Loan_Amount'].mean()  #grouping the data by loan purpose
z.head(10)

#why are most people taking loans from the lending company. Majority are taking 
#loans for debt consolidation. They see this medium as an avenue to pay off their
#outstanding loans. If you dont address the problem that caused the debt in the first place
#you may need another consolidation loan after paying off the first one.
lnp_count = cust_ID['Loan_Purpose'].value_counts()
lnp_count

#bar graph to show the distribution of loan purpose
y= lnp_count.tolist()
x= lnp_count.keys().tolist()
pos = np.arange(len(lnp_count))

plt.bar(pos,y,color='blue',edgecolor='black')
plt.xticks(pos, x)
plt.xlabel('Loan Purpose ', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.title('Barchart - Loan Purpose',fontsize=20)
plt.show()



w =cust_ID.sort_values(by = 'Loan_Amount', na_position='first')
w.head(10)

m = w.groupby(['Emp_Title', ])['Loan_Amount'].mean()
m.head(20)

#checking correlation coefficient for loan amount obligations. result showed a 
#weak negative correlation between the two factors
Loan_check = cust_ID[['Loan_Amount', 'Obligations']]
Loan_check
Loan_check.corr(method='pearson', min_periods =1)

#checking values in the original dataset
Lending_file.columns()

#subset of the cust_ID subset of the original dataset
sort_by_home_ownership = cust_ID.sort_values(['Home_ownership', 'Member_ID'])
sort_by_home_ownership.head(10)

#Subsetting  
Loan_performance = pd.read_csv("Loan_Directory1.csv", na_values=" ",
                      usecols=[0,1,2,4,11,12,15,17,18], header=0,
                      names=['Loan_ID', 'Member_ID','Loan_Amount','Interest_Rate',
                      'Loan_Verification','Loan_Status','Obligations', 'Utilization', 'Credit_Accounts'], 
                      dtype={'int_rate':np.float64})

Loan_performance.head(10)

#define average loan utilization
z = Loan_performance['Utilization'].mean()
z
# results show that the average utiization of the credit line was 52%. most people 
#are not using the lines available to them and that means reduced interest income compared to expectations

plt.interactive(False)#interactive mode is off, you have to call plt.show() explicitly to pop up figure window.

w = Loan_performance['Loan_Status'].value_counts()
w
#from here  calculate the percentage default and visualize the percentage default

values = [9628, 1964, 301, 243, 100, 60, 27]
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
labels = ['Current', 'Fully Paid', 'Charged Off', 'Late(31-120 days)', 'In Grace Period', 'Late(16-30 days)','Default']
explode = (0, 0, 0, 0, 0, 0, 0.6)
plt.pie(values, colors=colors, labels= labels, autopct='%1.1f%%', 
explode=explode,counterclock=False, shadow=True)
plt.title('Loan Default Rate')
plt.legend(labels,loc=2)
plt.show()

#define the frequency of borrowing by checking a histogram of the credit accounts
bf = Loan_performance['Credit_Accounts']
bf.head(10)
plt.hist(bf,5, histtype='step', align='mid', color='g', label='Loan Frequency')
plt.legend(loc=1)
plt.title('Customer Retention')
plt.show()
#most of the customers have multiple credit accounts opened or closed. 
#It gives opportunity to obtain credit report and verify customers. 
#However, having many accounts at once can pose a credit risk
