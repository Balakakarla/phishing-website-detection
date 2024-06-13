from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
import joblib
from .features_extraction import FeatureExtraction

# Load the trained model
model = joblib.load('C:\\Users\\Bhavitha\\Desktop\\DeployModelProject\\DeployModel\\gradient_boosting_model.pkl')

def home(request):
    return render(request, "home.html")

def predict(request):
    print(request.method)
    if request.method == 'POST':
        url = request.POST.get('url')
        # Perform feature extraction
        obj = FeatureExtraction(url)
        features = obj.getFeaturesList()
        # Make prediction
        prediction = model.predict([features])[0]
        context={'ans':prediction,
                 'url' : url
                 }
        return render(request,'result.html',context)
    elif request.method == 'GET':
        # Handle GET request (optional)
        return HttpResponse("GET request received")

