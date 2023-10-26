from django.http import HttpResponse


def main(request):
    with open("./business_card_app/navigation.txt", 'r', encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)


def about_me(request):
    with open("./business_card_app/about_me_html.txt", 'r', encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)


def my_dreams(request):
    with open("./business_card_app/dreams_html.txt", 'r', encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)
