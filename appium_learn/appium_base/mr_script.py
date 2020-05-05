from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

print("connect devices")
device = mr.waitForConnection(5 , '8BN0217622004127')

# print("install app")
# device.installPackage('C:\Users\\55077\Desktop\wandoujia.apk')

print('startactivity')
package = 'com.wandoujia.phoenix2'
activity = 'com.pp.assistant.activity.PPMainActivity'
p_a = package + '/' + activity
print(p_a)
device.startActivity(component = p_a)
mr.sleep(2)

print('touch the input')
device.touch(584,193,'DOWN_AND_UP')
mr.sleep(2)

print('input something')
device.type('AK4')
mr.sleep(2)

print('screenshort')
pic = device.takeSnapshot()
pic.writeToFile('C:\Users\\55077\Desktop\pic.png','png')
mr.sleep(2)
# cmp=com.wandoujia.phoenix2/com.pp.assistant.activity.PPMainActivity

