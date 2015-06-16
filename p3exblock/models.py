import json

class Question(object):
	def __init__(self, p_str_statement = "", p_str_answer = ""):
		self.writer_id = 0
		self.str_statement = p_str_statement
		self.str_answer = p_str_answer
		self.grade = 0
		self.nb_eval = 0

	@staticmethod
	def create_json(p_writer_id = 0, p_str_statement = "", p_str_answer = "", p_grade = 0, p_nb_eval = 0):
		json_var = {
			'writer_id': p_writer_id,
			'str_statement': p_str_statement,
			'str_answer': p_str_answer,
			'grade': p_grade,
			'nb_eval': p_nb_eval,
		}
		return json.dumps(json_var)

	def to_json(self):
		json_var = {
			'writer_id': self.writer_id,
			'str_statement': self.str_statement,
			'str_answer': self.str_answer,
			'grade': self.grade,
			'nb_eval': self.nb_eval,
		}
		return json.dumps(json_var)


class Response(object):
	def __init__(self):
		self.answerer_id = 0
		self.question_id = 0
		self.text = ""
		self.grade = 0

	@staticmethod
	def create_json(p_answerer_id = 0, p_question_id = 0, p_text = "", p_grade = 0):
		json_var = {
			'answerer_id': p_answerer_id,
			'question_id': p_question_id,
			'text': p_text,
			'grade': p_grade,
		}
		return json.dumps(json_var)
