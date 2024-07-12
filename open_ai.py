from flask import Flask,request,jsonify
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-nXjUxK9biMBirC9tlBE5T3BlbkFJGJUJb57cgwMmnHHD8at7'

@app.route('/')
def home():
   return 'Welcome Home'
    
def get_response(prompt):
    completion = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0.5 
    )
    return completion['choices'][0]['text'].strip()

@app.route('/home',methods = ['GET','POST'])
def gpt():
    if request.method == 'POST':
        # Get JSON data from the request
        data = request.get_json()
        if data and 'prompt' in data:
            prompt = data['prompt']
            print(prompt)
            response = get_response(prompt)
            print (response)
            return 1
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'Invalid request'}), 400
    return 'Get method'
    

if __name__ == '__main__':
    app.run()