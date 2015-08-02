#! usr/bin/env python -tt
"""
Prediction using trained models in a class format
"""

### MVP Imports
import us, random
import pickle
from sklearn.linear_model import LogisticRegression

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


	def state_clusters(self, salary=None, family_size=None, own=None, rent=None):
		if self.load_model(self.DIR) != None:
			return self.model_predict(salary, preferences)
		else:
			return self.mvp_state_clusters(salary, preferences)

	def mvp_state_clusters(self, salary=None, family_size=None, own=None, rent=None):
		
		random.seed(salary)
		lodging_options = {name.abbr:{'fillKey':random.randint(1,5)} for name in us.STATES}

		return lodging_options


	def log_clusters(self, salary=None, family_size=None, own=None, rent=None):

		# pickle_file = 'state/mvp_2015_0801.pickle'
		
		def pickle_loader(pickle_file):
			with open(pickle_file, "r") as fp: 	#Load model from file
				pred = pickle.load(fp)
				return pred

		def mvp_state_clusters_v2(salary, family_size, own, rent):
			request = [salary, family_size, own, rent]
			state_matrix = {}
			states = [u'AK', u'AL', u'AZ', u'CA', u'CO', u'CT', u'DC', u'DE', u'FL', u'GA', u'HI', u'ID', u'IL', u'IN', u'KS', u'KY', u'LA', u'MA', u'MD', u'ME', u'MI', u'MN', u'MO', u'NE', u'NH', u'NJ', u'NV', u'NY', u'OH', u'OR', u'PA', u'SC', u'TN', u'TX', u'UT', u'VA', u'WA', u'WI', u'WV']
			len_states = len(states)
			for index, state in enumerate(states):
				flag = [0 for n in states]
				flag[index] = 1
				combine = request + flag
				state_matrix.update({state: {'fillKey':int(logreg_production.predict(combine))}})
			return state_matrix

		logreg_production = pickle_loader('state/mvp_2015_0801.pickle')

		return mvp_state_clusters_v2(salary, family_size, own, rent)





	def predict(self, salary=None, family_size=None, own=None, rent=None):
		return self.log_clusters(salary=salary, family_size=family_size, own=own, rent=rent)



if __name__ == '__main__':
	lodge = Lodger()
	assert lodge.predict(1000, preferences="this")[1]['type'] == '1BR'
	print 'test lodger passed'

	budget = Budgeter()
	assert budget.predict(40000)['max']['housing'] == 6000.0
	print 'test budget passed'

	# state = StateCluster()
	# assert state.predict(10000)[u'DC']['fillKey'] == 5 
	# print 'test state passed'


	state = StateCluster()
	print state.predict(salary=70000, family_size=1, own=0, rent=1)