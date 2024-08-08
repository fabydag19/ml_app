from flask import Flask, render_template, request
from model import model_predictions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    result = None
    if request.method == 'POST':

        short_description = request.form.get('short_description')
        description = request.form.get('description')
        impact = int(request.form.get('impact'))
        urgency = int(request.form.get('urgency'))
        priority = int(request.form.get('priority'))
        
        result = model_predictions(short_description,description, impact, urgency, priority)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')