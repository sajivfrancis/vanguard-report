### Dash Vanguard Report
###### multi-page, external_css, external_scripts        

This is a demo of the [Dash](https://plot.ly/products/dash/) interactive Python framework developed by [Plotly](https://plot.ly/).

Dash abstracts away all of the technologies and protocols required to build an interactive web-based application and is a simple and effective way to bind a user interface around your Python code.

To learn more check out our [documentation](https://dash.plot.ly).

##### About this repo:

**Procfile**   
This file specifies the commands that are executed by this application. For more information, see [here](https://devcenter.heroku.com/articles/procfile).

**requirements.txt**   
This file describes the python dependencies for this application.

**runtime.txt**   
This file declares the python runtime that the application is using. For more information, see [here](https://devcenter.heroku.com/articles/python-runtimes).

##### To run this app:

You can clone or download this repo:   
```
git clone <repo name>
```

Then cd into the repo:   
```
cd <repo name>
```

Now create and activate a virtualenv (noting the python runtime):   
On a mac:   
```
virutalenv -p <python version> venv
source venv/bin/activate
```

On a Windows:   
```
virutalenv -p <python version> venv
venv/Scripts/activate
```

Now that virtualenv is setup and active we can install the dependencies:   
```
pip install -r requirements.txt
```

Once the dependencies have been installed, run the application:
```
python app.py
```
