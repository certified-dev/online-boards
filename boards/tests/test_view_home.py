from ..views import BoardListView, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

from django.test import TestCase
from django.urls import resolve


class HomeTests(TestCase):
    # ...
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)
