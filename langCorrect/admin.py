from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Correction, Language, CustomUser, LanguageLevel, Sentence

from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "native_language"]


admin.site.register(Post)
admin.site.register(Correction)
admin.site.register(CustomUser)
admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(Sentence)

