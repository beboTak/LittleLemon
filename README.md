this is my Django project
path for the project and app :
project path:
 path('admin/', admin.site.urls),
    path('restaurant/',include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
app path :
path('index/', views.index, name='index'),
path('menu/', views.MenuItemsView.as_view()),
path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
path('message/', views.msg),
path('api-token-auth/', obtain_auth_token),
