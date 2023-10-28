# Importing necessary libraries
import requests

# Fetches the list of teams that participated in a given IPL season
def teamsPerSeason(season):
    response = requests.get('http://127.0.0.1:5000/api/teamsperseason?season={}'.format(season))
    return response.json()

# Fetches the list of teams that played against a given team
def teamsPerTeam(team):
    response = requests.get('http://127.0.0.1:5000/api/teamsperteam?team={}'.format(team))
    return response.json()

# Fetches the list of teams that played against a given team in a specific season
def teamsPerSeasonTeam(season, team):
    response = requests.get('http://127.0.0.1:5000/api/teamsperseasonteam?season={}&team={}'.format(season, team))
    return response.json()

# Fetches the list of batsmen across all IPL seasons
def batsmenPerAllSeasons():
    response = requests.get('http://127.0.0.1:5000/api/batsmenperallseasons')
    return response.json()

# Fetches the list of batsmen for a given IPL season
def batsmenPerSeason(season):
    response = requests.get('http://127.0.0.1:5000/api/batsmenperseason?season={}'.format(season))
    return response.json()

# Fetches the list of bowlers across all IPL seasons
def bowlersPerAllSeasons():
    response = requests.get('http://127.0.0.1:5000/api/bowlersperallseasons')
    return response.json()

# Fetches the list of bowlers for a given IPL season
def bowlersPerSeason(season):
    response = requests.get('http://127.0.0.1:5000/api/bowlersperseason?season={}'.format(season))
    return response.json()

# Fetches the overall stats/data for all IPL seasons
def overallAllSeasons():
    response = requests.get('http://127.0.0.1:5000/api/allseasons')
    return response.json()

# Fetches the stats/data for a given IPL season
def overallSeason(season):
    response = requests.get('http://127.0.0.1:5000/api/season?season={}'.format(season))
    return response.json()

# Fetches the stats/data of a given team across all IPL seasons
def teamAllSeasons(team):
    response = requests.get('http://127.0.0.1:5000/api/teamallseasons?team={}'.format(team))
    return response.json()

# Fetches the stats/data of a given team for a specific IPL season
def teamSeason(team, season):
    response = requests.get('http://127.0.0.1:5000/api/teamseason?team={}&season={}'.format(team, season))
    return response.json()

# Fetches the head-to-head stats/data between two teams across all IPL seasons
def teamVsTeamAllSeasons(team1, team2):
    response = requests.get('http://127.0.0.1:5000/api/teamvsteamallseasons?team1={}&team2={}'.format(team1, team2))
    return response.json()

# Fetches the head-to-head stats/data between two teams for a specific IPL season
def teamVsTeamSeason(team1, team2, season):
    response = requests.get('http://127.0.0.1:5000/api/teamvsteamseason?team1={}&team2={}&season={}'.format(team1, team2, season))
    return  response.json()

# Fetches the stats/data of a given batsman across all IPL seasons
def batsmanAllSeasons(batsman):
    response = requests.get('http://127.0.0.1:5000/api/batsmanallseasons?batsman={}'.format(batsman))
    return response.json()

# Fetches the stats/data of a given batsman for a specific IPL season
def batsmanSeason(batsman, season):
    response = requests.get('http://127.0.0.1:5000/api/batsmanseason?batsman={}&season={}'.format(batsman, season))
    return response.json()

# Fetches the stats/data of a given bowler across all IPL seasons
def bowlerAllSeasons(bowler):
    response = requests.get('http://127.0.0.1:5000/api/bowlerallseasons?bowler={}'.format(bowler))
    return response.json()

# Fetches the stats/data of a given bowler for a specific IPL season
def bowlerSeason(bowler, season):
    response = requests.get('http://127.0.0.1:5000/api/bowlerseason?bowler={}&season={}'.format(bowler, season))
    return response.json()