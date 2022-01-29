from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name


class List(models.Model):
    list_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="lists", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_questions = models.IntegerField(default=0)

    def __str__(self):
        return self.list_name

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    list = models.ForeignKey(List, related_name="questions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    correct_phrase = models.CharField(max_length=500)
    image_path = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.question_text

class Score(models.Model):
    user = models.ForeignKey(User, related_name="scores", on_delete=models.CASCADE)
    list = models.ForeignKey(List, related_name="scores", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + str(self.score)