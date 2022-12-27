from flask import Flask, jsonify, render_template, request, make_response
import transformers
import requests

app = Flask(__name__)


# recreate the dictionary 
# make the model run from URLs API instead
# create a python dictionary for your models d = {<key>: <value>, <key>: <value>, ..., <key>: <value>}
#dictOfModels = {"RoBERTa" : transformers.pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english"),
 #               "BERT" : transformers.pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment")}


dictOfModels = {"RoBERTa" : "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english",
                "BERT" : "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"}


# create a list of keys to use them in the select part of the html code
listOfKeys = []
for key in dictOfModels :
	listOfKeys.append(key)

#Write the inference function:
def get_prediction(message, model):
    API_TOKEN=xx
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload= f"inputs: {message}"
    results=requests.post(model, headers=headers, json=payload)
    results=results.json()[0]
    
    d={}
    for i in results:
        d[i["label"]]=i["score"]
        
    results={k:v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True) }
    
    # tuple 
    results = list(results.keys())[0], list(results.values())[0]    

    return results

# define a GET Method
@app.route('/', methods=['GET'])
def get():
    # in the select we will have each key of the list in option
    return render_template("home.html", len = len(listOfKeys), listOfKeys = listOfKeys)


# define a POST Method
@app.route('/', methods=['POST'])
def predict():
    message = request.form['message']
    # choice of the model
    results = get_prediction(message, dictOfModels[request.form.get("model_choice")])
    print(f'User selected model : {request.form.get("model_choice")}')
    my_prediction = f'The feeling of this text is {results[0]} with probability of {results[1]*100:.2f}%.'
    return render_template('result.html', text = f'{message}', prediction = my_prediction)


# Start the app
if __name__ == '__main__':
    # starting app
    app.run(debug=True,host='0.0.0.0')