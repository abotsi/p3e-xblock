# coding: utf-8
"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import logging
from random import sample, shuffle

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, List, Dict
from xblock.fragment import Fragment

from mako.template import Template

from models import Question, Answer

APP_PATH = "/home/abotsi/Documents/stage_p3e/fun/edxwork/p3exblock/p3exblock/"
# APP_PATH = "/home/pilou/xblock-sdk/p3exblock/p3exblock/"

class P3eXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    dict_questions = Dict(
        default={}, scope=Scope.user_state_summary,
        help="The list of all questions",
    )
    max_id_question = Integer(
        default=0, scope=Scope.user_state,
        help="The phase currently running",
    )
    current_phase = Integer(
        default=1, scope=Scope.user_state,
        help="The phase currently running",
    )
    phase1_question_indexes = List(
        default=[], scope=Scope.user_state,
        help="The ids of the 3 questions this student answered in phase 1",
    )
    phase2_question_index = Integer(
        default=[], scope=Scope.user_state,
        help="The id of the question this student asked in phase 1",
    )
    phase3_answer_indexes = List(
        default=[], scope=Scope.user_state,
        help="The ids of the 9 answers this student corrected in phase 1",
    )
    
    def studio_view(self, context):
        pass

    def student_view(self, context=None):
        if len(self.dict_questions)<10:
            for i in range(10):
                self.add_question("question bidon n"+str(i), "reponse bidon n"+str(i), p_is_prof=True)
                self.add_question("question eleve bidon n"+str(i), "reponse bidon n"+str(i))

        data = []
        if (self.current_phase == 1):
            data = self.get_data_phase1()
        elif (self.current_phase == 3):
            data = self.get_data_phase3()

        return self.load_current_phase(data)


    def load_current_phase(self, p_data):
        """Loading the whole XBlock fragment"""

        frag = Fragment(self.get_current_html(p_data))
        frag.add_css(self.resource_string("static/css/p3exblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/p3exblock.js"))
        frag.initialize_js('P3eXBlock')
        return frag

    def get_current_html(self, p_data=[]):
        """Handy helper for loading mako template."""
        f = APP_PATH+"templates/phase"+ str(self.current_phase) +".html"
        # f = self.runtime.local_resource_url(self, "public/templates/phase"+ str(self.current_phase) +".html")
        html = Template(filename=f, input_encoding='utf-8').render(data=p_data)
        return html

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def get_data_phase1(self, context=None):
        """
        Selecting 3 random questions for the first phase
        """
        
        lst_txt = []        
        self.phase1_question_indexes = []

        # on prend au hasard des indexes de questions profs
        self.phase1_question_indexes = sample(self.get_prof_questions(), 2)
        # puis on ajoute une question étudiant
        self.phase1_question_indexes.append(sample(self.get_student_questions(), 1)[0])
        #on melange les questions pour que celle de l'etudiant ne soit pas toujours a la fin
        shuffle(self.phase1_question_indexes)

        print
        print "Selected questions : ", self.phase1_question_indexes
        print

        # on prend le texte des questions profs que l'on vient d'ajouter
        for i in self.phase1_question_indexes:
            lst_txt.append(self.dict_questions[i]['s_text'])

        return lst_txt


    def get_data_phase3(self, context=None):
        """
        The third phase of the P3E
        """

        triplet1 = ("Lorem ipsum dolor sit amet ?", "Ok", "je suis la puissance")
        triplet2 = ("Praesent pulvinar in suscipit ?", "Ok", "je suis la puissance")
        triplet3 = ("Mauris at risus in ipsum ?", "Ok","je suis la puissance")
        triplet4 = ("Glori et gritum sanctus ? ", "Ok","je suis la puissance")
        triplet5 = ("Spius victum sacra tol ?", "Ok", "je suis la puissance")
        triplet6 = ("Rosa palaviar sactara bitum solo ?", "Ok", "je suis la puissance")
        triplet7 = ("Spartium calacam ravinar et rocasar ?", "Ok", "je suis la puissance")
        triplet8 = ("Incipit dosera magnanum et via  ?", "Ok", "je suis la puissance")
        triplet9 = ("Caviar Vodka par lo vomit  ? ", "Ok", "je suis la puissance")

        return [triplet1, triplet2, triplet3, triplet4, triplet5, triplet6, triplet7, triplet8, triplet9]

    @XBlock.json_handler
    def validate_phase1(self, data, suffix=''):
        """
        A handler to validate the phase 1
        """
        print 
        print "Appel au handler 1"
        print "data : ", data

        for i in range(3):
            question_index = self.phase1_question_indexes[i]
            answer = data[i]['answer']
            grade = int(data[i]['question_grade'])

            # Pour ne pas perdre de precision a cause de la moyenne,
            # on sauvegarde separement le total de evaluations et le nombre d'evaluation 
            self.dict_questions[question_index]['nb_of_grade']+=1
            self.dict_questions[question_index]['n_grade'] += grade
            self.add_answer_to_question(question_index, answer)

        self.current_phase = 2
        print "Fin du handler"

        return {'phase_number':self.current_phase, 'content':self.get_current_html()}

    @XBlock.json_handler
    def validate_phase2(self, data, suffix=''):
        """
        A handler to validate the phase 2
        """

        print
        print "Appel au handler 2"
        self.add_question(data['question'], data['answer'])

        self.current_phase = 3
        print "Fin handler"

        return {'phase_number':self.current_phase, 'content':self.get_current_html()}

    @XBlock.json_handler
    def validate_phase3(self, data, suffix=''):
        """
        A handler to validate the phase 3
        """

        print "validate_phase3 called!"

        self.current_phase = 4

    def add_question(self, p_question_txt, p_answer_txt, p_is_prof=False):
        self.max_id_question+=1
        res = {
            # 'n_question_id': -42, --> pas besoin a cause du self.max_id_question
            'n_writer_id': -1,
            'is_prof': p_is_prof,
            's_text': p_question_txt,
            'lst_clue_answer': [{
                'answer_id': -42,
                'n_writer_id': -1,
                's_text': p_answer_txt,
                'n_grade': 0,
                'nb_of_grade': 0,
            }],
            'n_grade': 0,
            'nb_of_grade': 0,
            'lst_answer_to_evaluate': [],
        }
        # la cle d'un field.Dict passe au format unicode
        self.dict_questions[unicode(self.max_id_question)] = res

    def add_answer_to_question(self, id_question, p_s_text):
        self.dict_questions[id_question]['lst_answer_to_evaluate'].append({
            'answer_id': -42,
            'n_writer_id': -1,
            's_text': p_s_text,
            'n_grade': 0,
            'nb_of_grade': 0,
        })

    def get_prof_questions(self):
        """Return a subset of all questions written by a professor"""
        return dict(filter(lambda k: k[1]['is_prof']==True, self.dict_questions.items()))

    def get_student_questions(self):
        """Return the subset of questions written by students"""
        return dict(filter(lambda k: k[1]['is_prof']==False, self.dict_questions.items()))

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("P3eXBlock",
             """<p3exblock/>
             """),
        ]

# d = {11: {'f': 'orange', 'is_prof': 'False'}, 1: {'f': 'pomme', 'is_prof': 'True'}, 3: {'f': 'orange', 'is_prof': 'False'}, 7: {'f': 'bannane', 'is_prof': 'True'}}
# sous_ensemble =  [v for k,v in d2.iteritems() if v['f']=='orange']
# dict(filter(lambda k: k[1]['is_prof']=='True', d.items()))