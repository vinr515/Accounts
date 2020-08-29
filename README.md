# Accounts
This lets you track your expenses. 
### Starting (flask)
1. `cd Accounts`
2. `export FLASK_APP=app/accountPage.py`
3. `python -m flask run`
4. and go to [127.0.0.1:5000](http://127.0.0.1:5000)

### Starting (python)
1. `cd Accounts`
2. `python app/accountPage.py`
3. and go to [0.0.0.0:5000](http://0.0.0.0:5000)

### Starting (docker)
1. `cd Accounts`
2. `docker build . -t accounts`
3. `docker run -itdp 5000:5000 --name accounts accounts`
4. and go to [0.0.0.0:5000](http://0.0.0.0:5000)

The first page lets you add new expenses to the database. It keeps track of the date, how you paid, the amount, the type of expense, and a short description. 

The view page (`url/view`) shows you a pie chart of your expenses between two dates, broken down by category. It also shows the total amount spent in that time, and the number of purchases

### Screenshots

###### Main Page
![Image of Main Page](https://github.com/vinr515/Accounts/blob/master/mainpage.PNG)
###### View Page
![Image of View Page](https://github.com/vinr515/Accounts/blob/master/viewpage.PNG)
###### Chart Page
![Image of Chart Page](https://github.com/vinr515/Accounts/blob/master/chartpage.PNG)