## Python Backend course on Udacity

###Assignment and Tasks

A complete directory of the Tasks and assignments for the [Intro to Backend](https://www.udacity.com/course/intro-to-backend--ud171) course on Udacity.
Taken as part of the [Fullstack Web Development](https://www.udacity.com/degrees/full-stack-web-developer-nanodegree--nd004).

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   https://github.com/akshaym91/intro-to-backend.git
   ```
3. Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project directory.

   ```
   cd intor-to-backend
   pip install -r requirements.txt -t lib
   ```
4. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

How to use the google cloud platform:
```
$ dev_appserver.py $PWD
```
$ gcloud app deploy app.yaml --project <project-name>
```

### Relational Databases and Datastore
To add persistence to your models, use
[NDB](https://developers.google.com/appengine/docs/python/ndb/) for
scale.  Consider
[CloudSQL](https://developers.google.com/appengine/docs/python/cloud-sql)
if you need a relational database.

### Installing Libraries
See the [Third party
libraries](https://developers.google.com/appengine/docs/python/tools/libraries27)
page for libraries that are already included in the SDK.  To include SDK
libraries, add them in your app.yaml file. Other than libraries included in
the SDK, only pure python libraries may be added to an App Engine project.

## Contributing changes
See [CONTRIB.md](CONTRIB.md)

## Licensing
See [LICENSE](LICENSE)

## Author
Akshay Menon
