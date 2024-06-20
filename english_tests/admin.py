from django.contrib import admin
from .models import IELTS, Duolingo, TOEFL, CEFR


@admin.register(IELTS)
class IELTSAdmin(admin.ModelAdmin):
    list_display = ('id', 'listening', 'reading', 'writing', 'speaking')


@admin.register(Duolingo)
class DuolingoAdmin(admin.ModelAdmin):
    list_display = ('id', 'literacy', 'conversation', 'comprehension', 'production')


@admin.register(TOEFL)
class TOEFLAdmin(admin.ModelAdmin):
    list_display = ('id', 'reading', 'listening', 'speaking', 'writing')


@admin.register(CEFR)
class CEFRAdmin(admin.ModelAdmin):
    list_display = ('id', 'listening', 'reading', 'writing', 'speaking')
