from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

#필드의 이름(question_text, pub_date)은 데이터베이스의 컬럼명으로 사용
class Question(models.Model):
    question_text = models.CharField(max_length=200) #문자 필드
    pub_date = models.DateTimeField('date published') #날짜,시간 필드

    # __str__() 메소드는 객체의 표현을 대화식 프롬프트와 Django 관리 사이트에서 편하게 보기위해 사용
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #외래키 설정, CASCADE(종속) 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text