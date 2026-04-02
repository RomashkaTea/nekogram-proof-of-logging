# Nekogram-logging-proofs

A proof of Nekogram collecting phone numbers

# Requirements
- A rooted Android device
- LSPosed 

# How to reproduce

1. Run the bot (python3 bot.py)
2. Insert your bot ID and username in module/app/src/main/java/com/yourname/nekopoc/MainHook.java
3. Install it, activate, force stop Nekogram
4. Open the Nekogram app, make sure the module is working by checking logcat:
```adb logcat | grep Xposed``` 
5. Sign in to an account, check the bot logs.