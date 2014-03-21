from django.conf.urls import patterns, url
from recipes import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^add_category/$', views.add_category,
                           name='add_category'),
                       url(r'^category/(?P<category_name_url>\w+)/$',
                           views.category, name='category'),
                       url(r'^add_recipe/$',
                           views.add_recipe, name='add_recipe'),
                       url(r'^add_ingredient/$', views.add_ingredient,
                           name='add_ingredient'),
                       url(r'recipe/(?P<recipe_id>\d+)/add_recipe_ingredient/$',
                           views.add_recipe_ingredient, name='add_recipe_ingredient'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^restricted/$', views.restricted,
                           name='restricted'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^goto/$', views.track_url, name='track_url'),
                       url(r'^like_category/$', views.like_category,
                           name='like_category'),
                       url(r'^suggest_category/$', views.suggest_category,
                           name='suggest_category'),
                       url(r'^suggest_recipe/$', views.suggest_recipe,
                           name='suggest_recipe'),
                       url(r'^auto_add_recipe/$', views.auto_add_recipe,
                           name='auto_add_recipe'),
                       url(r'^recipe/(?P<recipe_id>\d+)/$',
                           views.show_recipe, name='recipe'),
                       url(r'^recipe/(?P<recipe_id>\d+)/edit/$',
                           views.add_recipe, name='edit_recipe'),
                       )
