import os
import webapp2
import jinja2
import codecs

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
        items = self.request.get_all('food')
        self.render("shopping_list.html", items=items)


class FizzBuzz(Handler):
    """docstring for FizzBuzz"""

    def get(self):
        self.render("fizzbuzz.html")


class Rot13(Handler):
    """docstring for Rot13"""

    def encode_to_rot13():
        pass

    def decode_from_rot13():
        pass

    def get(self):
        self.render("rot13.html")

    def post(self):
        input_text = self.request.get('text')
        output_text = codecs.encode(input_text, 'rot_13')
        self.render("rot13.html", output_text=output_text)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/fizzbuzz', FizzBuzz),
                               ('/rot13', Rot13)], debug=True)
