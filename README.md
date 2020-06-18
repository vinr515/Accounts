# Accounts
This lets you track your expenses. 
### Starting (in command prompt)
1. cd into the directory
2. set FLASK_APP=accountPage.py
3. python -m flask run
4. and go to [127.0.0.1:5000](http://127.0.0.1:5000)

The first page (/) lets you add new expenses to the database. It keeps track of the date, how you paid, the amount, the type of expense, and a short description. 

The view page (/view) shows you a pie chart of your expenses between two dates, broken down by category. It also shows the total amount spent in that time, and the number of purchases

### Screenshots

###### Main Page
![Image of Main Page](https://github.com/vinr515/Accounts/mainpage.png)
###### View Page
![Image of View Page](https://github.com/vinr515/Accounts/viewpage.png)
###### Chart Page
![Image of Chart Page](https://github.com/vinr515/Accounts/chartpage.png)