from django.shortcuts import render, redirect
import requests
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