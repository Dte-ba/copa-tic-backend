from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    Home de copatic-backend

    <a href="/admin/">Admin</a>

    """)
