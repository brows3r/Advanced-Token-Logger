import winreg
import os

print("Scanning Registry...")
print("Scanning Registry...")
print("Done.")

# CurrentVersion

print(''' 
Information from SOFTWARE\Microsoft\Windows NT\CurrentVersion
---------------------------------------------------------------''')

def reg():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break
reg()

print(''' 

''')


# Environment

print(''' 
Information from \Environment
---------------------------------------------------------------''')

def reg1():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)

	regkey = winreg.OpenKey(access_reg, r"Environment")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break
reg1()


print(''' 

''')


# HKEY_CURRENT_USER\Volatile

print(''' 
Information from HKEY_CURRENT_USER\Volatile Environment
---------------------------------------------------------------''')

def reg2():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)

	regkey = winreg.OpenKey(access_reg, r"Volatile Environment")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break
reg2()


print(''' 

''')


# SOFTWARE\Microsoft\Windows NT\CurrentVersion\networkcards\3

print(''' 
Information from SOFTWARE\Microsoft\Windows NT\CurrentVersion\networkcards\3
------------------------------------------------------------------------------''')

def reg3():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\networkcards\3")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break
reg3()


print(''' 

''')


# HARDWARE\DESCRIPTION\SYSTEM

print(''' 
Information from HARDWARE\DESCRIPTION\SYSTEM
---------------------------------------------------------------''')

def reg4():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"HARDWARE\DESCRIPTION\SYSTEM")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break
reg4()


print(''' 

''')


# SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform


print(''' 
Information from SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform
---------------------------------------------------------------''')

def reg5():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break
reg5()

print(''' 

''')

# \SOFTWARE\Microsoft\Windows Defender

print(''' 
Information from \SOFTWARE\Microsoft\Windows Defender
---------------------------------------------------------------''')

def reg6():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break
reg6()



os.system("py registry.py > Files\RegistryInfo.txt")