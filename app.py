from flask import Flask, render_template
from flask import request as flask_request
#Importing the required libraries
import requests, os, uuid, json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/en', methods=['GET'])
def index_en():
    return render_template('translate.html')
@app.route('/en', methods=['POST'])
def en_post():
    # Read the values from the form
    text = flask_request.form['text']
    
    # Load the values from .env
    key = "your Subscription Key"
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    location = "eastus"


    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate'
    constructed_url = endpoint + path

    params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['ja']
    }
    #params[to]=flask_request.form('language')
    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }


    body = [{
        'text': text
    }]
    # Make the call using post
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    # Retrieve the JSON response
    response = request.json()

    # Retrieve the translation
    response = response[0]['translations'][0]['text']


    # Call render template, passing the translated text,
    # # original text, and target language to the template
    return render_template(
        'results.html',
        response=response,
        text=text

    )
@app.route('/ja', methods=['GET'])
def index_ja():
    return render_template('translate.html')
@app.route('/ja', methods=['POST'])
def post_ja():
    # Read the values from the form
    text = flask_request.form['text']
    
    # Load the values from .env
    key = "56021f41d65c4246bdf51a20569d0cee"
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    location = "eastus"


    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate'
    constructed_url = endpoint + path

    params = {
    'api-version': '3.0',
    'from': 'ja',
    'to': ['en']
    }
    #params[to]=flask_request.form('language')
    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }


    body = [{
        'text': text
    }]
    # Make the call using post
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    # Retrieve the JSON response
    response = request.json()

    # Retrieve the translation
    response = response[0]['translations'][0]['text']


    # Call render template, passing the translated text,
    # # original text, and target language to the template
    return render_template(
        'results.html',
        response=response,
        text=text

    )
   
if __name__== "__main__":
    app.run(debug=False, host= '0.0.0.0')
