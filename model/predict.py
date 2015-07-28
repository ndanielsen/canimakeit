#! usr/bin/env python -tt
"""
Prediction using trained models in a class format
"""

### MVP Imports
import us, random


class ModelBase(object):
	def __init__(self):
		self.DIR = None
		

	def load_model(self, dir):
		model_loaded_successfully = False
		if model_loaded_successfully: ### To refactor after MVP
			pass
		else:
			return None

	def model_predict(self, x, z):
		pass

	def test(self, x):
		''' assert test'''
		assert 2 + 2  == 4

class Budgeter(ModelBase):
	def __init__(self):
		self.DIR = 'budget/'


	def breakdown(self, user_salary): # 
		if self.load_model(self.DIR):
			return self.model_predict(user_salary)
		else:
			return self.mvp_breakdown(user_salary) 
	
	def mvp_breakdown(self, user_salary): ### develop catgories and budget precentages
		self.test
		
		budgets = {'max' : {'housing':user_salary*.15, 'grocery':None},
          'mean' : {'housing':user_salary*.33, 'grocery':None},
          'min' : {'housing':user_salary*.50, 'grocery':None}}

		return budgets

	def predict(self, user_salary):
		return self.breakdown(user_salary)

class Lodger(ModelBase):

	def __init__(self):
		self.DIR = 'lodge/'

	def housingchoices(self, housing, preferences=None):
		if self.load_model(self.DIR) != None:
			return self.model_predict(housing, preferences)
		else:
			return self.mvp_housing(housing, preferences)

	def mvp_housing(self, housing, preferences=None):
		
		lodging_options = {
		1: {'type':"1BR", "rent":1400, "neighborhood":"Columbia Heights", 'url':None},
		2: {'type':"2BR", "rent":1000, "neighborhood":"Anacostia", 'url':None},
		3: {'type':"Studio", "rent":1900, "neighborhood":"Georgetown", 'url':None},
		}

		return lodging_options

	def predict(self, housing, preferences=None):
		return self.housingchoices(housing, preferences)

class StateCluster(ModelBase):
	"""
	input: Salary, rent/own, household size   output: dictionary {state: num 0-4}
	"""
	def __init__(self):
		self.DIR = 'state/'


	def state_clusers(self, salary, preferences=None):
		if self.load_model(self.DIR) != None:
			return self.model_predict(salary, preferences)
		else:
			return self.mvp_state_clusers(salary, preferences)

	def mvp_state_clusers(self, salary, preferences=None):
		
		random.seed(1)
		lodging_options = {name.name: random.randint(1,5) for name in us.STATES}


		return lodging_options

	def predict(self, salary, preferences=None):
		return self.state_clusers(salary)



if __name__ == '__main__':
	lodge = Lodger()
	assert lodge.predict(1000, preferences="this")[1]['type'] == '1BR'
	print 'test lodger passed'

	budget = Budgeter()
	assert budget.predict(40000)['max']['housing'] == 6000.0
	print 'test budget passed'

	state = StateCluster()
	assert state.predict(1000)[u'District of Columbia'] == 1
	print 'test state passed'