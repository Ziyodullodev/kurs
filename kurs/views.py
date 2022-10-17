from django.shortcuts import render, redirect
import requests
# from django.http.response import JsonResponse
# from rest_framework.views import APIView
# Create your views here.

def home(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        tel = request.POST['tel']
        email = request.POST['email']
        # if tel.index("+"):
        #     a = tel.split("+")
        #     if a[1].isnumeric():
        text = f"🎉Yangi odam ro'yxatdan o'tdi\n\n👤Ismi: <b>{name}</b>\n📞Telefon raqami: <b>+{tel}</b>\n📧Email: <b>{email}</b>"
        requests.get(f"https://api.telegram.org/bot5342966070:AAF7m176nTTcVD3a0JLwD5JoO2Mvf-JEqxg/sendmessage?chat_id=848796050&text={text}&parse_mode=html")
        return redirect('home')
        # return redirect('home')
    return render(request, 'home.html')

# def bot(request):
#     print(request)
#     # if request.method == "POST":
#     #     data = request.POST
#     return JsonResponse({'slaom':'alik'})
#     #     requests.get(f"https://api.telegram.org/bot5342966070:AAF7m176nTTcVD3a0JLwD5JoO2Mvf-JEqxg/sendmessage?chat_id=848796050&text={data}&parse_mode=html")
#     # return render(request, 'home.html')

# class Botpost(APIView):
#     def post(self, request):
#         data = request.POST
#         # data = {
#         #     'salom':"qale"
#         # }
#         data = list(data)
#         ok = requests.get(f"https://api.telegram.org/bot1513183791:AAEmAhS3eCFG3ahUE49ghoeKSeCx9xLfw8c/sendmessage?chat_id=848796050&text=salom{data}&parse_mode=html")
#         # print(ok.json())
#         return JsonResponse({'ok':'salom'})