# from operator import index

# # import requests
# import json
# import os
import subprocess

# import pandas as pd
# from glob import glob


# def runBash(command):
#     os.system(command)


def download_stream(url, save_name, duration=60):
    # Use subprocess to run the FFmpeg command
    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        url,
        "-t",
        str(duration),
        "-acodec",
        "copy",
        "-vcodec",
        "copy",
        "-y",
        "-loglevel",
        "info",
        "-f",
        "mp4",
        save_name,
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Downloaded {duration} seconds of video from {url} to {save_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


# "ffmpeg -i "+'https://d387613w8yyayj.cloudfront.net/405_2022_07_30_09_39_33_19693208/index.m3u8'+ " -acodec copy -vcodec copy  -y -loglevel info -f mp4 "+save_name

# save_name = './downloaded_stream/my.mp4'
# url = 'https://d387613w8yyayj.cloudfront.net/405_2022_07_30_09_39_33_19693208/index_504p30.m3u8'
# download_stream(url,save_name)

if __name__ == "__main__":
    url = "https://d387613w8yyayj.cloudfront.net/402_2022_03_10_14_53_12_15227505/index.m3u8"
    save_name = "./downloaded_stream/my_video.mp4"

    download_stream(url, save_name)

    # df = pd.read_csv("./stream_url.csv", index_col=None)
    # print(df.head(5))
    # print(df.columns)

    # existing_vid = glob("./downloaded_stream/*.mp4")
    # count = 0
    # for ind in df.index:
    #     if ind > 10:
    #         if count == 2:
    #             break

    #         save_name = (
    #             "./downloaded_stream/" + df["title"][ind].replace(" ", "") + ".mp4"
    #         )
    #         url = df["video_url"][ind]
    #         url_wintout_extension = url[: len(url) - 5] + "_720p30.m3u8"
    #         print(url_wintout_extension)
    #         if save_name not in existing_vid:
    #             print("\n\n\n... Downloading: ", save_name)
    #             try:
    #                 download_stream(url_wintout_extension, save_name)
    #                 count += 1
    #             except:
    #                 pass
    #     # if count>=15:
    #     #     break
