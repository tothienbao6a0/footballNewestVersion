from django.shortcuts import redirect, render
from .models import *
# Create your views here.'
# views are essentially functiosn that returns an HTML template, HTTP responses nand others when called

def index(request):
    # this checks if user is logged in
    if 'user' not in request.session:
        return redirect('/login')
    user = User.objects.get(id=request.session['user'])
    return render(request, 'index.html', {'user': user})

def login(request):
    # if user is logged in --> dont go to login page
    if 'user' in request.session:
        return redirect('/')
    return render(request, 'login.html')

def register(request):
    # if user is logged in then dont go to register page
    if 'user' in request.session:
        return redirect('/')
    return render(request, 'register.html')

def createUser(request):
    if request.method == 'POST':
        # get data from form
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #this checks if passwords match
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        user = User.objects.filter(email=email)
        #this checks if email is already in use
        if len(user) > 0:
            return render(request, 'register.html', {'error': 'Email already in use'})
        user = User(first_name=fname, last_name=lname, email=email, password=password1)
        user.save()
        #save user in session
        request.session['user'] = user.id
        return redirect('/')

def logout(request):
    # remove user from session
    request.session.clear()
    return redirect('/login')

def checkUser(request):
    if request.method == 'POST':
        # get data from form
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        # check if email is already in use
        if len(user) > 0:
            user = user[0]
            # check if password is correct
            if user.password == password:
                request.session['user'] = user.id
                return redirect('/')
        
       
    return render(request, 'login.html', {'error': 'Invalid email or password'})


def lists(request):
    #this is checking if user is logged in
    if 'user' not in request.session:
        return redirect('/login')
    user = User.objects.get(id=request.session['user'])
    lists = List.objects.all()
    return render(request, 'lists.html', {'user': user,'lists':lists})


def createlist(request):
    if request.method == 'GET':
        lists = List.objects.filter(user=request.session['user'])
        return render(request, 'createlist.html', {'lists': lists})
    if request.method == 'POST':
        # get data from form
        name = request.POST['name']
        user = User.objects.get(id=request.session['user'])
        # create list
        list = List(list_name=name, user=user)
        list.save()
      
        return redirect('/createlist')

def add_question(request,list_id):
    list = List.objects.get(id=list_id)
    if request.method == 'GET':
        return render(request, 'add_question.html', {'list': list})

def createquestion(request): #this functions creates the questions (or start a new flash card) basically. 
    if request.method == 'POST':
        # get data from form
        name = request.POST['name']
        correct_phrase = request.POST['phrase']
        image = request.POST['image']
        list = List.objects.get(id=request.POST['list_id'])
        list.number_of_questions += 1
        list.save()
        # create question
        question = Question(question_text=name, list=list,correct_phrase=correct_phrase,image_path=image)
        question.save()
        return redirect('/createlist')

def delete_list(request,id):
    list = List.objects.get(id=id)
    list.delete()
    return redirect('/createlist')

def view(request,id):
    list = List.objects.get(id=id)
    questions = Question.objects.filter(list=list)
    return render(request, 'view.html', {'list': list, 'questions': questions})

def results(request):
    if 'user' not in request.session:
        return redirect('/login')
    else:
        # getting all scores
        scores = Score.objects.all()
        return render(request, 'results.html', {'scores': scores})

import random
def attempt(request,id):
    if 'user' not in request.session:
        return redirect('/login')
    else:
        # get list
        user = User.objects.get(id=request.session['user'])
        list = List.objects.get(id=id)
        # getting questions from that list
        questions = Question.objects.filter(list=list)
        options = Question.objects.all()
        questions_new = []
        for ques in questions:
            options_without_correct = options.exclude(correct_phrase=ques.correct_phrase)
            opts = [ques.correct_phrase,options_without_correct[random.randint(0,len(options_without_correct)-2)].correct_phrase,
                                    options_without_correct[random.randint(0,len(options_without_correct)-2)].correct_phrase,
                                    options_without_correct[random.randint(0,len(options_without_correct)-2)].correct_phrase]
            # randomizing options
            random.shuffle(opts) # this is so that the questions dont repeat, and the players can remember the plays more effectively. 
            question = {}
            question['question'] = ques
            question['options'] = opts
            questions_new.append(question)
        # shuffling the list of questions
        random.shuffle(questions_new)
        return render(request, 'attempt.html', {'user': user, 'list': list, 'questions': questions_new})


def submitquizresult(request):
    list_id = request.POST['list']
    list = List.objects.get(id=list_id)
    questions = Question.objects.filter(list=list)
    correct = 0
    for ques in questions:
        if request.POST['options-'+str(ques.id)] == ques.correct_phrase:
            correct += 1
    score = Score(user=User.objects.get(id=request.session['user']), list=list, score=correct)
    score.save()
    return redirect('/results')