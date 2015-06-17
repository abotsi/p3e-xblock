import json

class Question(object):
	def __init__(self, p_n_question_id = -1, p_n_writer_id = -1, p_s_text = "", p_lst_clue_answer = [], p_n_grade = -1, p_nb_of_grade = -1, p_lst_answer_to_evaluate = []):
		self.n_question_id = p_n_question_id
		self.n_writer_id = p_n_writer_id
		self.s_text = p_s_text
		self.lst_clue_answer = p_lst_clue_answer
		self.n_grade = p_n_grade
		self.nb_of_grade = p_nb_of_grade
		self.lst_answer_to_evaluate = p_lst_answer_to_evaluate

	def __str__(self):
		return self.__dict__.__str__()
	# @staticmethod
	# def create_json(p_n_writer_id = 0, p_s_text = "", p_lst_clue_answer = [], p_n_grade = 0, p_nb_of_grade = 0):
	# 	json_var = {
	# 		'n_writer_id': p_n_writer_id,
	# 		's_text': p_s_text,
	# 		'lst_clue_answer': p_lst_clue_answer,
	# 		'n_grade': p_n_grade,
	# 		'nb_of_grade': p_nb_of_grade,
	# 	}
	# 	return json.dumps(json_var)

	def to_json(self):
		json_var = {
			'n_question_id': self.n_question_id,
			'n_writer_id': self.n_writer_id,
			's_text': self.s_text,
			'lst_clue_answer': [],
			'n_grade': self.n_grade,
			'nb_of_grade': self.nb_of_grade,
			'lst_answer_to_evaluate': [],
		}
		for ans in self.lst_clue_answer:
			json_var['lst_clue_answer'].append(ans.to_json())
		for ans in self.lst_answer_to_evaluate:
			json_var['lst_answer_to_evaluate'].append(ans.to_json())
		return json.dumps(json_var)

	@staticmethod
	def from_json(json_string):
		json_var = json.loads(json_string)
		res = Question()
		res.question_id = json_var['n_question_id']
		res.n_writer_id = json_var['n_writer_id']
		res.s_text = json_var['s_text']
		res.lst_clue_answer = []
		res.n_grade = json_var['n_grade']
		res.nb_of_grade = json_var['nb_of_grade']
		res.lst_answer_to_evaluate = []
		
		for ans in json_var['lst_clue_answer']:
			res.lst_clue_answer.append(ans.from_json())
		for ans in json_var['lst_answer_to_evaluate']:
			res.lst_answer_to_evaluate.append(ans.from_json())
		return res


class Answer(object):
	def __init__(self, p_answer_id = -1, p_n_writer_id = -1, p_s_text = "", p_n_grade = -1, p_nb_of_grade = -1):
		self.answer_id = p_answer_id
		self.n_writer_id = p_n_writer_id
		self.s_text = p_s_text
		self.n_grade = p_n_grade
		self.nb_of_grade = p_nb_of_grade

	def __str__(self):
		return self.__dict__.__str__()

	def to_json(self):
		json_var = {
			'answer_id': self.answer_id,
			'n_writer_id': self.n_writer_id,
			's_text': self.s_text,
			'n_grade': self.n_grade,
			'nb_of_grade': self.nb_of_grade,
		}
		return json.dumps(json_var)

	@staticmethod
	def from_json(json_string):
		json_var = json.loads(json_string)
		res = Answer()
		res.answer_id = json_var['answer_id']
		res.n_writer_id = json_var['n_writer_id']
		res.s_text = json_var['s_text']
		res.n_grade = json_var['n_grade']
		res.nb_of_grade = json_var['nb_of_grade']
		return res
	
	# @staticmethod
	# def create_json(p_answer_id = 0, p_n_question_id = 0, p_s_text = "", p_n_grade = 0):
	# 	json_var = {
	# 		'answer_id': p_answer_id,
	# 		's_text': p_s_text,
	# 		'grade': p_n_grade,
	# 	}
	# 	return json.dumps(json_var)


if __name__ == '__main__':
	# a = Answer(p_s_text = "yo")
	# print "a :", a
	# print
	# q = Question(p_s_text = "bjr", p_lst_clue_answer = [a])
	# print "q :", q
	# print
	# q_json = q.to_json()
	# print "q_json :", q_json
	# print
	# q_py = Question.from_json(q_json)
	# print "q_py :", q_py
	# print


	a = {
		'answer_id': -1,
		'n_writer_id': -1,
		's_text': "yo.",
		'n_grade': -1,
		'nb_of_grade': -1,
	}
	print "a :", a
	print
	q = {
		'n_question_id': -1,
		'n_writer_id': -1,
		's_text': "bjr",
		'lst_clue_answer': [a],
		'n_grade': 4,
		'nb_of_grade': -1,
		'lst_answer_to_evaluate': [],
	}
	print "q :", q
	print
	q_encode = json.dumps(q)
	print "q_encode :", q_encode
	print
	q_decode = json.loads(q_encode)
	print "q_decode :", q_decode
	print
	print "q['n_grade'] == q_decode['n_grade'] : ", q['n_grade'] == q_decode['n_grade'] 