from django.urls import path
from .import views


app_name='photo'

urlpatterns=[

# 診断アプリのトップページ
path('',views.IndexView.as_view(),name='index'),

# situation：状況の選択ページ
path('situation/', views.situation, name='situation'),

# purpose:目的の選択ページ
path('interest/', views.interest, name='interest'),


#language:言語の選択ページ
path('language/', views.language, name='language'),


# religion:宗教の選択ページ
path('religion/', views.religion, name='religion'),

# 結果表示ページ
path('recommend/',views.recommend,name='recommend'),


    # 写真投稿のトップページ
path('photo_index/',views.PhotoIndexView.as_view(),name='photo_index'),
    # Formを二つ作ったので、関数で書いた
path('post/',views.create_photo_view,name='post'),
path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
path('photos/<int:country>',views.CountryView.as_view(),name='photos_cat'),
path('user-list/<int:user>',views.UserView.as_view(),name='user_list'),
# 詳細ページ
path('detail/<int:pk>',views.detail, name='detail'),
path('mypage/',views.MypageView.as_view(),name='mypage'),
path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name='photo_delete'),
path('photo/<int:pk>/update/',views.PhotoUpdateView.as_view(),name='photo_update'),


]