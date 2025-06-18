import os, sys

def Compile(script,icon,console):
	if console==1:
		try:
			os.system(f'pyinstaller -a {script}')
			os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')
		except:
			if sys.platform=='win32':
				os.system('pip install pyinstaller')
				os.system(f'pyinstaller -a {script}')
				os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')
			else:
				try:
					os.system('pip3 install pyinstaller')
					os.system(f'pyinstaller -a {script}')
					os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')
				except:
					os.system('git clone https://github.com/pypa/pip')
					os.chdir('pip')
					os.system('python setup.py install')
					os.system('pip3 install pyinstaller')
					os.system(f'pyinstaller -a {script}')
					os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')

	elif console==0:
		try:
			os.system(f'pyinstaller -noconsole {script}')
			os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')
		except:
			if sys.platform=='win32':
				os.system('pip install pyinstaller')
				os.system(f'pyinstaller -noconsole {script}')
				os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')
			else:
				try:
					os.system('pip3 install pyinstaller')
					os.system(f'pyinstaller -noconsole {script}')
					os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')
				except:
					os.system('git clone https://github.com/pypa/pip')
					os.chdir('pip')
					os.system('python setup.py install')
					os.system('pip3 install pyinstaller')
					os.system(f'pyinstaller -noconsole {script}')
					os.system(f'pyinstaller --onefile --name {script} --windowed --icon {icon} {script}')

script_name=input('Enter path/filename of python script to compile:')
icon_name=input('Enter path/filename of icon : ')
console=int(input('COmpile with console or no console(1/0):'))

if str(console).lower()=='console' or str(console).lower()=='y' or str(console).lower()=='yes':console=1
elif str(console).lower()=='no console' or str(console).lower()=='n' or str(console).lower()=='no':console=0

try:
	print(f'compiling {script_name}......')
	Compile(script_name,icon_name,console)
	print(f'COMPILED {script_name} SUCCESSFULLY')
except:
	print('an error might have occured')

