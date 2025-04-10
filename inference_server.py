# Inference Server

# install flask

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model("best_model.keras")

# Make the inference server
@app.route('/summary', methods=['GET'])
def model_summary():
    return jsonify({
        "name": "Damaged Building Classifier",
        "version": "v1.0",
        "description": "A model to classify images of buildings as damaged or not damaged.",
        "number_of_parameters": model.count_params(),
        "input_shape": model.input_shape,
        "output_shape": model.output_shape,
    })

@app.route('/inference', methods=['POST']) 
def inference():
   try:
       image_bytes= request.data
       image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
       image = image.resize((128, 128))  
       image_array = np.array(image) / 255.0  
       image_array = np.expand_dims(image_array, axis=0)  
       
       prediction = model.predict(image_array)[0][0]  
       label = "damage" if prediction > 0.5 else "no damage"
       return jsonify({"prediction": label})
   except Exception as e:
       return jsonify({"error": str(e)}), 400
   
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
       