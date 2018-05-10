from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.contrib import sessions
from . import models
from .models import User,Vote,Entry,Selection
from block import block_hashfunc
import dateutil.parser
from .models import User,Vote
import block.model_block as bm
import datetime
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='username',max_length=50)
    password = forms.CharField(label='password',widget=forms.PasswordInput())

# class VoteForm(forms.Form):
#     vote_name = forms.CharField(max_length=50)
#     vote_description = forms.
#     vote_type = models.IntegerField()  # 多选,单选
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     option_size = models.IntegerField()  # 选项数目
#     option_content = models.TextField()  # 选项内容,可能为一个json文件



def hello(request):
    return HttpResponse('<html>hi </html>')

def index(request):
    articles =  models.Artivle.objects.all()
    return render(request,'index.html',{'artilces':articles})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                request.session['user_id'] = user.first().user_id
                return HttpResponseRedirect('/card')
            else:
                return render(request, "login.html", {"msg": u"用户名或密码错误"})

def form(request):
    # 先检验登录状态
    if request.method == 'GET':
        return render(request, 'form.html')
    else:
        # hash 校验
        if Vote.objects.filter(vote_target=block_hashfunc.hash(str(request.POST.get("vote_name")).encode())):
            return HttpResponse(" this vote has been exist!")
        else:
            vote = Vote()
            entry = Entry()
            vote.creat_time = datetime.datetime.now()
            vote.vote_name = request.POST.get("vote_name")
            vote.vote_description = request.POST.get("vote_description")
            vote.start_time = request.POST.get("start_time")
            vote.end_time = request.POST.get("end_time")

            d =  datetime.datetime.now()
            if dateutil.parser.parse(request.POST.get("start_time")) > d : # 未开始
                vote.vote_state = 1
            elif dateutil.parser.parse(request.POST.get("end_time")) > d : # 进行中
                vote.vote_state = 2
            else: # 已结束
                vote.vote_state = 3

            if request.POST.get("is_opened") == "yes":  # 是否是公开投票
                vote.is_opened = True
            else:
                vote.is_opened = False
            if request.POST.get("is_checkable") == "须权限认证":  # 是否展示投票结果给参与者
                vote.is_checkable = True
            else:
                vote.is_checkable = False

            if request.POST.get("vote_type") == "单选":
                vote.vote_type = 1
            else:
                vote.vote_type = 2
            vote_target = block_hashfunc.hash(str(vote.vote_name).encode())
            vote.vote_target = vote_target
            vote.save()
            entry.user_id = User.objects.filter(user_id=request.session['user_id']).first()
            entry.vote_id = Vote.objects.get(vote_target=vote_target)
            entry.identity = 2  # 表示发起人
            entry.condition = False
            entry.save()
            return card(request)



def vote(request):
    target = request.GET.get("target")
    vote = Vote.objects.filter(vote_target=target)
    if vote is None:
        return HttpResponse("Wrong vote target!")
    select = Selection.objects.filter(vote_id=vote.vo)
    br = bm.BlockReader()
    on_chain_result = br.getVoteResult(target)
    # on_web_list = vote.
    print(vote.vote_name)
    candidate = list()
    candidate.append({"id":1, "option": "A. Boris.Chen","img": "/static/img/team/member1.jpg", "content": "大家好我是鲍里斯陈，来自db group，我爱麻辣火锅，谢谢大家支持。\n"*4})
    candidate.append({"id":2, "option": "B. Mark.Zeng","img": "/static/img/team/member5.jpg","content": "大家好我是马克曾，来自db group，我爱牛肉火锅，谢谢大家支持。\n"*4})
    candidate.append({"id":3, "option": "B. Mark.Zeng","img": "/static/img/team/member5.jpg","content": "大家好我是马克曾，来自db group，我爱牛肉火锅，谢谢大家支持。\n"*4})
    candidate.append({"id":4, "option": "B. Mark.Zeng","img": "/static/img/team/member5.jpg","content": "大家好我是马克曾，来自db group，我爱牛肉火锅，谢谢大家支持。\n"*4})
    votename = "VoteName"
    voteLimit = 1
    max_id = len(candidate)
    t = "单选题"
    description = "这里是描述"
    target = "target"
    miner_list = br.getMinerList()
    return render(request, 'vote.html', {'votes': candidate
                                         , "votename": votename
                                         , "voteLimit":voteLimit
                                         , "max_id":max_id
                                         , "type": t
                                         , "description": description
                                         , "target": target
                                         , "miner_list": miner_list})
    # return render(request, 'vote.html')

def card(request):
    u_id = request.session['user_id']  # 获取当前user_id
    votes = []
    e = Entry.objects.filter(user_id=u_id)
    for item in e:
        votes.append(item.vote_id)
    return render_to_response('card.html',{"votes":votes})
# def creat_vote(request):

def article_page(request,id):
    article = models.Artivle.objects.get(pk=id)
    return  render(request,'startvote/page.html',{'article':article})

def edit_page(request,id):
    if str(id)=='0':
        return render(request,'startvote/edit.html')
    article = models.Artivle.objects.get(pk=id)
    return render(request, 'startvote/edit.html',{'article':article})

def edit_action(request):
    title = request.POST.get('title','TITLE')#后面是默认值
    content = request.POST.get('content','CONTENT')
    id = request.POST.get('id','0')
    if id=='0':
        models.Artivle.objects.create(title=title,content=content)

    else:
        article = models.Artivle.objects.get(pk=id)
        article.title = title
        article.content = content
        article.save()

    articles = models.Artivle.objects.all()
    return render(request, 'startvote/index.html', {'artilces': articles})

#获得单个block内的信息
def single_block_info(request):
    block_id = request.POST.get("id", 0)
    br = bm.BlockReader()
    infos = br.getSingleBlockInfo(block_id)
    title = ["target", "pubkey", "selection", "timestamp"]
    format_infos = []
    for i in infos:
        i = list(i)
        i[0] = i[0][:16]
        i[1] = i[1][:16]
        dateArray = datetime.datetime.utcfromtimestamp(i[3])
        i[3] = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        format_infos.append(i)
    return render(request, 'single_block_info.html', {'infos': format_infos, 'title': title})

#获得block chain的信息
def block_info(request):
    br = bm.BlockReader()
    blocks = br.getBlockInfos()
    title = ["Id","hash","prehash","vote_num","generator"]
    format_blocks = []
    for b in blocks:
        b = list(b)
        b[1] = b[1][:32]   #截取哈希的前32位
        b[2] = b[2][:32]
        format_blocks.append(b)
    return render(request, 'block_info.html', {'blocks': format_blocks, 'title': title})