# from flask import Flask
# app = Flask(__name__)
# app.config['DEBUG'] = True

# # Note: We don't need to call run() since our application is embedded within
# # the App Engine WSGI application server.


# @app.route('/')
# def hello():
#     """Return a friendly HTTP greeting."""
#     return 'Hello World!'


# @app.errorhandler(404)
# def page_not_found(e):
#     """Return a custom 404 error."""
#     return 'Sorry, nothing at this URL.', 404
import webapp2
import cgi

form = """
<form method="post">
    What is your birthday?
    <br/>
    <label>Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <br/>
    <div style="color: red">%(error)s</div>
    <br/>
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    """docstring for MainPage"""

    def write_form(self, error="", month="", day="", year=""):
        def escape_html(str):
            return cgi.escape(str, quote=True)

        self.response.out.write(form % {"month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year),
                                        "error": error})

    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
        months_abbvs = dict((m[:3].lower(), m) for m in months)

        def valid_day(day):
            if (day and day.isdigit()):
                int_day = int(day)
                if (int_day > 0 and int_day <= 31):
                    return int_day

        def valid_year(year):
            if (year and year.isdigit()):
                int_year = int(year)
                if (int_year > 1900 and int_year < 2020):
                    return int_year

        def valid_month(month):
            if month:
                if month.capitalize() in months:
                    short_month = month[:3].lower()
                    return months_abbvs.get(short_month)

        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        # Validate the values that the user entered
        validated_month = valid_month(self.request.get('month'))
        validated_day = valid_day(self.request.get('day'))
        validated_year = valid_year(self.request.get('year'))

        if not (validated_month and validated_day and validated_year):
            self.write_form("Sorry, the value you entered is not accepted.",
                            user_month,
                            user_day,
                            user_year)
        else:
            # self.response.headers['Content-Type'] = 'text/plain'
            self.redirect("/thanks")
            # self.response.out.write("Thanks! That is totally valid day!")


class ThanksHandler(webapp2.RequestHandler):
    """docstring for ThanksHandler"""

    def get(self):
        self.response.out.write("Thanks! That is totally valid day!")


app = webapp2.WSGIApplication(
    [('/', MainPage), ('/thanks', ThanksHandler)], debug=True)
