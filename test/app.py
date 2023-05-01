import flask
app = flask.Flask(__name__)

def molly(text):
    return ' pensive'

def daniel(text):
    return ' blegh'

def chris(text):
    return ' hmm'

# Run input on model
@app.route('/model', methods=['POST'])
def model():
    try:
        # Get form data
        selected_model = flask.request.form.get('model')
        text = flask.request.form.get('text')

        # Run model
        if selected_model == 'molly':
            output = molly(text)
        elif selected_model == 'daniel':
            output = daniel(text)
        elif selected_model == 'chris':
            output = chris(text)
        else:
            output = 'Error: Invalid model'
        # Return output as JSON
        return flask.jsonify({'output': output})

    except Exception as e:
        return flask.jsonify({'error': str(e)})

# Show about page
@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/')
def hello():
    return flask.render_template('index.html')

app.run()