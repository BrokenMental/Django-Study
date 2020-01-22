from django.urls import path
from . import views # 현재 폴더의 views 파일을 연결

# polls 앱 말고도 여러 앱이 있을때 구분할 수 있도록 app_name 을 지정할 수 있다.
# templates 에서 url 을 '별칭'이 아닌 'app_name:별칭' 으로 지정하면 된다.
app_name = 'polls'

# path('url', import한 파일의 메소드, 별칭)
urlpatterns = [
    # ex) /polls/
    path('', views.index, name='index'),
    # ex) /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex) /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex) /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]