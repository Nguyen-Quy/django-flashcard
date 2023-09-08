from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list",
    ),
    path(
        "create",
        views.CardCreateView.as_view(),
        name="card-create",
    ),
    path(
        "update/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update",
    ),
    # path(
    #     "card/<int:pk>",
    #     views.CardDetailView.as_view(),
    #     name="card-detail",
    # ),
    path(
        "review",
        views.StartReview.as_view(),
        name="card-review",
    ),
]
