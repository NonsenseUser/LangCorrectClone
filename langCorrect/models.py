from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(max_length=20, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    male = "Мужской"
    female = "Женский"
    other = "Другой"
    unknown = "Предпочитаю не указывать"

    username = models.CharField(max_length=20, primary_key=True, unique=True)
    gender_choice = ((male, "Мужской"), (female, "Женский"), (other, "Другой"), (unknown, "Предпочитаю не указывать"))
    native_language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name="native_language", null=True)
    gender = models.CharField(choices=gender_choice, default=unknown)


class LanguageLevel(models.Model):
    level_choices = [("A2", "Новичок"), ("A1", "Элементарный"), ("B2", "Средний"), ("B1", "Выше среднего"),
                     ("C2", "Продвинутый"), ("C1", "Опытный")]
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    student = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    level = models.CharField(max_length=20, choices=level_choices, default="Новичок")

    def __str__(self):
        return self.student.username + " knows " + self.language.name + " at " + self.level + " level"


class Post(models.Model):
    male = "Мужской"
    female = "Женский"
    other = "Другой"
    unknown = "Предпочитаю не указывать"
    gender_choice = ((male, "Мужской"), (female, "Женский"), (other, "Другой"), (unknown, "Предпочитаю не указывать"))

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, primary_key=True, unique=True)
    verbose_title = models.CharField(max_length=20)
    text = models.TextField()
    native_text = models.TextField(null=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    gender = models.CharField(choices=gender_choice, default=unknown)
    #permission = models.CharField(choices=(('all', 'Видимо всем'), ('signedIn', 'Видно только зарегистрированный пользователям')))
    correctionsQuantity = models.IntegerField(default=0)
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Correction(models.Model):
    # def __init__(self, *args, **kwargs):
    #     super(Correction, self).__init__(*args, **kwargs)
    #     self.original = self.post.text

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    commentary = models.TextField(null=True)
    # corrected = models.TextField()


class Sentence(models.Model):
    original = models.TextField()
    text = models.TextField(default='')
    commentary = models.TextField(default='')
    isCorrect = models.BooleanField(default=False)
    correction = models.ForeignKey(Correction, on_delete=models.CASCADE)

    def __str__(self):
        if self.text != '':
            return self.text
        else:
            return 'Все правильно'










