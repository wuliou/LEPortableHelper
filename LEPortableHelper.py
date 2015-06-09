import xml.etree.ElementTree as ET
import os

profiles = None
selected_profile = None
runnable_path = ''

def welcome_message():
	print 'LEPortableHelper, using Locale Emulator without install it.'
	print ''

def profile_not_exist_message():
	print 'The LEConfig.xml file dose not exist.'
	print ' -Did you put LEPortableHelper at the same folder as LEConfig.xml?'
	print ' -Have you install and uninstall Locale Emulator first?'

def load_xml():
	print 'Loading LE profiles...'
	tree = ET.parse('LEConfig.xml')
	root = tree.getroot()
	global profiles
	profiles = root[0]
	list_all_profiles()

def list_all_profiles():
	print 'Profiles found:'
	profile_index = 0
	for profile in profiles:
		print '- [' + str(profile_index) + ']' + profile.attrib['Name']
		profile_index+=1

def ask_select_profile():
	print 'Please select a LE profile setting:',
	print ''
	user_selected_profile_index = int(raw_input())
	global selected_profile
	selected_profile = profiles[user_selected_profile_index]
	output_message = 'Profile  \"'
	output_message += str(selected_profile.attrib['Name'])
	output_message += '\"  has been selected.'
	print output_message

def ask_runnable():
	global runnable_path
	print 'Please input path of the executable file:'
	runnable_path = raw_input()
	if ' ' in runnable_path:
		runnable_path = '\"' + runnable_path + '\"'

def script_maker():
	exe = 'LEProc.exe -runas'
	profile_id = selected_profile.attrib['Guid']
	return exe + ' ' + profile_id + ' ' + runnable_path

def save_to_file(cmd):
	print 'Saving to \"script.bat\" ...'
	with open('script.bat', 'wb') as f:
		f.write(cmd)
	print 'Saved.'

def run_now(cmd):
	print 'Start running...'
	os.system(cmd)

def ask_run_or_save():
	print 'Save to BAT file or run now?'
	print '- [0] Save to \"script.bat\" (overwrite!)'
	print '- [1] Run it now'
	return raw_input()

if __name__ == '__main__':
	welcome_message()
	try:
		load_xml()
	except:
		profile_not_exist_message()
		raw_input('Press [Enter] to exit.')
		exit()
	while(True):
		try:
			ask_select_profile()
			break
		except:
			print 'Such profile not exist.'
			list_all_profiles()
	ask_runnable()
	cmd = script_maker()
	while(True):
		user_option = ask_run_or_save()
		if user_option == '0':
			save_to_file(cmd)
			break
		elif user_option == '1':
			run_now(cmd)
			break
		else:
			continue
