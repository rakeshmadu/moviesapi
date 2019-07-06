from django.urls import path
from.views import get_maxd,get_mostpop,post_fav,get_least_watch,get_best_dir,get_top_ten

urlpatterns=[
    path('maxd/',get_maxd),
    path('mpop/',get_mostpop),
    path('fav/',post_fav),
    path('least/',get_least_watch),
    path('best/',get_best_dir),
    path('top/',get_top_ten)

]