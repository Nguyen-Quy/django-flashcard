from django.db import models
from django.utils.translation import gettext_lazy as _
import pendulum as pdl
from .algorithm import SMTwo

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    easiness = models.FloatField(default=2.5)
    repetitions = models.PositiveIntegerField(default=0)
    interval = models.IntegerField(default=1)
    review_date = models.DateField(null=True)

    class Meta:
        ordering = ["review_date"]

    def set_first_review(self, quality: int):
        first_rv = SMTwo.first_review(quality=quality)
        self.easiness = first_rv.easiness
        self.interval = first_rv.interval
        self.repetitions = first_rv.repetitions
        self.review_date = first_rv.review_date
        self.save()

    def next_review(self, quality: int):
        next_rv = SMTwo(self.easiness, self.interval, self.repetitions).review(
            quality=quality
        )
        self.easiness = next_rv.easiness
        self.interval = next_rv.interval
        self.repetitions = next_rv.repetitions
        self.review_date = next_rv.review_date
        self.save()

    def __str__(self):
        return self.question

    # def move(self, solved):
    #     new_box = self.box + 1 if solved else BOXES[0]
    #     if new_box in BOXES:
    #         self.box = new_box
    #         self.save()
    #     return self
