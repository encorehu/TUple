from django.shortcuts import render_to_response

def home(requst):
    return HttpResponse("Home")
    
def instructions(request):
    return HttpResponse("Instructions")
    
def exam(request):
    return HttpResponse("Exam")
    
def finished(request):
    return HttpResponse("Finished")

def closed(request):
    return render_to_response('closed.html')