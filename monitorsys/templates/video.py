import os

def upload_video():
    video_file = "../static/video"
    video_dict = {}
    for idx, i in enumerate(os.listdir(video_file)):
        if i.endswith((".mp4", ".mkv", ".avi")):
            video_path = os.path.join(video_file, i)
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
    return video_dict


print(upload_video())