from django.http import HttpResponse


def main(request):
    html = """
    <!doctype html>
<html lang="en">
<head>
  <title>HTML Document Template</title>
  <style>
    h1 {
      ;
      font-family: fantasy;
      color: #FF4500;
    }

    body{

            background-image: url("https://i.pinimg.com/originals/45/69/aa/4569aa6967159dad5b48c7bbd5ecf72c.jpg");
            background-repeat: repeat-x;
            background-size: 100%;
}
p{
font-family: cursive;
color: #9932CC;
-webkit-text-stroke: 0.1px white;

}
  </style>
</head>
<body background-image: red>
<h1> Навигация </h1>
  <p>1. При подключении по адресу 
   http://192.168.0.7:8000/business/main/ - Вы попадаете на страницу с навигацией. </p>
  <p>2. about/  - откроеться стриница данных обо мне.  </p>
  <p>3. dreams/ - страница целей. </p>
</body>
</html>
    """
    return HttpResponse(html)


def about_me(request):
    with open("./business_card_app/about_me_html.txt", 'r', encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)


def my_dreams(request):
    pass
