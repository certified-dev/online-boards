from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Post, Topic
from ..views import reply_topic


class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    # ...

    def test_redirection(self):
        """
        A valid form submission should redirect the user
        """
        url = reverse('topic_posts', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
        topic_posts_url = '{url}?page=1#2'.format(url=url)
        self.assertRedirects(self.response, topic_posts_url)
