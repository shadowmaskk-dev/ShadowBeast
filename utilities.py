import os
import urllib.parse

APPS = {
    "youtube": "am start -n com.google.android.youtube/com.google.android.youtube.HomeActivity",
    "whatsapp": "am start -n com.whatsapp/.Main",
    "discord": "am start -n com.discord/.main.MainActivity",
    "instagram": "am start -n com.instagram.android/.activity.MainTabActivity",
    "firefox": "am start -n org.mozilla.firefox/.App",
    "chatgpt": "am start -n com.openai.chatgpt/.MainActivity",
    "insta": "am start -n com.instagram.android/.activity.MainTabActivity",
    "gpt": "am start -n com.openai.chatgpt/.MainActivity",
    "minecraft": "am start -n com.mojang.minecraftpe/com.mojang.minecraftpe.MainActivity",
    "mc": "am start -n com.mojang.minecraftpe/com.mojang.minecraftpe.MainActivity",
    "zarchiver": "am start -n ru.zdevs.zarchiver/ru.zdevs.zarchiver.ZArchiver",
    "za": "am start -n ru.zdevs.zarchiver/ru.zdevs.zarchiver.ZArchiver",
    "music": "am start -n com.musicplayer.player.mp3player.white/com.musicplayer.player.mp3player.white.activity.MainActivity",
    "musicplayer": "am start -n com.musicplayer.player.mp3player.white/com.musicplayer.player.mp3player.white.activity.MainActivity",

    "pinterest": "am start -n com.pinterest/com.pinterest.activity.PinterestActivity",
    "pin": "am start -n com.pinterest/com.pinterest.activity.PinterestActivity",

    "spck": "am start -n io.spck/io.spck.editor.EditorActivity",
    "editor": "am start -n io.spck/io.spck.editor.EditorActivity",

    "flixfox": "am start -n com.tenacious.flixfox/com.gxgx.daqiandy.ui.splash.SplashActivity",
    "flix": "am start -n com.tenacious.flixfox/com.gxgx.daqiandy.ui.splash.SplashActivity",
    "gmail": "am start -n com.google.android.gm/.ConversationListActivityGmail",

    "camera": "am start -a android.media.action.IMAGE_CAPTURE",

    "settings": "am start -a android.settings.SETTINGS",

    "clock": "am start -a android.intent.action.SHOW_ALARMS",

    "files": "am start -a android.intent.action.VIEW_DOWNLOADS",

    "playstore": "am start -n com.android.vending/com.google.android.finsky.activities.MainActivity",
    "play": "am start -n com.android.vending/com.google.android.finsky.activities.MainActivity",

    "minecraft": "am start -n com.mojang.minecraftpe/com.mojang.minecraftpe.MainActivity",
    "mc": "am start -n com.mojang.minecraftpe/com.mojang.minecraftpe.MainActivity",

    "zarchiver": "am start -n ru.zdevs.zarchiver/ru.zdevs.zarchiver.ZArchiver",
    "za": "am start -n ru.zdevs.zarchiver/ru.zdevs.zarchiver.ZArchiver",
}

def handle_command(command):

    cmd = command.lower().strip()

    if cmd.startswith("open "):
        app = cmd[5:]

        if app in APPS:
            os.system(APPS[app])
            return True

        print("Unknown app")
        return True

    if cmd.startswith("google "):
        query = urllib.parse.quote(command[7:])
        os.system(
            f'termux-open-url "https://www.google.com/search?q={query}"'
        )
        return True

    if cmd.startswith("youtube "):
        query = urllib.parse.quote(command[8:])
        os.system(
            f'termux-open-url "https://www.youtube.com/results?search_query={query}"'
        )
        return True
    if cmd == "apps":

            print("""
    Available Apps:

    youtube
    whatsapp
    discord
    instagram
    firefox
    chatgpt
    gmail
    camera
    settings
    clock
    files
    playstore
    minecraft
    zarchiver
    music
    pinterest
    spck
    flixfox
    """)

            return True

    return False
