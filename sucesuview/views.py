from django.shortcuts import render

def post_list(request):
    return render(request, 'sucesu_templates/index.html', {})
