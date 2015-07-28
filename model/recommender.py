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
		
		self.budgeting = Budgeter()
		self.lodging = Lodger() # returns three lodging options that fit 
		self.statecluster = StateCluster()

	def recommend(self, user_salary, rent=None, own=None, household_size=None ):
		user_recommendations = {"timestamp": datetime.datetime.now().isoformat(' ')}		

		budgets = self.budgeting.predict(user_salary)
		
		for b in budgets.keys():
			# print b
			housing = budgets[b]['housing']
			budgets[b]['lodging'] = self.lodging.predict(housing) # returns dictionary of recommendations
		
		user_recommendations["budgeting"] = budgets	
		user_recommendations['statecluster'] = self.statecluster.predict(user_salary)

		return user_recommendations

		

if __name__ == '__main__':
	main = Recommender()
	print main.recommend(10000)

	lodge = Lodger()
	assert lodge.predict(1000, preferences="this")[1]['type'] == '1BR'
	print 'test lodger passed'

	budget = Budgeter()
	assert budget.predict(40000)['max']['housing'] == 6000.0
	print 'test budget passed'

	state = StateCluster()
	assert state.predict(1000)[u'District of Columbia'] == 1
	print 'test state passed'
