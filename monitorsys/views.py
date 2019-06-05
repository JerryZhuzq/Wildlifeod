from django.shortcuts import render,render_to_response
from django.http import JsonResponse
from django.template import RequestContext
from django.template.context_processors import csrf
from monitorsys.models import UserInfo, VideoInfo
from django.core.mail import send_mail
import os

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if username != "" and password != "":
            userResult = UserInfo.objects.filter(username=username,password=password)
            if(len(userResult)>0):
                request.session['username']=username
                user=UserInfo.objects.get(username=username)
                user_name=user.username
                return render_to_response('index.html',context=csrf(request))
                # return render_to_response('index.html',locals(), context_instance=RequestContext(request))
            else:
                c = csrf(request)
                c.update({'message':"用户名或密码错误"})
                return render_to_response('login.html',context = c)
        else:
            c = csrf(request)
            c.update({'message':"用户名或密码不能为空"})
            return render_to_response('login.html',context = c)
            # return render_to_response('login.html',{'message':"用户名或密码不能为空"}, context_instance=RequestContext(request))
    else:
        return render(request,'login.html')

def index(request):
	return render(request,'index.html')

def upload_video(request):
	video_file = "static/video"
	video_path = ""
	video_dict = {}
	for idx, i in enumerate(os.listdir(video_file)):
		if i.endswith((".mp4",".mkv",".avi")):
			video_path = os.path.join(video_file,i)
			num = str(i.split('_')[0])
			video_dict[video_path] = [num]
			if i.split("_")[1] == "wy":
				video_dict[video_path].append(['文一路'])
			if i.split("_")[1] == "we":
				video_dict[video_path].append(['文二路'])
			if i.split("_")[2][:-4] == "panda":
				video_dict[video_path].append("大熊猫")
			if i.split("_")[2][:-4] == "tiger":
				video_dict[video_path].append("老虎")
			if i.split("_")[2][:-4] == "elephant":
				video_dict[video_path].append("大象")
	return JsonResponse(video_dict)

def raise_alarm(request):
	if request.method == "POST":
		host_email = '846527233@qq.com'
		target_email = 'jerryzhu_@outlook.com'
		wildlife_name = request.GET['wildlife_name']
		alarm_loca = request.GET['alarm_loca']
		ala_mess = '野生动物出没警报，野生动物种类: ' + wildlife_name +', 出没区域: ' + alarm_loca
		send_email('野生动物警报！', ala_mess, host_email, [target_email], fail_silently = False)
		c = csrf(request)
		c.update({'message':"警报已发送"})
		return render_to_response('index.html',context = c)
	else:
		return render(request,'index.html')


def upload_img(request):
	img_file = "static/images/monitoring"
	img_path = ""
	img_dict = {}
	for idx, i in enumerate(os.listdir(img_file)):
		if i.endswith(".jpg"):
			img_path = os.path.join(img_file,i)
			num = str(i.split('_')[0])
			img_dict[img_path] = [num]
			if i.split("_")[1] == "wy":
				img_dict[img_path].append(['识别成功'])
			if i.split("_")[1] == "we":
				img_dict[img_path].append(['文二路'])
			if i.split("_")[2][:-4] == "friedrice":
				img_dict[img_path].append("炒饭")
			if i.split("_")[2][:-4] == "sushi":
				img_dict[img_path].append("寿司")
			if i.split("_")[2][:-4] == "steak":
				img_dict[img_path].append("牛排")
	return JsonResponse(img_dict)