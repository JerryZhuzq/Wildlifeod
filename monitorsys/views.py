from django.shortcuts import render
from django.http import JsonResponse
import os

# Create your views here.


def index(request):
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