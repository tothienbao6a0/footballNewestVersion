from django.db import models
#the models file is essentially where all the classes are created (classes are objects like in Java)
#they are all created in the same file
#self is like in
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self): #this is like the getInstance() method in Frc, it gets the instance object
        return self.first_name + " " + self.last_name
        #define the model for user 


class List(models.Model):
    list_name = models.CharField(max_length=255) 
    user = models.ForeignKey(User, related_name="lists", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #used for logging the time that the user signed up
    number_of_questions = models.IntegerField(default=0) #used to collect the number of questions that are collected by the user

    def __str__(self):
        return self.list_name
        #the login module for the user --> collect these datas

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    list = models.ForeignKey(List, related_name="questions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    correct_phrase = models.CharField(max_length=500)
    image_path = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.question_text
    #questions module for the user, the user can create questions, and it will save as an object


class Score(models.Model):
    user = models.ForeignKey(User, related_name="scores", on_delete=models.CASCADE)
    list = models.ForeignKey(List, related_name="scores", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    #score of the user, which is saved in the database and displayed 
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + str(self.score)