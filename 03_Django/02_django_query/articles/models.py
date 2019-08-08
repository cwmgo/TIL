from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10) # 글자수를 제한하는 함수.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updatated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'
