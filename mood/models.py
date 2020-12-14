from django.db import models

class Thinker(models.Model):
    name = models.CharField("name of thinker", max_length=30)

    class Meta:
        unique_together = ['name']
        ordering = ['name']

class Mood(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mood = models.IntegerField("mood of person")
    thinker = models.ForeignKey(Thinker,
        on_delete=models.CASCADE,
        related_name='moods')

    class Meta:
        ordering = ['created']
