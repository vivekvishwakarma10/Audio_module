from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def display():
    
    return render_template('indexaudio.html')

@app.route('/submit',methods = ['POST', 'GET'])
def generate_action():
    query01 = ""
    link = ""
    if request.method == 'POST':
        query01 = request.form['query']
    if "google" in query01:
        link = "google.com"
    elif "youtube" in query01:
        link = "youtube.com"
    # return str(res)
    days_ago = ""

    if 'live event' in query01:
        eventType = ""
        # speak("Please wait trying to display live alert event")
        link = f"localhost:4101/live"
        # print(link)

    if 'view logs' in query01:
        eventType = ""
        # speak("Please wait trying to display View logs event")
        # link = f"http://localhost:5000/api/v1/analytics/logs?EventType=&from_date=2023-04-01T17:01&to_date=2023-04-10T17:01"
        link = f"localhost:4101/search"
        # print(link)
    if 'view challan' in query01:
        eventType = ""
        # speak("Please wait trying to display live alert event")
        link = f"localhost:4101/challan"
        # print(link)        

    if 'exit' in query01:
        # speak('Thanks for using ITMS audio system')
        exit()

    return redirect('http://' +str(link))

if __name__=='__main__':
    app.run(debug= True, port = 5011)
