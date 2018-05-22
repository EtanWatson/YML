from django.shortcuts import render
from .picture_analysis import *

# 首页
def index(request):

    # 获取
    return render(request, 'index.html')

# 自己的home页面
def home(request):

    # 解析最相似的几个图片  todo: 这个照片可以是本地传上来的，也可以是在页面中选中的
    context = {}
    res =parse_multi_res("/static/images/SCUT-FBP-1.jpg")
    context ['res'] = res

    return render(request, 'home.html', context)

