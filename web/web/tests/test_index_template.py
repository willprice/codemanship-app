from django.test  import TestCase
from django.template.loader import render_to_string
from core.player import Player
from core.queue import Queue
from lxml import etree


class IndexTemplateTests(TestCase):
    def test_page_with_two_players_has_two_list_elements_in_player_div(self):
        will = Player("Will")
        jason = Player("Jason")
        queue = Queue()
        queue.add_players([will, jason])
        context = {'queue': queue, 'games': None}
        html = render_to_string('web/index.html', context)
        html_tree = etree.fromstring(html)

        number_of_players_matcher = etree.XPath("//div[@id='players']/ul/li")
        number_of_players = number_of_players_matcher(html_tree)
        self.assertEqual(2, len(number_of_players))
