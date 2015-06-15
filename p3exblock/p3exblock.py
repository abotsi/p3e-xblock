"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

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

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def load_template(self, filename, data=None):
        """Handy helper for loading mako template."""
        mytemplate = Template(filename=APP_PATH+"templates/"+filename, input_encoding='utf-8')
        return mytemplate.render(data=data)
    

    def studio_view(self, context):
        pass

    def student_view(self, context=None):
        if (self.current_phase == 1):
            return self.phase1_view()
        elif (self.current_phase == 2):
            return self.phase2_view()
        elif (self.current_phase == 3):
            return self.phase3_view()
        elif (self.current_phase == 4):
            return self.finish_view()
        else:
            pass
            # return self.default_view()


    def phase1_view(self, context=None):
        """
        The first phase of the P3E
        """
        q1 = "Lorem ipsum dolor sit amet ?"
        q2 = "Praesent pulvinar in suscipit ?"
        q3 = "Mauris at risus in ipsum ?"

        html = self.load_template("phase1.html", [q1, q2, q3])
        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/p3exblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/p3exblock.js"))
        frag.initialize_js('P3eXBlock')
        return frag

    def phase2_view(self, context=None):
        """
        The second phase of the P3E
        """
        html = self.load_template("phase2.html", [])
        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/p3exblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/p3exblock.js"))
        frag.initialize_js('P3eXBlock')
        return frag

    def phase3_view(self, context=None):
        """
        The third phase of the P3E
        """

        paire1 = ("Lorem ipsum dolor sit amet ?", "Ok")
        paire2 = ("Praesent pulvinar in suscipit ?", "Ok")
        paire3 = ("Mauris at risus in ipsum ?", "Ok")
        paire4 = ("Glori et gritum sanctus ? ", "Ok")
        paire5 = ("Spius victum sacra tol ?", "Ok")
        paire6 = ("Rosa palaviar sactara bitum solo ?", "Ok")
        paire7 = ("Spartium calacam ravinar et rocasar ?", "Ok")
        paire8 = ("Incipit dosera magnanum et via  ?", "Ok")
        paire9 = ("Caviar Vodka par lo vomit  ? ", "Ok")

        html = self.load_template("phase3.html", [paire1, paire2, paire3, paire4, paire5, paire6, paire7, paire8, paire9])
        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/p3exblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/p3exblock.js"))
        frag.initialize_js('P3eXBlock')
        return frag

    def finish_view(self, context=None):
        """
        The end of P3E
        """
        html = self.load_template("finish.html", [])
        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/p3exblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/p3exblock.js"))
        frag.initialize_js('P3eXBlock')
        return frag

    @XBlock.json_handler
    def validate_phase1(self, data, suffix=''):
        """
        A handler to validate the phase 1
        """

        self.r1 = data['r1']
        self.r2 = data['r2']
        self.r3 = data['r3']
        self.questions.append(Question("coucou"))

        self.current_phase = 2

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
