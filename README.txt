The app has been hosted at  https://protected-woodland-97549.herokuapp.com/.
You shall head to the same any time so as to access the app.
In case the app is not awake for some reasons or out of your personal interest if you want to run it locally, the following steps need to be followed :

1.Check if python is installed [For windows only as mac and linux have python installed]:
   a.Open a command prompt window (press Windows+R, type in cmd, and hit enter).
   b.Type python. If you get 'python is not recognized as an internal or external command' either you have no python installed or the PATH variable is not set. Add python and python/scripts and check again
2.Setting virtualenv [optional] :
    It is advisable to install dependencies for each project in a virtual environments so as prevent them from messing up with other version.Please follow the tutorial linked below for setting up the same
    http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/
	https://virtualenv.pypa.io/en/stable/
3. Once everything is up and running, type :
   1.go to the apps root directory
   2. python setup.py install 
   3. pip -r requirements.txt
 4.The app would start running in the local host : 127.0.0.1
 5. You will be directed to the home page that displays hello world.
 6.Every page has a header which hyperlinks to each of the tasks assigned. This can be used as the primary means of navigation
 
 Home -> hello world [task 1]
 Authors -> JSON parsing of author's posts
 Set Cookie -> sets cookies if not already set.
 Get cookie -> Retrieve the cookies set
 Deny ->  /deny endpoint
 Forms -> gets an input and posts it to another endpoint
 Image -> Renders an image.
 Feel free to exlore!!
   
   
   https://protected-woodland-97549.herokuapp.com/
