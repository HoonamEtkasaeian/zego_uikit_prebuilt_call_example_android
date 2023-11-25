hiimport os
import json
import xml.etree.ElementTree as ET


class AndroidConfigChecker:
    def __init__(self) -> None:
        self._google_service_json_path = "./app/google-services.json"
        self._android_manifest_xml_path = "./app/src/main/AndroidManifest.xml"
        self._project_gradle_path = "./build.gradle"
        self._app_gradle_path = "./app/build.gradle"

    def start_check(self):
        if self.is_google_service_json_in_right_location():
            print("✅ The google-service.json is in the right location.")
            if self.is_google_service_json_match_package_name():
                print("✅ The package name matches google-service.json.")
            else:
                print("❌ The package name does NOT match google-service.json.")
        else:
            print("❌ The google-service.json is NOT in the right location.")
        if self.is_project_gradle_correct():
            print("✅ The project level gradle file is ready.")
        else:
            print("❌ Missing dependencies in project-level gradle file.")
        if self.is_app_gradle_plugin_correct():
            print("✅ The plugin config in the app-level gradle file is correct.")
        else:
            print("❌ Missing com.google.gms.google-services plugin in the app-level gradle file.")
        if self.is_app_gradle_firebase_dependencies_correct():
            print("✅ Firebase dependencies config in the app-level gradle file is correct.")
        else:
            print("❌ Missing com.google.firebase:firebase-bom dependencies in the app-level gradle file.")

    def is_google_service_json_in_right_location(self):
        gs_path = os.path.abspath(self._google_service_json_path)
        return os.path.exists(gs_path)

    def is_google_service_json_match_package_name(self):
        gs_path = os.path.abspath(self._google_service_json_path)
        package_name_list = []
        with open(gs_path) as json_file:
            data = json.load(json_file)
            client = data['client']
            for c in client:
                package_name = c["client_info"]["android_client_info"]["package_name"]
                package_name_list.append(package_name)

        android_manifest_root = ET.parse(self._android_manifest_xml_path).getroot()
        project_package_name = android_manifest_root.get("package")

        return project_package_name in package_name_list

    def is_project_gradle_correct(self):
        with open(os.path.abspath(self._project_gradle_path)) as file:
            content = file.read()
            if "com.google.gms:google-services:" in content:
                return True
        return False

    def is_app_gradle_plugin_correct(self):
        with open(os.path.abspath(self._app_gradle_path)) as file:
            content = file.read()
            if "com.google.gms.google-services" in content:
                return True
        return False

    def is_app_gradle_firebase_dependencies_correct(self):
        with open(os.path.abspath(self._app_gradle_path)) as file:
            content = file.read()
            if "com.google.firebase:firebase-bom" in content:
                return True
        return False
        
    def is_app_gradle_firebase_messaging_dependencies_correct(self):
        with open(os.path.abspath(self._app_gradle_path)) as file:
            content = file.read()
            if "com.google.firebase:firebase-messaging:" in content:
                return True
        return False
    
      
if __name__ == "__main__":
    android_checker = AndroidConfigChecker()
    android_checker.start_check()
    public class MainActivity extends AppCompatActivity {
    long appID = YourAppID;
    String appSign = YourAppSign;
    String userID = "userID";
    String userName = "userName";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initSendCallInvitationButton();
        initCallInviteService();
    }

    public void initCallInviteService() {
      ZegoUIKitPrebuiltCallInvitationConfig callInvitationConfig = new ZegoUIKitPrebuiltCallInvitationConfig(ZegoSignalingPlugin.getInstance());
      //Change notifyWhenAppRunningInBackgroundOrQuit to false if you don't need to receive a call invitation notification while your app running in the background or quit.
      callInvitationConfig.notifyWhenAppRunningInBackgroundOrQuit = true;
      //This property needs to be set when you are building an Android app and when the notifyWhenAppRunningInBackgroundOrQuit is true. notificationConfig.channelID must be the same as the FCM Channel ID in ZEGOCLOUD Admin Console, and the notificationConfig.channelName can be an arbitrary value. The notificationConfig.soundmust be the same as the FCM sound in Admin Console either.
      ZegoNotificationConfig notificationConfig = new ZegoNotificationConfig();
      notificationConfig.sound = "zego_uikit_sound_call";
      notificationConfig.channelID = "CallInvitation";
      notificationConfig.channelName = "CallInvitation";
      ZegoUIKitPrebuiltCallInvitationService.init(getApplication(), appID, appSign, userID, userName,callInvitationConfig);
    }

    private void initSendCallInvitationButton(){
        String targetUserID = ; // The ID of the user you want to call.
        Context context = ; // Android context.

        ZegoSendCallInvitationButton button = new ZegoSendCallInvitationButton(context);
        //	If true, a video call is made when the button is pressed. Otherwise, a voice call is made.
        button.setIsVideoCall(true);
        //resourceID can be used to specify the ringtone of an offline call invitation, which must be set to the same value as the Push Resource ID in ZEGOCLOUD Admin Console. This only takes effect when the notifyWhenAppRunningInBackgroundOrQuit is true.
        button.setResourceID("zego_uikit_call");
        button.setInvitees(Collections.singletonList(new ZegoUIKitUser(targetUserID)));
    }
    }
