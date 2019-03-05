# wallpaper-scripts
A script to change my wallpaper from the cli. Works only on KDE Plasma.

# How to use
Link to `set-wallpaper.py` somewhere in your path, for example,
`ln -s /clone/directory/set-wallpaper.py /home/matias/bin/set-wallpaper`.
Restart your shell, and now you can call set-wallpaper /path/to/image/or/video to set your wallpaper.

# Video Wallpapers
You need to have the [VideoWallpaper](https://store.kde.org/p/1213488) plugin installed in order to set a video as your wallpaper.
From the VideoWallpaper link on how to install:

```
Install:
kpackagetool5 -t Plasma/Wallpaper -i VideoWallpaper.tar.gz

Remove:
kpackagetool5 -t Plasma/Wallpaper -r VideoWallpaper
```

# Binding to keyboard shortcuts
I have bound a few wallpapers to keyboard shortcuts using KDE's Shortcuts module in System Settings.
This way, I can switch wallpapers quickly.
