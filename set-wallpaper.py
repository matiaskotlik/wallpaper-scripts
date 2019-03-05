#!/usr/bin/env python3
import dbus
import argparse
import sys
import mimetypes

# Modified from https://github.com/pashazz/ksetwallpaper/blob/master/ksetwallpaper.py
# This version detects if the file is a video or image and sets the wallpaper accordingly

image = """
var allDesktops = desktops();
print (allDesktops);
for (i=0;i<allDesktops.length;i++) {{
    d = allDesktops[i];
    d.wallpaperPlugin = "org.kde.image";
    d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
    d.writeConfig("Image", "file://{filename}")
    d.writeConfig("FillMode", 2)
}}
"""
video = """
var allDesktops = desktops();
print (allDesktops);
for (i=0;i<allDesktops.length;i++) {{
    d = allDesktops[i];
    d.wallpaperPlugin = "VideoWallpaper";
    d.currentConfigGroup = Array("Wallpaper", "VideoWallpaper", "General");
    d.writeConfig("VideoWallpaperBackgroundVideo", "file://{filename}")
}}
"""

parser = argparse.ArgumentParser(description='KDE Wallpaper setter')
parser.add_argument('filename', help='Wallpaper file name')
parser.add_argument('-t', '--filetype', choices=('image', 'video'), help='Type of wallpaper, image or video')
args = parser.parse_args()


bus = dbus.SessionBus()
plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')

mimetype = args.filetype

if (mimetype == None):
    mimetype = mimetypes.guess_type(args.filename)[0]

    if (mimetype == None):
        print('Unrecognized file type, please specify the file type', file=sys.stderr)
        sys.exit(1)

script = video if mimetype.startswith('video') else image

plasma.evaluateScript(script.format(filename=args.filename))
