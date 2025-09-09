from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Berguegou Briana Yadjam',
        'class': 'PBP KI',
        'npm': '2506561555',
        'application_name': 'Crampons Etoiles'
    }

    return render(request, "main.html", context)
