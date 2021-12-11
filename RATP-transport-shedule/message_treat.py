from datetime import datetime,timedelta
def message_erreur(message):
	message=message.split(' ')
	return f"Le {message[0]} {message[1]} n'est pas disponible pour le moment à l'arrêt {message[2]}."

def heure_cal(minute):
	try:
		return (datetime.now() + timedelta(minutes=int(minute))).strftime('%H:%M')
	except:
		return ''
def message_rep(types, code, station, message_dict):
	if 'SERVICE' in list(message_dict.values())[0][0] and 'SERVICE' in list(message_dict.values())[1][0]:
		return f'Le service est terminé pour le {types} {code}.'
	else:
		try:
			word0=list(message_dict.values())[0][0]+ ' vers ' +list(message_dict.keys())[0]
		except:
			pass
		try:
			word1=' à '+heure_cal(list(message_dict.values())[0][0][0:2]) if list(message_dict.values())[0][0][0:2].isnumeric()or list(message_dict.values())[0][0][0].isnumeric()else ''
		except:
			word1=""
		try:
			word2=' (prochain dans '+list(message_dict.values())[0][1] if list(message_dict.values())[0][1][0:2].isnumeric() or list(message_dict.values())[0][1][0].isnumeric()else list(message_dict.values())[0][1]
		except:
			word2=""
		try:
			word3=list(message_dict.values())[1][0]
		except:
			word3=""
		try:
			word4=list(message_dict.keys())[1]
		except:
			word4=""
		try:
			word5=' à '+heure_cal(list(message_dict.values())[1][0][0:2]) if list(message_dict.values())[1][0][0:2].isnumeric()or list(message_dict.values())[1][0][0].isnumeric() else ''
		except:
			word5=""
		try:
			word6=' (prochain dans '+ list(message_dict.values())[1][1] if list(message_dict.values())[1][1][0:2].isnumeric() or list(message_dict.values())[1][1][0].isnumeric() else list(message_dict.values())[0][1]
		except:
			word6=""
		finally:
			return ' '.join(f"{word0} {word1} {word2}) %% {word3} vers {word4} {word5}{word6})".split()).replace('%', '\n')


