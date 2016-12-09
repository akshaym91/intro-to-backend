import os
import webapp2
import jinja2
import codecs
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
    """docstring for Handler"""

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    """docstring for MainPage"""

    def get(self):
        self.render("backend.html")


class FizzBuzz(Handler):
    """docstring for FizzBuzz"""

    def get(self):
        self.render("fizzbuzz.html")


class TodoList(Handler):
    """docstring for TodoList"""

    def get(self):
        items = self.request.get_all('food')
        self.render("shopping_list.html", items=items)


class SignUp(Handler):
    """docstring for SignUp"""

    def get(self):
        errors = {"username_error": "",
                  "password_error": "",
                  "verify_error": "",
                  "email_error": "",
                  "user_username": "",
                  "user_email": ""}
        self.render("signup.html", errors=errors)

    def post(self):

        def validate_username(username):
            USERNAME_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
            return USERNAME_RE.match(username)

        def validate_email(email):
            EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
            if(EMAIL_RE.match(email) or email == ""):
                return True
            return EMAIL_RE.match(email)

        def validate_password(password):
            PASSWORD_RE = re.compile(r"^.{3,20}$")
            return PASSWORD_RE.match(password)

        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verifypassword = self.request.get('verify')
        user_email = self.request.get('email')

        test_username = validate_username(user_username)
        test_password = (validate_password(user_password) and
                         (user_password == user_verifypassword))
        test_email = validate_email(user_email)
        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""
        if (not test_username):
            username_error = "Invalid Username."

        if (not validate_password(user_password)):
            password_error = "Invalid Password."

        if (not (user_password == user_verifypassword)):
            verify_error = "Password mismatch."

        if (not test_email):
            email_error = "Invalid Email."

        if not (test_username and
                test_password and
                test_email and
                (user_password == user_verifypassword)):
            self.render("signup.html",
                        errors={"username_error": username_error,
                                "password_error": password_error,
                                "verify_error": verify_error,
                                "email_error": email_error,
                                "user_username": user_username,
                                "user_email": user_email})
        else:
            self.render("thanks.html", user_username=user_username)


class Rot13(Handler):
    """docstring for Rot13"""

    def get(self):
        self.render("rot13.html")

    def post(self):
        input_text = self.request.get('text')
        output_text = codecs.encode(input_text, 'rot_13')
        self.render("rot13.html", output_text=output_text)


class ThanksHandler(Handler):
    """docstring for ThanksHandler"""

    def get(self):
        self.render("thanks.html")

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/fizzbuzz', FizzBuzz),
                               ('/todolist', TodoList),
                               ('/signup', SignUp),
                               ('/rot13', Rot13),
                               ('/thanks', ThanksHandler)], debug=True)
