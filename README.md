# Mood
A web application used to maintain your mental health by tracking your daily moods and activities.
<h2>Installation and Configuration of Beta-tested Software</h2>
<b>For users of the project.</b> Our web application need not be installed nor do configurations have to be done to the machine in order to use it. Mood is deployed through https://mood-192.herokuapp.com.

<b>For future developers of the project.</b> The web application can be cloned through the GitHub repository. The <b>master</b> branch is set to track a deployable project, with the database migrated from SQLite to PostgreSQL and required files for deployment present (Procfile and requirements.txt). We suggest to use the <b>test</b> branch in developing when using a local host. The software requires the use of a virtual environment with the following dependencies installed (which you can do so with python’s pip install):
<ul><li>Django==2.2</li>
<li>sqlparse==0.3.0</li>
<li>pyts==2018.9</li></ul>
Once accomplished, navigate to the root folder of the project and from the command line, execute<code>python manage.py runserver</code> and this will run Mood in a local host.
<p><p>We, the team, wish you the best of luck and we hope this project helps you help people.
