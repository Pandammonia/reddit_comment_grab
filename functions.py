from datetime import datetime
import tkinter as tk

try:
	from login_id import *
except ImportError:
	pass

def grabusercomments(user):
	with open(f"{user}.txt", "w") as file:
		for comment in reddit.redditor(name=user).comments.new(limit=None):
			try:
				file.write(comment.body)
			except UnicodeEncodeError:
				pass

def grabuserscomments(*users):
	for user in users:
		with open(f"{user}.txt", "w") as file:
			for comment in reddit.redditor(name=user).comments.new(limit=None):
				try:
					file.write(comment.body)
				except UnicodeEncodeError:
					pass

def wordsplit(file):
	data = file.read()
	words = data.split()
	return words

def freq(string):
	string = string.split()
	string2 = []
	for word in string:
		if word not in string2:
			string2.append(word)
	for x in range(0, len(string2)):
		if string.count(string2[x]) < 5:
			pass
		else:
			print(f"{string2[x]} appears", string.count(string2[x]), "times.")



def usergrabbutton():
	username = entrybox.get()
	grabusercomments(username)

root = tk.Tk()
root.title('Reddit comment grab')
frm_window = tk.Frame(master = root)
entrytitle = tk.Label(master=frm_window,text="Username:")
entrytitle.grid(row=0, column=0, sticky="e")
entrybox = tk.Entry(master=frm_window)
entrybox.grid(row=0, column=1, sticky="w")
entrysubmit = tk.Button(master=frm_window,text="Submit!", command=usergrabbutton)
entrysubmit.grid(row=0, column=2)
frm_window.grid(row=0, column=0)


root.mainloop()