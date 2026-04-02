package com.yourname.nekopoc;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

public class MainHook implements IXposedHookLoadPackage {

    @Override
    public void handleLoadPackage(LoadPackageParam lpparam) throws Throwable {
        // Filter out everything except the target app
        if (!lpparam.packageName.equals("tw.nekomimi.nekogram")) {
            return;
        }

        XposedBridge.log("NekoPoC: Successfully injected into Nekogram");

        ClassLoader classLoader = lpparam.classLoader;

        try {
            // Hooking the 'a' method to return a specific string
            XposedHelpers.findAndHookMethod("uo5$a", classLoader, "a", new XC_MethodHook() {
                @Override
                protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                    XposedBridge.log("NekoPoC: a() called");
                    param.setResult("INSERT_YOUR_BOT_USERNAME_WITHOUT_@");
                }
            });

            XposedHelpers.findAndHookMethod("uo5$a", classLoader, "getId", new XC_MethodHook() {
                @Override
                protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                    XposedBridge.log("NekoPoC: getBotId() called");
                    param.setResult(INSERT_YOUR_BOT_ID);
                }
            });

        } catch (Throwable t) {
            // Catching and logging errors helps immensely with debugging obfuscated apps
            XposedBridge.log("NekoPoC Error: " + t.getMessage());
        }
    }
}