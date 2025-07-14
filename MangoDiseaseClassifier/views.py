# views.py

from django.shortcuts import render
import requests
from .forms import PredictionForm  # assuming you have this form defined

def index(request):
    result = None
    image_url = None

    if request.method == 'POST':
        form = PredictionForm(request.POST, request.FILES)
        if form.is_valid():
            model_choice = form.cleaned_data['model_choice']
            mode = form.cleaned_data['mode']
            leaf_image = form.cleaned_data['leaf_image']
            fruit_image = form.cleaned_data['fruit_image']

            files = {}
            if leaf_image:
                files['leaf_image'] = (leaf_image.name, leaf_image.read(), leaf_image.content_type)
            if fruit_image:
                files['fruit_image'] = (fruit_image.name, fruit_image.read(), fruit_image.content_type)

            data = {
                'model_choice': model_choice,
                'mode': mode
            }

            try:
                response = requests.post(
                    "https://mohsinramzan-mango-fusion.hf.space/predict/",
                    data=data,
                    files=files
                )

                if response.status_code == 200:
                    output = response.json()
                    result = f"{output['prediction']} with ({output['confidence']}% confidence)"
                    
                    # Determine whether to show 1 or 2 images
                    if mode == 'fusion':
                        # fusion has one combined image
                        image_url = [f"data:image/png;base64,{output['image_base64']}"]
                    else:
                        image_url = [f"data:image/png;base64,{output['image_base64']}"]

                else:
                    result = f"Error: {response.json().get('error', 'Unknown error')}"

            except Exception as e:
                result = f"Exception occurred: {str(e)}"

    else:
        form = PredictionForm()

    return render(request, 'MangoDiseaseClassifier/index.html', {
        'form': form,
        'result': result,
        'image_url': image_url
    })
