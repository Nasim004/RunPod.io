import os
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.



def home(request):
    return render(request,'forms.html')



def image_generate(request):
    if request.method == "POST":
        try:

            api_key = request.POST.get('api')
            prompt = request.POST.get('prompt')
            height = int(request.POST.get('height'))
            width = int(request.POST.get('width'))
            image = int(request.POST.get('image'))

            payload = {
                "input": {
                    "prompt": prompt,
                    "height": height,
                    "width": width,
                    "num_outputs": image,
                    "num_inference_steps": 50,
                    "guidance_scale": 7.5,
                    "scheduler": "KLMS"
                }
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            url = "https://api.runpod.ai/v2/stable-diffusion-v2/runsync"

            response = requests.post(url, json=payload, headers=headers)   
            response_data = json.loads(response.text)
            if response.status_code == 200:
                execution_time = response_data.get('executionTime')
                status = response_data.get('status')
                images = [item['image'] for item in response_data['output']]
                result = {
                    'execution_time':execution_time,
                    'status':status,
                    'images':images

                }
                # return JsonResponse(json.dumps(result), safe=False)
            else:
                return JsonResponse({"success": False, "error": response.text})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
        return render(request,'forms.html',{'result':result})


        