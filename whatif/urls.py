from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login, logout
from whatif.games.views.admin import (admin_index, new_game, edit_game, remove_question, delete_game, 
                                             add_token, remove_token, add_question, update_modifier)
from whatif.games.views.public import (home, view_game, play_game, answer_question)

urlpatterns = patterns('',
    url('^$', home, name='home'),
    url('^game/(\w+)/$', view_game, name='view-game'),
    url('^game/(\w+)/play/$', play_game, name='play-game'),
    url('^instance/(\w+)/respond/$', answer_question, name='answer-question'),
    url('^admin/$', admin_index, name='admin'),
    url('^admin/login/$', login, {'template_name': 'admin/login.html'}, name='log-in'),
    url('^admin/logout/$', logout, {'next_page': '/'}, name='log-out'),
    url('^admin/new/$', new_game, name='new-game'),
    url('^admin/(\w+)/delete/$', delete_game, name='delete-game'),
    url('^admin/(\w+)/addtoken/$', add_token, name='add-token'),
    url('^admin/(\w+)/rmtoken/(\w+)/$', remove_token, name='remove-token'),
    url('^admin/(\w+)/q/(\w+)/update/$', update_modifier, name='update-modifier'),
    url('^admin/(\w+)/addquestion/$', add_question, name='add-question'),
    url('^admin/(\w+)/rmquestion/(\w+)/$', remove_question, name='remove-question'),
    url('^admin/(\w+)/edit/$', edit_game, name='edit-game'),
)
