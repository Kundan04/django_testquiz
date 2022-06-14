from django.http import request
from django.shortcuts import render
from .models import Questions
from django.core.mail import send_mail
from django.http import HttpResponse


to=['kunalsanwadkar@gmail.com']


# Create your views here.
def home(request):
    choices = Questions.CAT_CHOICES
    print(choices)
   
    '''if request.method =="POST":
        to = request.POST['emailID']
        print(to)'''
    return render(request,
        'quiz/home.html',
        {'choices':choices})

def questions(request , choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    return render(request,
        'quiz/questions.html',
        {'ques':ques})

def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        eff = (score/total)*100

        score1= str(score)
        eff1=str(eff)
    
        send_mail('Hello !',
        'Your response has been submitted, Your score is '+score1+' You are '+ eff1+ '% accurate',
        'trialminiproject@gmail.com',
        to,
        fail_silently=False
        )
    return render(request,
        'quiz/result.html',
        {'score':score,
        'eff':eff,
        'total':total})


def about(request):
    return render(request,
        'quiz/about.html')

def contact(request):
    return render(request,
        'quiz/contact.html')




