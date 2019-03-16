from sportsreference.nba.schedule import Schedule
import datetime

def get_boston_three():
	sched = Schedule('BOS')
	# sched[-3:] should be last three games of season
	# today is 2019-03-15
	# these are the past three games played rather than last of season
	# prints 2019-03-09, 2019-03-11, 2019-03-14
	for game in sched[-3:]: 
		print(game.date)

	# celtics play wizards on 2019-04-09
	celtics_last_game = "2019-04-09"
	all_dates = [game.date for game in sched]
	assert celtics_last_game in all_dates

def get_date():
	return datetime.datetime.today().strftime('%Y-%m-%d')





get_boston_three()
