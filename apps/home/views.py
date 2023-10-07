from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import requests
from django.http import JsonResponse
import openai

from django.http import JsonResponse
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

openai.api_key = "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"

def chat(request):
    if request.method == 'POST':
        user_message = request.POST['message']
        bot_response = chatbot(user_message+"  here is the data about the company: youre an product manager with a product expo at 12:30 coming up and need to onboard")[0]['generated_text']
        return JsonResponse({'bot_response': bot_response})

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
