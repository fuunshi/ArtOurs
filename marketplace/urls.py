from django.urls import path, include
from .views import (
    edit_artwork,
	marketplace,
	artwork_detail,
	add_artwork,
    like_artwork,
    add_review,
    delete_artwork
)

urlpatterns = [
    path("list/", marketplace, name='marketplace'),
    path("list/<int:artwork_id>/", artwork_detail, name="artwork_detail"),
    path("list/<int:artwork_id>/edit", edit_artwork, name="edit_artwork"),
    path("list/<int:artwork_id>/delete", delete_artwork, name="delete_artwork"),
    path("list/<int:artwork_id>/addreview", add_review, name="add_review"),
    path("add/", add_artwork, name="art_add"),
    path("like/<int:artwork_id>", like_artwork, name="like_artwork"),
]
