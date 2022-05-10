"Add ourself html page "


from django.http import HttpResponse

HTMLstring = """
 <h1> This is me </h1> """


def home(request):


    return(HTMLstring)




