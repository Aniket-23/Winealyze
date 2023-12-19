from flask import Flask, render_template, redirect, request, url_for, flash
import numpy as np
#from tensorflow.keras.models import load_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)