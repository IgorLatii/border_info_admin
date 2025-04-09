from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import QuestionAnswer, PredefinedResponse


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_summary', 'answer', 'language', 'processed', 'created_at', 'updated_at')
    search_fields = ('question', 'processed')
    list_filter = ('language', 'processed')
    ordering = ('-updated_at',)

    def question_summary(self, obj):
        return obj.question[:50] + "..." if len(obj.question) > 50 else obj.question
    question_summary.short_description = "Question"

@admin.register(PredefinedResponse)
class PredefinedResponseAdmin(admin.ModelAdmin):
    list_display = ('command', 'language', 'created_at')
    search_fields = ('command', 'response_text')
    list_filter = ('language',)
    ordering = ('command',)
