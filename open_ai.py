from flask import Flask,request,jsonify
from openai import OpenAI
from dotenv import load_dotenv  
import os

app = Flask(__name__)
load_dotenv()
if 'OPENAI_API_KEY' in os.environ:
    print("Environment variable is set.")
    #print(f"API Key: {os.environ['OPENAI_API_KEY']}")
else:
    raise EnvironmentError("Please set the OPENAI_API_KEY environment variable")

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']
)

@app.route('/')
def home():
   return 'Welcome Home'
    
    
def get_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    return completion.choices[0].message.content

@app.route('/home',methods = ['GET','POST'])
def gpt():
    if request.method == 'POST':

        data = request.get_json()
        if data and 'prompt' in data:
            prompt = data['prompt']
            print(prompt)
            response = str(get_response(prompt))
            print (response)
            
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'Invalid request'}), 400
    return 'Get method'
    

if __name__ == '__main__':
    app.run()