#! usr/bin/env python -tt
"""Recommendation Engine for Can I Make It 

Input: User supplied information such salary, household size and etc

Output: Returns nested dictionary of 3 budget types (min, mean, max) with a housing recommendation for each

By Nathan Danielsen
DDL4 Team
"""
import datetime

from predict import Budgeter, Lodger, StateCluster

class Base(object):
	pass

class Recommender(Base):
	""" 
	Inherits from Base-Object

	Returns a nested dictionary of budgets each with housing recommendation
	"""
	def __init__(self):
		
		self.budgeting = Budgeter() # predict() returns max, mean, min budgets 
		self.lodging = Lodger() # predict() returns three lodging options that housing prediction 
		self.statecluster = StateCluster() # predict() returns list of states with clustering 1-5

	def recommend(self, user_salary, rent=None, own=None, household_size=None ):

		def xstr(s):
			return 0 if s is None else s 

		def xsize(s):	
			return 1 if s is None else s 


		# user_salary = xstr(user_salary)
		rent = xstr(rent)
		own = xstr(own)
		household_size = xsize(household_size)


		user_recommendations = {"timestamp": datetime.datetime.now().isoformat(' ')}		

		budgets = self.budgeting.predict(user_salary)
		
		for b in budgets.keys():
			# print b
			housing = budgets[b]['housing']
			budgets[b]['lodging'] = self.lodging.predict(housing) # returns dictionary of recommendations
		
		user_recommendations["budgeting"] = budgets	
		user_recommendations['state_cluster'] = self.statecluster.predict(salary=user_salary, family_size=household_size, own=own, rent=rent )

		return user_recommendations

		

if __name__ == '__main__':
	import pprint
	

	main = Recommender()
	pprint.pprint(main.recommend(40000))

	lodge = Lodger()
	assert lodge.predict(1000, preferences="this")[1]['type'] == '1BR'
	print 'test lodger passed'

	budget = Budgeter()
	assert budget.predict(40000)['max']['housing'] == 6000.0
	print 'test budget passed'

	state = StateCluster()
	print 'test state passed'
	assert state.predict(salary=70000, family_size=1, own=0, rent=1)['DC']['fillKey'] == 4

