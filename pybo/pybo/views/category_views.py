from django.shortcuts import render, get_object_or_404
from ..models import Question, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def question_in_category(request, category_number=None):
    categories=Category.object.all()#카테고리 모델을 모두 부른다.
    questions=Question.object.all() #카테고리 내부 요소를 모두 부른다. 필요에 따라 order를 사용하여 정렬하기도..
    if category_number: #카테고리 번호가 주어진다면..
        current_category=get_object_or_404(Category, category_number=category_number)
        questions=questions.object.filter(category=current_category) #다시 필터를 걸어 해당 카테고리 내부의 것들만 모은다.
    context = {'categories':categories,'current_category': current_category,
        'questions':questions}
    return render(request, '.html', context)