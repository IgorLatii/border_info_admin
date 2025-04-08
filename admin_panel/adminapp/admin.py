from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import QuestionAnswer, UserQuery, PredefinedResponse


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_summary', 'language', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('language', )
    ordering = ('-updated_at',)

    def question_summary(self, obj):
        return obj.question[:50] + "..." if len(obj.question) > 50 else obj.question
    question_summary.short_description = "Question"

@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'query_summary', 'processed', 'created_at')
    search_fields = ('query', )
    list_filter = ('processed', )
    ordering = ('-created_at',)

    def query_summary(self, obj):
        return obj.query[:50] + "..." if len(obj.query) > 50 else obj.query
    query_summary.short_description = "User Query"

@admin.register(PredefinedResponse)
class PredefinedResponseAdmin(admin.ModelAdmin):
    list_display = ('command', 'language', 'created_at')
    search_fields = ('command', 'response_text')
    list_filter = ('language',)
    ordering = ('command',)
