from django.db import models

# Create your models here.

class Task(models.Model):
    # Taskクラスを作成
    title = models.CharField(max_length=100)
    # タイトルは100文字までの文字列
    created = models.DateTimeField(auto_now_add=True)
    # 作成日時は自動で現在の日時が入る
    completed = models.BooleanField(default=False)
    # 完了フラグはデフォルトでFalse

    def __str__(self):
        return self.title
    # タイトルを返す