import random
from typing import Any, Dict, Optional
from django.db import models

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
import pendulum as pdl
from datetime import datetime, timedelta
from .forms import CardCheckForm
from .models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("-review_date")


class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer"]
    success_url = reverse_lazy("card-create")


class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")


# class CardDetailView(DetailView):
#     model = Card
#     fields = [
#         "question",
#         "answer",
#         "easiness",
#         "repetitions",
#         "interval",
#         "review_date",
#     ]
#     queryset = Card.objects.all()
#     template_name = "cards/box.html"
#     form_class = CardCheckForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.object:
#             context["check_card"] = self.object
#         return context

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
#             print("cardId", form.cleaned_data["card_id"])
#             print("repetition", card.repetitions)
#             print("quality", form.cleaned_data["quality"])
#             if card.repetitions == 0:
#                 card.set_first_review(quality=form.cleaned_data["quality"])
#             else:
#                 card.next_review(quality=form.cleaned_data["quality"])
#         return redirect(request.META.get("HTTP_REFERER"))


class StartReview(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        # return Card.objects.all()
        return Card.objects.filter(review_date__lte=datetime.now() + timedelta(days=1))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list:
            print("object list", self.object_list, type(self.object_list))
            context["check_card"] = random.choice(self.object_list)
            print("context", context)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            print("cardId", form.cleaned_data["card_id"])
            print("repetition", card.repetitions)
            print("quality", form.cleaned_data["quality"])
            if card.repetitions == 0:
                card.set_first_review(quality=form.cleaned_data["quality"])
            else:
                card.next_review(quality=form.cleaned_data["quality"])
        return redirect(request.META.get("HTTP_REFERER"))
