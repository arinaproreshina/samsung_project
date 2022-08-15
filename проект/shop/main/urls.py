@@ -4,6 +4,7 @@


app_name = 'main'

urlpatterns = [
    path('index', views.index, name = "index"),
    path('profile', views.profile, name = "profile"),