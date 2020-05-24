from django.shortcuts import render
from django.template import loader
from . models import Flashcard, User, Topic, Subtopic, Question, Interview

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def flashcards(request):
    flash_term = Flashcard.objects.all() 
    if request.method == "POST":
        button = request.POST['button']
        is_front = int(request.POST['card_face'])
        selection = request.POST['selection']
        index = int(request.POST['old_index'])

        if button == "python":
            selection = "python"
            index = 0
        elif button == "sql":
            selection = "sql"
            index = 0
        
        if selection == "python":
            flash_term = Flashcard.python_flash.all()
        elif selection == "sql":
            flash_term = Flashcard.sql_flash.all()

        if button == "1":
            if index != 0:
                #previous
                is_front = 1
                index -= 1
        elif button == "2":
            #flip
            if is_front == 1:
                is_front = 0
            elif is_front == 0:
                is_front = 1
        elif button == "3":
            #next
            is_front = 1
            index += 1
        
        if is_front == 1:
            text = flash_term[index].Term
        else:
            text = flash_term[index].Definition
        
        return render(request, 'flashcards.html', {
            'index': index,
            'is_front': is_front,
            'selection': selection,
            'card_text': text,
            })
    else:
        index = 0
        is_front = 1
        selection = " "
        text = flash_term[index].Term
        return render(request, 'flashcards.html', {
            'index': index,
            'is_front': is_front,
            'selection': selection,
            'card_text': text,
        })

def questions(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        correct_ans = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_ans:
            my_ans = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_ans = "Incorrect! " + old_num_1 + " + " + old_num_2 + " is not " + answer + ", it is " + str(correct_ans)
            color = "danger"


        return render(request, 'questions.html', {
            'answer':answer,
            'my_ans': my_ans,
            'num_1':num_1,
            'num_2':num_2,
            'color':color,
            })
    return render(request, 'questions.html', {
        'num_1':num_1,
        'num_2':num_2,
    })

def interview(request):
    int_ques = Interview.objects.all() 
    if request.method == "POST":
        button = request.POST['button']
        is_front = int(request.POST['card_face'])
        index = int(request.POST['old_index'])

        if button == "1":
            if index != 0:
                #previous
                is_front = 1
                index -= 1
        elif button == "2":
            #flip
            if is_front == 1:
                is_front = 0
            elif is_front == 0:
                is_front = 1
        elif button == "3":
            #next
            is_front = 1
            index += 1
        
        if is_front == 1:
            text = int_ques[index].Question
        else:
            text = int_ques[index].Hint
        
        return render(request, 'interview.html', {
            'index': index,
            'is_front': is_front,
            'card_text': text,
            })
    else:
        index = 0
        is_front = 1
        text = int_ques[index].Question
        return render(request, 'interview.html', {
            'index': index,
            'is_front': is_front,
            'card_text': text,
        })