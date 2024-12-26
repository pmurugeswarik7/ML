import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the pre-trained model from a pickle file
with open('salary.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    input_text = request.form.get('t1')
    
    # Convert the input to the appropriate format for the model
    # (Adjust preprocessing as per your model's requirements)
    input_data = [float(input_text)]  # Example: single numeric input

    # Make a prediction
    prediction = model.predict([input_data])[0]  # Modify if model expects a different format

    # Render the result.html with the prediction
    return render_template('result.html', prediction=f"The predicted output is: {prediction}")

if __name__ == '__main__':
    app.run(debug=True)
