"""vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
import startvote.views as v1

handler404 = v1.page_not_found
handler403 = v1.page_not_found
handler500 = v1.page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', v1.index, name="index"),
    re_path(r'^login$', v1.login, name="login"),
    re_path(r'^signup$', v1.signup, name="signup"),
    re_path(r'^logout$', v1.logout, name="logout"),
    re_path(r'^form$', v1.form, name="form"),
    re_path(r'^card$', v1.card, name="card"),
    re_path(r'^error$', v1.page_not_found, name="error"),
    re_path(r'^share$', v1.share, name="share"),
    re_path(r'^vote/(?P<target>.*?)$', v1.vote, name="vote"),
    re_path(r'^result$', v1.real_time_result, name="realTimeResult"),



    # re_path(r'^article/(?P<id>[0-9]+)$', v1.article_page, name="article_page"),
    # re_path(r'^edit/(?P<id>[0-9]+)$', v1.edit_page, name='edit_page'),
    # re_path(r'^edit/action$', v1.edit_action, name='edit_action'),
    # re_path(r'hello', v1.hello),
    re_path(r'^fold_demo$', v1.fold_demo, name="fold_demo"),
    re_path(r'^block_info$', v1.block_info, name="block_info"),
    re_path(r'^single_block_info$', v1.single_block_info, name="single_block_info"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
