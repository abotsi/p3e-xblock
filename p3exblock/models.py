
class Question(object):
	def __init__(self, text=""):
		self.interrogator_id = 0
		self.text = text
		self.grade = 0
		self.nb_eval = 0

class Response(object):
	def __init__(self):
		self.answerer_id = 0
		self.question_id = 0
		self.text = ""
		self.grade = 0