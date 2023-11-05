import json


def save():
	with open("data1.json", "a", encoding="utf-8") as f:
		f.write(json.dumps(data1, indent=4, ensure_ascii=False))

def load():
	with open("data1.json", "r", encoding="utf-8") as fh:
		newnote = fh.read()
	print(f"Все заметки: \n{newnote}")
	return newnote

def edit():
	with open("data1.json", 'r', encoding="utf-8") as fh:
		newnote = fh.read()
		newnote['Имя'] = 'Новая заметка'
		with open("data1.json", "a", encoding="utf-8") as f:
			f.write(json.dumps(newnote, indent=4, ensure_ascii=False))

edit()
load()