[app]

# Title of your application
title = Zen Invoice

# Package name (no spaces or special characters)
package.name = zeninvoice

# Package domain
package.domain = com.zenkeep

# Source directory
source.dir = .

# Include your HTML and asset files
source.include_exts = py,png,jpg,json,html,js,css

# Application requirements (Kivy + Pyjnius for Android WebView hooks)
requirements = python3,kivy,pyjnius

# Supported orientations (portrait or landscape)
orientation = portrait

# Fullscreen mode (0 = show status bar, 1 = immersive fullscreen)
fullscreen = 0

# Android specific settings (INTERNET is mandatory to load Tailwind/Fonts CDN)
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
