from django.http import HttpResponse
import logging

logging.basicConfig(filename="./log/log.log",
                    filemode='a', encoding="utf-8", level=logging.INFO,
                    format="{asctime} {format}: {levelname} {message}",
                    style='{')
logger = logging.getLogger(__name__)


def main(request):
    logger.info(request)
    with open("./business_card_app/navigation.txt", 'r', encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)


def about_me(request):
    logger.info(request)
    with open("./business_card_app/about_me_html.txt", 'r', encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)


def my_dreams(request):
    logger.info(request)
    with open("./business_card_app/dreams_html.txt", 'r', encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)
