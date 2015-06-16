"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import logging

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, List
from xblock.fragment import Fragment

from mako.template import Template

from models import Question, Response

APP_PATH = "/home/abotsi/Documents/stage_p3e/fun/edxwork/p3exblock/p3exblock/"

class P3eXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    questions = List(
        default=[], scope=Scope.user_state_summary,
        help="The list of all questions",
    )
    responses = List(
        default=[], scope=Scope.user_state_summary,
        help="The list of all responses",
    )
    current_phase = Integer(
        default=1, scope=Scope.user_state,
        help="The phase currently running",
    )
    r1 = String(
        default="", scope=Scope.user_state,
        help="The first answer of the phase 1",
    )
    r2 = String(
        default="", scope=Scope.user_state,
        help="The second answer of the phase 1",
    )
    r3 = String(
        default="", scope=Scope.user_state,
        help="The third answer of the phase 1",
    )

    q = String(
        default="", scope=Scope.user_state,
        help="The question proposed by the student",
    )
    r = String(
        default="", scope=Scope.user_state,
        help="The answer proposed by the student",
    )
    
    def studio_view(self, context):
        pass

    def student_view(self, context=None):
        # print
        # print "Debut"
        # print self.questions
        # self.questions.append({'1': 'prout', '2':"pet"})
        # self.questions.append({'message': "coucou"})
        # print self.questions
        # print "Fin"
        # print

        data = []
        if (self.current_phase == 1):
            data = self.get_data_phase1()
        elif (self.current_phase == 3):
            data = self.get_data_phase3()

        return self.load_current_phase(data)


    def load_current_phase(self, data):
        """Handy helper for loading mako template."""
        f = APP_PATH+"templates/phase"+ str(self.current_phase) +".html"
        html = Template(filename=f, input_encoding='utf-8').render(data=data)

        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/p3exblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/p3exblock.js"))
        frag.initialize_js('P3eXBlock')
        return frag

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def get_data_phase1(self, context=None):
        """
        The first phase of the P3E
        """
        q1 = "Lorem ipsum dolor sit amet ?"
        q2 = "Praesent pulvinar in suscipit ?"
        q3 = "Mauris at risus in ipsum ?"

        return [q1, q2, q3]

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
        print "Appel au handler"

        self.r1 = data['r1']
        self.r2 = data['r2']
        self.r3 = data['r3']

        json_resp = Response.create_json(v_question_id = 1, v_text = data['r1'])
        print "json 1 created : ", json_resp
        self.responses.append(json_resp)
        print "rep added : ", self.responses
        json_resp = Response.create_json(v_question_id = 2, v_text = data['r2'])
        self.responses.append(json_resp)
        json_resp = Response.create_json(v_question_id = 3, v_text = data['r3'])
        self.responses.append(json_resp)

        self.current_phase = 2
        print "Fin du handler"

    @XBlock.json_handler
    def validate_phase2(self, data, suffix=''):
        """
        A handler to validate the phase 2
        """

        self.q = data['q']
        self.r = data['r']

        self.current_phase = 3

    @XBlock.json_handler
    def validate_phase3(self, data, suffix=''):
        """
        A handler to validate the phase 3
        """

        print "validate_phase3 called!"

        self.current_phase = 4

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
