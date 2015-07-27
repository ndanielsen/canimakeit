#! usr/bin/env python -tt
"""Recommendation Engine for Can I Make It 

Input: User supplied information such salary, household size and etc

Output: Returns nested dictionary of 3 budget types (min, mean, max) with a housing recommendation for each

By Nathan Danielsen
DDL4 Team
"""

from model.predict import Budgeter, Lodger


### TEST CASES 

user1 = 35,000
user2 = 70,000
user3 = 100,000

class Base(object):
	pass

class Recommend(Base):
	""" 
	Inherits from Base-Object

	Returns a nested dictionary of budgets each with housing recommendation
	"""
	def __init__(self):
		
		self.budgeting = Budgeter()
		self.lodging = Lodger() # returns three lodging options that fit 


	def recommend(self, user_salary):
		user_recommendations = {}

		budgets = self.budgeting.predict(user_salary)
		# print budgets
		for b in budgets.keys():
			# print b
			housing = budgets[b]['housing']
			lodging_options = self.lodging.predict(housing) # returns dictionary of recommendations
			budgets[b]['lodging'] = lodging_options

			# user_recommendations.update(bu)

		return budgets

		

if __name__ == '__main__':
	main = Recommend()
	print main.recommend(10000)['min']

	lodge = Lodger()
	assert lodge.predict(1000, preferences="this")[1]['type'] == '1BR'
	print 'test lodger passed'

	budget = Budgeter()
	assert budget.predict(40000)['max']['housing'] == 6000.0
	print 'test budget passed'
