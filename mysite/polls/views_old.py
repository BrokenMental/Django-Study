from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# index() 뷰를 단축 기능으로 작성하기 위해 사용
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# 현재 폴더의 models.py의 메소드들 import
from .models import Question, Choice


def index(request):
    '''output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)'''

    '''template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))'''

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    '''response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)'''

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST : 키로 전송된 자료에 접근할수 있게 해주는 객체, 값은 항상 문자열
        # 만약 POST 자료에 'choice'가 없으면, request.POST['choice']는 KeyError가 발생
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # reverse() : 제어를 전달하기 원하는 뷰의 이름을, URL 패턴의 변수부분을 조합해서 해당 뷰를 가르킨다(예 : 'polls/3/results/' 문자열 반환).
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
