from flask import Flask
from flask import render_template
from flask import request, redirect
import sqlite3
import time

CASH_CARD = 'No Card (Cash)'
ERROR_CODE = {'account':[], 'view':[]}

#(year integer, month integer, date integer, pay text, card text, amount real,
#description text, category text)

app = Flask(__name__)

@app.route('/')
def account_page():
    if(len(ERROR_CODE['account']) == 0):
        return render_template("full.html")
    code = ERROR_CODE['account'][0]
    ERROR_CODE['account'].clear()
    return render_template("full.html", error=code)

@app.route('/newPurchase', methods=['POST'])
def new_purchase():
    ###Uses request to get the form answers for each field
    formNames = ['purchaseDate', 'type', 'cardName', 'amount', 'description', 'category']
    info = get_form_responses(formNames)
    errorCode = check_responses(info)
    if(errorCode):
        ERROR_CODE['account'].append(errorCode)
        return redirect('/')
    
    date, payType, cardName, amount = info[0], info[1], info[2], info[3]
    description, category = info[4], info[5]

    ###Gets the fields needed for the database from the form answers
    year, month, day = map(int, date.split('-'))
    amount = round(float(amount), 2)
    if(cardName == CASH_CARD):
        cardName = ''
        
    newRow = (year, month, day, payType, cardName, amount, description, category)
    insert_value(newRow)
    return redirect(request.referrer)

@app.route('/view')
def view_data():
    if(len(ERROR_CODE['view']) == 0): 
        return render_template("view.html")
    code = ERROR_CODE['view'][0]
    ERROR_CODE['view'].clear()
    return render_template("view.html", error=code)

@app.route('/chart', methods=['POST'])
def output_chart():
    if(request.form['startDate'] == '' or request.form['endDate'] == ''):
        ERROR_CODE['view'].append('One or both dates are not there')
        return redirect('/view')
    startDate = map(int, request.form['startDate'].split('-'))
    endDate = map(int, request.form['endDate'].split('-'))
    if(not(check_time(startDate, endDate))):
        ERROR_CODE['view'].append('Start Date is after the End Date')
        return redirect('/view')

    goodRows = get_purchases(request.form['startDate'], request.form['endDate'])
    return send_chart(goodRows)

@app.route('/sendchart', methods=['GET'])
def send_chart(goodRows):
    breakdown, totalSum = {}, 0
    for i in goodRows:
        if(i[-1] in breakdown):
            breakdown[i[-1]] += i[5]
        else:
            breakdown[i[-1]] = i[5]
        totalSum += i[5]

    allSum = round(totalSum, 2)
    finalBreakdown = []
    for i in breakdown:
        part = str(round((breakdown[i]/allSum)*100, 2))
        finalBreakdown.append((i, part, "{:0.2f}".format(breakdown[i])))
    totalSum = "{:0.2f}".format(totalSum)
        
    return render_template('chart.html', length=len(finalBreakdown),
                           chartData=finalBreakdown, total=totalSum,
                           numPurchases=len(goodRows))

def insert_value(value):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('''INSERT INTO expenses VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', value)
    conn.commit()
    conn.close()

def get_form_responses(formNames):
    info = ['']*len(formNames)
    for i in range(len(formNames)):
        info[i] = request.form[formNames[i]]
    return info

def check_responses(responses):
    if(responses[0] == ""):
        return "Wrong Date"
    
    nowTime = time.localtime()
    rowTime = (nowTime.tm_year, nowTime.tm_mon, nowTime.tm_mday)
    gDate = map(int, responses[0].split('-'))
    if(not(check_time(gDate, rowTime))):
        return "Date is After Today"
    if(responses[2] == ""):
        return "Wrong Card"

    if(not(check_float(responses[3]) and float(responses[3]) >= 0)):
        return "Wrong Amount"

    if(responses[-1] == ""):
        return "Wrong Category"
    return ""

def check_time(givenTime, newTime):
    gYear, gMonth, gDay = givenTime
    rYear, rMonth, rDay = newTime

    if(gYear > rYear):
        return False
    if(gYear < rYear):
        return True
    if(gMonth > rMonth):
        return False
    if(gMonth < rMonth):
        return True
    if(gDay > rDay):
        return False
    if(gDay < rDay):
        return True
    return True

def check_float(num):
    try:
        num = float(num)
        return True
    except ValueError:
        return False

def get_purchases(startDate, endDate):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    goodDates = []
    startDate = list(map(int, startDate.split('-')))
    endDate = list(map(int, endDate.split('-')))
    for i in c.execute('''SELECT * FROM expenses'''):
        timeTuple = (i[0], i[1], i[2])
        if(check_time(startDate, timeTuple) and check_time(timeTuple, endDate)):
            goodDates.append(i)

    conn.close()
    return goodDates

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")