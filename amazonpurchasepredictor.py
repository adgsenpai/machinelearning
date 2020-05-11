#ASHLIN DARIUS GOVINDASAMY
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
import tkinter as tk
#Amazon Inteview Question {Determine on these characteristics if the customer will buy or not buy on the Amazon market today}
#1. where they live,
#2. their income,
#3. their gender,
#4. their profession

#New York 1
#Boston 2
#New Jersey 3
#Texas 4

#any int value for income

#M,F 1,2
#E for Engineer, D developer, A arts and crafts, E Education, O Other



features = [[1,10000,1,1],[2,5000,2,4],[3,6000,1,4],[4,1000,2,3],[2,5000,2,4],[4,20000,1,1],[1,1000,2,3],[2,4000,1,2]]
labels = [1,1,1,0,0,1,0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

state = input("What state do you live in? ex NY [1],MA [2], NJ[3], TX [4]")
income = input("Income in USD $ per month ")
gender = input("Gender M(1) or F(2)? ")
profession = input("Profession? 1 for Engineer, 2 developer, 3 arts and crafts, 4 Education ")
tree.plot_tree(clf.fit(features,labels)) 
outcome = clf.predict([[state,income,gender,profession]])


if outcome==[1]:
 print('User will buy on Amazon Today')
else:
 print('User will not likely buy today')

tree.export_graphviz(clf)
