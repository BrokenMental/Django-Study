from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
# generic.ListView : 개체 목록 표시, 기본적으로 <app name>/<model name>_list.html 템플릿 사용
# generic.DetailView : 특정 개체 유형에 대한 세부 정보 페이지 표시, 기본적으로 <app name>/<model name>_detail.html 템플릿 사용


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return the last five published question."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
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
