#!/usr/bin/env python3

import constants
import extract_scene
import subprocess
import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

config = constants.config


class Handler(FileSystemEventHandler):
    def __init__(self, watch_file):
        self.watch_file = watch_file
        super(Handler, self).__init__()

    def on_any_event(self, event):
        if event.event_type == 'modified' and event.src_path == self.watch_file:
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)
            args = sys.argv.copy()
            args.remove("--watch")
            subprocess.Popen(args, env=os.environ)


if config["stream"]:
    # livestream()
    pass
else:
    if config["watch"]:
        print("watching...")
        watch_file = os.path.abspath(os.getcwd() + os.sep + config["file"])
        watch_dir = os.path.dirname(watch_file)
        event_handler = Handler(watch_file)
        observer = Observer()
        observer.schedule(event_handler, watch_dir)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("Stopped")
        observer.join()
    else:
        extract_scene.main(config)

# import sys
# import argparse
# # import imp
# import importlib
# import inspect
# import itertools as it
# import os
# import subprocess as sp
# import traceback
# 
# from constants import *
# 
# from scene.scene import Scene
# from utils.sounds import play_error_sound
# from utils.sounds import play_finish_sound
# 
# from colour import Color
# 
# 
# class Manim():
# 
#     def __init__(self):
#         self.config = {
#             "file": "example_file.py",
#             "scene_name": "LiveStream",
#             "open_video_upon_completion": False,
#             "show_file_in_finder": False,
#             # By default, write to file
#             "write_to_movie": True,
#             "show_last_frame": False,
#             "save_pngs": False,
#             # If -t is passed in (for transparent), this will be RGBA
#             "saved_image_mode": "RGB",
#             "movie_file_extension": ".mp4",
#             "quiet": True,
#             "ignore_waits": False,
#             "write_all": False,
#             "name": "LiveStream",
#             "start_at_animation_number": 0,
#             "end_at_animation_number": None,
#             "skip_animations": False,
#             "camera_config": HIGH_QUALITY_CAMERA_CONFIG,
#             "frame_duration": PRODUCTION_QUALITY_FRAME_DURATION,
#         }
