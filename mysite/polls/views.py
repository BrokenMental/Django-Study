from django.http import HttpResponse
from django.template import loader
# index() 뷰를 단축 기능으로 작성하기 위해 사용
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # return HttpResponse(template.render(context, request))

    # 템플릿의 context를 채워 표현한 결과를 HttpResponse 객체와 함께
    # 돌려주는 구문을 쉽게 표현하는 단축 기능
    # 이런식으로 작성하면 loader 와 HttpResponse를 import 하지 않아도 된다.
    # render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며,
    # context 사전형 객체를 세번째 선택적(optional) 인수로 받는다.
    # 인수로 지정된, context로 표현된 템플릿의 HttpResponse 객체가 반환된다.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 404예외 발생시키기
    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise HttpResponse("Question does not exist")
    return render(request, 'polls/detail. html', {'question': question})'''

    # 객체가 존재하지 않을때 get()를 사용하여 Http404 예외를 발생시키는 방법, get_object_or_404를 import 한다.
    # get_object_or_404() 함수는 Django 모델의 첫번째 인자로 받고,
    # 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘긴다.
    # 만약 객체가 존재하지 않을 경우, Http404 예외가 발생한다.
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})

    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



