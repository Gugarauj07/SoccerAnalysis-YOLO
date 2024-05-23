from utils import read_video, save_video

def main():
    video_path = "input_videos/08fd33.mp4"
    frames = read_video(video_path)
    save_video(frames, "output_videos/output_video.avi")

if __name__ == "__main__":
    main()