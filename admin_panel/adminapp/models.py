from django.db import models

# Create your models here.
from django.db import models

class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    language = models.CharField(max_length=10, choices=[('ru', 'Russian'), ('ro', 'Romanian'), ('en', 'English')])
    embedding = models.TextField(blank=True, null=True)  # JSON-vector
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'question_answer'

    def __str__(self):
        return f"Q: {self.question[:50]}..."

class UserQuery(models.Model):
    user_id = models.BigIntegerField(null=True, blank=True)
    query = models.TextField()
    detected_keywords = models.TextField(null=True, blank=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_queries'

    def __str__(self):
        return f"User {self.user_id}: {self.query[:50]}..."

class PredefinedResponse(models.Model):
    command = models.CharField(max_length=50)
    response_text = models.TextField()
    language = models.CharField(max_length=10, choices=[('ru', 'Russian'), ('ro', 'Romanian'), ('eng', 'English')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('command', 'language')  # unique combination
        db_table = 'predefined_responses'

    def __str__(self):
        return f"{self.command} ({self.language})"