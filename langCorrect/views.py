from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django import forms
from .models import Post, LanguageLevel, Correction, Sentence, CustomUser
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm, LanguageForm, Language, CorrectSentence


def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        language_form = LanguageForm(request.POST)
        if user_form.is_valid() and language_form.is_valid():
            print('Досюда работает')
            user = user_form.save()
            language_name = language_form.cleaned_data['name']
            language = Language.objects.filter(name=language_name).first()
            level = language_form.cleaned_data['level']
            new_language = LanguageLevel.objects.create(student=user, language=language, level=level)
            new_language.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('journal')  # Перенаправление на главную страницу после успешной регистрации
    else:
        user_form = CustomUserCreationForm()
        language_form = LanguageForm()
    return render(request, 'langCorrect/signup.html', {'user_form': user_form, 'language_form': language_form})


def journal(request):
    posts = Post.objects.all()
    return render(request, 'langCorrect/journal.html', context={'posts': posts})


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'text', 'native_text', 'language', 'gender']
    #form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        print(self.request.user)
        form = super().get_form(form_class)
        print(LanguageLevel.objects.filter(student=self.request.user).values_list('language', flat=True))
        # print('Выше должен быть список языков')
        language_names = LanguageLevel.objects.filter(student=self.request.user).values_list('language_id', flat=True)
        form.fields['language'].queryset = Language.objects.filter(pk__in=language_names)
        return form


class PostDetail(DetailView):
    model = Post  # Указываем модель, которую мы хотим отобразить
    template_name = 'langCorrect/postDetail.html'  # Указываем имя шаблона, который мы будем использовать
    context_object_name = 'post'

    def get_queryset(self):
        post_title = self.kwargs.get('pk')
        return Post.objects.filter(title=post_title)


def prompts(request):
    return HttpResponse('<h1>Промпты</h1>')


def corrections(request, post_title):
    if request.method == 'POST':
        content_len = len(Post.objects.all().filter(title=post_title).first().text.split('.'))
        content = Post.objects.all().filter(title=post_title).first().text.split('.')
        new_correction = Correction.objects.create(post=Post.objects.all().filter(title=post_title).first(), author=request.user)
        new_correction.save()
        for i in range(content_len):
            new_sentence = Sentence.objects.create(correction=new_correction)
            new_sentence.original = content[i]
            if request.POST.getlist('text')[i]:
                new_sentence.text = request.POST.getlist('text')[i]
            else:
                new_sentence.isCorrect = True
            if new_sentence.text == new_sentence.original:
                new_sentence.isCorrect = True
            if request.POST.getlist('commentary')[i]:
                new_sentence.commentary = request.POST.getlist('commentary')[i]
            new_sentence.save()
        return redirect('journal')

    else:
        content = Post.objects.all().filter(title=post_title).first().text.split('.')
        forms = []
        for sentence in content:
            new_tuple = (sentence, CorrectSentence())
            print(tuple)
            forms.append(new_tuple)

        return render(request, 'langCorrect/corrections.html', context={'content': content, 'form': forms})


def profile(request, username):
    user = CustomUser.objects.get(username=username)
    languages = LanguageLevel.objects.filter(student=user)
    posts = user.post_set.all()
    return render(request, 'langCorrect/profile.html', context={'user': user, 'languages': languages,                                                             'posts': posts})


class LanguageList(ListView):
    model = LanguageLevel
    context_object_name = 'languageLevels'
    template_name = 'langCorrect/languageList.html'

    def get_queryset(self):
        return LanguageLevel.objects.filter(student=self.request.user)


class DeleteLanguage(DeleteView):
    model = LanguageLevel
    template_name = 'langCorrect/deleteLanguage.html'
    context_object_name = 'language'


