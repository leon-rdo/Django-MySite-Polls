from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Wellcome to this Django tutorial project! Type "/polls" after the server link to see the list of available polls.')