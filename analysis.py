# Importing necessary libraries and modules
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import api

# Fetches the list of teams that participated in a given IPL season
def teamsPerSeason(season):
    data = api.teamsPerSeason(season)
    return data['teamsPerSeason']['teams']

# Fetches the list of teams that played against a given team
def teamsPerTeam(team):
    data = api.teamsPerTeam(team)
    return data['teamsPerTeam']['teams']

# Fetches the list of teams that played against a given team in a specific season
def teamsPerSeasonTeam(season, team):
    data = api.teamsPerSeasonTeam(season, team)
    return data['teamsPerSeasonTeam']['teams']

# Fetches the list of batsmen across all IPL seasons
def batsmenPerAllSeasons():
    data = api.batsmenPerAllSeasons()
    return data['batsmenPerAllSeasons']['batsmenNames']

# Fetches the list of batsmen for a given IPL season
def batsmenPerSeason(season):
    data = api.batsmenPerSeason(season)
    return data['batsmenPerSeason']['batsmenNames']

# Fetches the list of bowlers across all IPL seasons
def bowlersPerAllSeasons():
    data = api.bowlersPerAllSeasons()
    return data['bowlersPerAllSeasons']['bowlersNames']

# Fetches the list of bowlers for a given IPL season
def bowlersPerSeason(season):
    data = api.bowlersPerSeason(season)
    return data['bowlersPerSeason']['bowlersNames']


# Fetches and visualizes overall IPL data spanning all seasons
def overallAllSeasons():
    # Retrieving data from API
    data = api.overallAllSeasons()

    # Setting the title for the data visualization section
    st.title('All Seasons Analysis')

    # Adding a divider for aesthetic separation
    st.divider()

    # Creating three side-by-side columns to display total seasons, teams, and matches played
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Total Seasons Played', data['overallAllSeasons']['totalSeasonsPlayed'])

    with col2:
        st.metric('Total Teams Played', data['overallAllSeasons']['totalTeamsPlayed'])

    with col3:
        st.metric('Total Matches Played', data['overallAllSeasons']['totalMatchesPlayed'])

    # Creating four side-by-side columns for highest runs, wickets, team score and lowest team score
    col4, col5, col6, col7 = st.columns(4)

    # Function to convert full team names into abbreviations
    def sortname_conveter(name):
        l = []
        for i in name.split(' '):
            l.append(i[0])
        return ''.join(l)

    with col4:
        st.metric('Highest Runs', data['overallAllSeasons']['highestRunsBatsmanName'], str(data['overallAllSeasons']['highestRuns']) + ' runs')

    with col5:
        st.metric('Highest Wickets', data['overallAllSeasons']['highestWicketsBowlerName'], str(data['overallAllSeasons']['highestWickets']) + ' wickets')

    with col6:
        team_name = sortname_conveter(data['overallAllSeasons']['highesTeamScoreName'])
        st.metric('Highest Team Score', team_name, str(data['overallAllSeasons']['highesTeamScore']) + ' runs')

    with col7:
        team_name = sortname_conveter(data['overallAllSeasons']['lowestTeamScoreName'])
        st.metric('Lowest Team Score', team_name, str(data['overallAllSeasons']['lowestTeamScore']) + ' runs')

    # Adding another divider for separation
    st.divider()

    # Displaying a list of teams
    st.subheader('Teams')
    st.table(pd.DataFrame(data['overallAllSeasons']['teams']['names'], columns=['Team Name'], index=range(1, len(data['overallAllSeasons']['teams']['names']) + 1)))

    st.divider()

    # Creating two side-by-side columns to display top 5 batsmen and bowlers
    col8, col9 = st.columns(2)

    with col8:
        st.subheader('Top Batsmen')
        st.table(pd.DataFrame(list(
            zip(data['overallAllSeasons']['top5Batsmen']['names'], data['overallAllSeasons']['top5Batsmen']['runs'])), columns=['Batsman Name', 'Batsman Runs'], index=[1, 2, 3, 4, 5]))

    with col9:
        st.subheader('Top Bowlers')
        st.table(pd.DataFrame(list(zip(data['overallAllSeasons']['top5Bowlers']['names'], data['overallAllSeasons']['top5Bowlers']['wickets'])), columns=['Bowler Name', 'Bowler Wickets'], index=[1, 2, 3, 4, 5]))

    st.divider()

    # Displaying a bar chart for winning teams across seasons
    st.subheader('Winning Teams')

    trace = go.Bar(x=data['overallAllSeasons']['winningTeams']['names'], y=data['overallAllSeasons']['winningTeams']['titles'], marker={'color': 'blue'})
    data = [trace]
    layout = go.Layout(xaxis={'title': 'Teams'}, yaxis={'title': 'Titles'})

    fig = go.Figure(data, layout)
    fig.update_xaxes(tickangle=20)

    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for a specific season
def overallSeason(season):
    # Retrieve data for the specific season from the API
    data = api.overallSeason(season)

    # Set the title for the data visualization section for the specific season
    st.title('{} Season Analysis'.format(season))

    # Add a divider for aesthetic separation
    st.divider()

    # Creating three side-by-side columns to display total matches, teams, and super overs for the season
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Total Matches Played', data['overallSeason']['totalMatchesPlayed'])

    with col2:
        st.metric('Total Teams Played', data['overallSeason']['totalTeamsPlayed'])

    with col3:
        st.metric('Total Superovers Played', data['overallSeason']['totalSuperOverPlayed'])

    # Creating four side-by-side columns to display highest runs, wickets, team score and lowest team score for the season
    col4, col5, col6, col7 = st.columns(4)

    # Function to convert full team names into abbreviations
    def sortname_conveter(name):
        l = []
        for i in name.split(' '):
            l.append(i[0])
        return ''.join(l)

    with col4:
        st.metric('Highest Runs', data['overallSeason']['highestRunsBatsmanName'], str(data['overallSeason']['highestRuns']) + ' runs')

    with col5:
        st.metric('Highest Wickets', data['overallSeason']['highestWicketsBowlerName'], str(data['overallSeason']['highestWickets']) + ' wickets')

    with col6:
        team_name = sortname_conveter(data['overallSeason']['highesTeamScoreName'])
        st.metric('Highest Team Score', team_name, str(data['overallSeason']['highesTeamScore']) + ' runs')

    with col7:
        team_name = sortname_conveter(data['overallSeason']['lowestTeamScoreName'])
        st.metric('Lowest Team Score', team_name, str(data['overallSeason']['lowestTeamScore']) + ' runs')

    # Add another divider for separation
    st.divider()

    # Displaying a list of teams that played in the specific season
    st.subheader('Playing Teams')
    st.table(pd.DataFrame(data['overallSeason']['playingTeams']['names'], columns=['Team Name'], index=range(1, data['overallSeason']['totalTeamsPlayed'] + 1)))

    st.divider()

    # Creating two side-by-side columns to display top 5 batsmen and bowlers for the season
    col8, col9 = st.columns(2)

    with col8:
        st.subheader('Top Batsmen')
        st.table(pd.DataFrame(
            list(zip(data['overallSeason']['top5Batsmen']['names'], data['overallSeason']['top5Batsmen']['runs'])), columns=['Batsman Name', 'Batsman Runs'], index=[1, 2, 3, 4, 5]))

    with col9:
        st.subheader('Top Bowlers')
        st.table(pd.DataFrame(
            list(zip(data['overallSeason']['top5Bowlers']['names'], data['overallSeason']['top5Bowlers']['wickets'])), columns=['Bowler Name', 'Bowler Wickets'], index=[1, 2, 3, 4, 5]))

    st.divider()

    # Displaying the winning team of the season
    st.subheader('Winning Team')
    st.success(data['overallSeason']['winningTeam'])

# Function to fetch and visualize IPL data for a specific team spanning all seasons
def teamAllSeasons(team):
    # Retrieve overall data for the team across all seasons from the API
    data = api.teamAllSeasons(team)

    # Set the title for the visualization section
    st.title('All Seasons Analysis')

    # Add a divider for aesthetic separation
    st.divider()

    # Creating three side-by-side columns to display total seasons, matches, and titles for the team
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Total Seasons Played', data['teamAllSeasons']['totalSeasonsPlayed'])

    with col2:
        st.metric('Total Matches Played', data['teamAllSeasons']['totalMatchesPlayed'])

    with col3:
        st.metric('Total Titles Won', data['teamAllSeasons']['totalTitlesWon'])

    # Creating four side-by-side columns to display team's highest runs, wickets, team score and lowest team score across seasons
    col4, col5, col6, col7 = st.columns(4)

    # Function to convert full team names into abbreviations
    def sortname_conveter(name):
        l = []
        for i in name.split(' '):
            l.append(i[0])
        return ''.join(l)

    with col4:
        st.metric('Highest Runs', data['teamAllSeasons']['highestRunsBatsmanName'], str(data['teamAllSeasons']['highestRuns']) + ' runs')

    with col5:
        st.metric('Highest Wickets', data['teamAllSeasons']['highestWicketsBowlerName'], str(data['teamAllSeasons']['highestWickets']) + ' wickets')

    with col6:
        team_name = sortname_conveter(data['teamAllSeasons']['highesScoreName'])
        st.metric('Highest Score', team_name, str(data['teamAllSeasons']['highesScore']) + ' runs')

    with col7:
        team_name = sortname_conveter(data['teamAllSeasons']['lowestScoreName'])
        st.metric('Lowest Score', team_name, str(data['teamAllSeasons']['lowestScore']) + ' runs')

    # Add another divider for separation
    st.divider()

    # Displaying top 5 batsmen and bowlers for the team across all seasons in two side-by-side columns
    col8, col9 = st.columns(2)

    with col8:
        st.subheader('Top Batsmen')
        st.table(pd.DataFrame(
            list(zip(data['teamAllSeasons']['top5Batsmen']['names'], data['teamAllSeasons']['top5Batsmen']['runs'])), columns=['Batsman Name', 'Batsman Runs'], index=[1, 2, 3, 4, 5]))

    with col9:
        st.subheader('Top Bowlers')
        st.table(pd.DataFrame(
            list(zip(data['teamAllSeasons']['top5Bowlers']['names'], data['teamAllSeasons']['top5Bowlers']['wickets'])), columns=['Bowler Name', 'Bowler Wickets'], index=[1, 2, 3, 4, 5]))

    # Add another divider
    st.divider()

    # Displaying win-loss-draw percentage for the team using a pie chart
    st.subheader('Win-Loss Percentage')

    lables = ['Win', 'Loss', 'Draw']
    trace = go.Pie(labels=lables, values=[data['teamAllSeasons']['matchesWinDrawLoss']['matchesWon'], data['teamAllSeasons']['matchesWinDrawLoss']['matchesLoss'], data['teamAllSeasons']['matchesWinDrawLoss']['matchesDraw']])
    data = [trace]
    layout = go.Layout()

    fig = go.Figure(data, layout)
    fig.update_xaxes(tickangle=20)
    fig.update_traces(textinfo='value+percent')

    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for a specific team during a particular season
def teamSeason(team, season):
    # Fetch data for the given team and season using the API
    data = api.teamSeason(team, season)

    # Display title for the Streamlit app
    st.title('{} Season Analysis'.format(season))

    # Add a visual divider for clarity
    st.divider()

    # Create three side-by-side columns to display metrics for matches played, superovers, and titles won
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Total Matches Played', data['teamSeason']['totalMatchesPlayed'])

    with col2:
        st.metric('Total Superovers Played', data['teamSeason']['totalSuperOverPlayed'])

    with col3:
        # Check if the team won any titles and display it
        if data['teamSeason']['titlesWon']:
            st.metric('Titles Won', 'Yes')
        else:
            st.metric('Titles Won', 'No')

    # Create columns for displaying top players and scores
    col4, col5, col6, col7 = st.columns(4)

    # Utility function to convert full team names into their abbreviations for brevity
    def sortname_conveter(name):
        return ''.join([i[0] for i in name.split(' ')])

    with col4:
        st.metric('Highest Runs', data['teamSeason']['highestRunsBatsmanName'], str(data['teamSeason']['highestRuns']) + ' runs')

    with col5:
        st.metric('Highest Wickets', data['teamSeason']['highestWicketsBowlerName'], str(data['teamSeason']['highestWickets']) + ' wickets')

    with col6:
        team_name = sortname_conveter(data['teamSeason']['highesScoreName'])
        st.metric('Highest Score', team_name, str(data['teamSeason']['highesScore']) + ' runs')

    with col7:
        team_name = sortname_conveter(data['teamSeason']['lowestScoreName'])
        st.metric('Lowest Score', team_name, str(data['teamSeason']['lowestScore']) + ' runs')

    # Add another visual divider
    st.divider()

    # Display list of players for the team
    st.subheader('Team Players')
    st.table(pd.DataFrame(data['teamSeason']['players']['names'], columns=['Players Name'], index=range(1, len(data['teamSeason']['players']['names']) + 1)))

    # Another visual divider
    st.divider()

    # Create two columns for displaying top batsmen and bowlers for the season
    col8, col9 = st.columns(2)

    with col8:
        st.subheader('Top Batsmen')
        st.table(pd.DataFrame(list(zip(data['teamSeason']['top5Batsmen']['names'], data['teamSeason']['top5Batsmen']['runs'])), columns=['Batsman Name', 'Batsman Runs'], index=[1, 2, 3, 4, 5]))

    with col9:
        st.subheader('Top Bowlers')
        st.table(pd.DataFrame(list(zip(data['teamSeason']['top5Bowlers']['names'], data['teamSeason']['top5Bowlers']['wickets'])), columns=['Bowler Name', 'Bowler Wickets'], index=[1, 2, 3, 4, 5]))

    # Visual divider
    st.divider()

    # Pie chart visualization to display win-loss-draw distribution for the team during the season
    st.subheader('Win-Loss Percentage')

    labels = ['Win', 'Loss', 'Draw']
    trace = go.Pie(labels=labels, values=[data['teamSeason']['matchesWinDrawLoss']['matchesWon'], data['teamSeason']['matchesWinDrawLoss']['matchesLoss'], data['teamSeason']['matchesWinDrawLoss']['matchesDraw']])

    fig = go.Figure(data=[trace])
    fig.update_xaxes(tickangle=20)
    fig.update_traces(textinfo='value+percent')
    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for the two teams across all seasons
def teamVsTeamAllSeasons(team1, team2):
    # Retrieve overall data for the two teams across all seasons from the API
    data = api.teamVsTeamAllSeasons(team1, team2)

    # Display title for the Streamlit app
    st.title('All Seasons Analysis')

    # Add a visual divider for clarity
    st.divider()

    # Create three side-by-side columns to display metrics for seasons played, matches played, and super overs
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Total Seasons Played', data['teamVsTeamAllSeasons']['totalSeasonsPlayed'])

    with col2:
        st.metric('Total Matches Played', data['teamVsTeamAllSeasons']['totalMatchesPlayed'])

    with col3:
        st.metric('Total Superovers Played', data['teamVsTeamAllSeasons']['totalSuperOversPlayed'])

    # Utility function to convert full team names into their abbreviations for brevity
    def sortname_conveter(name):
        return ''.join([i[0] for i in name.split(' ')])

    # Create columns to display top performers and scores between the two teams
    col4, col5, col6, col7 = st.columns(4)

    with col4:
        st.metric('Highest Runs', data['teamVsTeamAllSeasons']['highestRunsBatsmanName'], str(data['teamVsTeamAllSeasons']['highestRuns']) + ' runs')

    with col5:
        st.metric('Highest Wickets', data['teamVsTeamAllSeasons']['highestWicketsBowlerName'], str(data['teamVsTeamAllSeasons']['highestWickets']) + ' wickets')

    with col6:
        team_name = sortname_conveter(data['teamVsTeamAllSeasons']['highesScoreName'])
        st.metric('Highest Score', team_name, str(data['teamVsTeamAllSeasons']['highesScore']) + ' runs')

    with col7:
        team_name = sortname_conveter(data['teamVsTeamAllSeasons']['lowestScoreName'])
        st.metric('Lowest Score', team_name, str(data['teamVsTeamAllSeasons']['lowestScore']) + ' runs')

    # Add another visual divider
    st.divider()

    # Create columns to display top batsmen and bowlers between the two teams
    col8, col9 = st.columns(2)

    with col8:
        st.subheader('Top Batsmen')
        st.table(pd.DataFrame(list(zip(data['teamVsTeamAllSeasons']['top5Batsmen']['names'], data['teamVsTeamAllSeasons']['top5Batsmen']['runs'])), columns=['Batsman Name', 'Batsman Runs'], index=[1, 2, 3, 4, 5]))

    with col9:
        st.subheader('Top Bowlers')
        st.table(pd.DataFrame(list(zip(data['teamVsTeamAllSeasons']['top5Bowlers']['names'], data['teamVsTeamAllSeasons']['top5Bowlers']['wickets'])), columns=['Bowler Name', 'Bowler Wickets'], index=[1, 2, 3, 4, 5]))

    # Visual divider
    st.divider()

    # Pie chart visualization to display the win distribution between the two teams across all seasons
    st.subheader('Winning Percentage')

    labels = ['Won By {}'.format(sortname_conveter(data['teamVsTeamAllSeasons']['teamsName']['team1Name'])), 'Won By {}'.format(sortname_conveter(data['teamVsTeamAllSeasons']['teamsName']['team2Name'])), 'Draw']
    trace = go.Pie(labels=labels, values=[data['teamVsTeamAllSeasons']['matchesWinDraw']['matchesWonByTeam1'], data['teamVsTeamAllSeasons']['matchesWinDraw']['matchesWonByTeam2'], data['teamVsTeamAllSeasons']['matchesWinDraw']['matchesDraw']])

    fig = go.Figure(data=[trace])
    fig.update_xaxes(tickangle=20)
    fig.update_traces(textinfo='value+percent')
    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for the two teams for a particular season
def teamVsTeamSeason(team1, team2, season):
    # Fetch data for the given two team for a particular season using the API
    data = api.teamVsTeamSeason(team1, team2, season)

    # Set the title for the Streamlit dashboard
    st.title('{} Season Analysis'.format(season))

    # Insert a visual divider for clarity
    st.divider()

    # Create two columns for displaying match and superover metrics
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Total Matches Played', data['teamVsTeamSeason']['totalMatchesPlayed'])

    with col2:
        st.metric('Total Superovers Played', data['teamVsTeamSeason']['totalSuperOversPlayed'])

    # Create columns for top performers and scores for the match-up in the season
    col3, col4, col5, col6 = st.columns(4)

    # Utility function to create short team names from their full names for brevity
    def sortname_conveter(name):
        return ''.join([i[0] for i in name.split(' ')])

    # Display performance metrics using short names
    with col3:
        st.metric('Highest Runs', data['teamVsTeamSeason']['highestRunsBatsmanName'], str(data['teamVsTeamSeason']['highestRuns']) + ' runs')
    with col4:
        st.metric('Highest Wickets', data['teamVsTeamSeason']['highestWicketsBowlerName'], str(data['teamVsTeamSeason']['highestWickets']) + ' wickets')
    with col5:
        team_name = sortname_conveter(data['teamVsTeamSeason']['highesScoreName'])
        st.metric('Highest Score', team_name, str(data['teamVsTeamSeason']['highesScore']) + ' runs')
    with col6:
        team_name = sortname_conveter(data['teamVsTeamSeason']['lowestScoreName'])
        st.metric('Lowest Score', team_name, str(data['teamVsTeamSeason']['lowestScore']) + ' runs')

    # Visual divider
    st.divider()

    # Display the players from each team
    col7, col8 = st.columns(2)
    with col7:
        st.subheader('{} Players'.format(sortname_conveter(data['teamVsTeamSeason']['teamsName']['team1Name'])))
        st.table(pd.DataFrame(data['teamVsTeamSeason']['players']['team1Players'], columns=['Players Name'], index=range(1, len(data['teamVsTeamSeason']['players']['team1Players'])+1)))
    with col8:
        st.subheader('{} Players'.format(sortname_conveter(data['teamVsTeamSeason']['teamsName']['team2Name'])))
        st.table(pd.DataFrame(data['teamVsTeamSeason']['players']['team2Players'], columns=['Players Name'], index=range(1, len(data['teamVsTeamSeason']['players']['team2Players'])+1)))

    # Another visual divider
    st.divider()

    # Display top batsmen and bowlers of the match-up in the season
    col9, col10 = st.columns(2)
    with col9:
        st.subheader('Top Batsmen')
        st.table(pd.DataFrame(list(zip(data['teamVsTeamSeason']['top5Batsmen']['names'], data['teamVsTeamSeason']['top5Batsmen']['runs'])), columns=['Batsman Name', 'Batsman Runs'], index=[1, 2, 3, 4, 5]))
    with col10:
        st.subheader('Top Bowlers')
        st.table(pd.DataFrame(list(zip(data['teamVsTeamSeason']['top5Bowlers']['names'], data['teamVsTeamSeason']['top5Bowlers']['wickets'])), columns=['Bowler Name', 'Bowler Wickets'], index=[1, 2, 3, 4, 5]))

    # Insert a divider
    st.divider()

    # Create a pie chart to visualize the win distribution between the two teams in the season
    st.subheader('Winning Percentage')

    labels = ['Won By {}'.format(sortname_conveter(data['teamVsTeamSeason']['teamsName']['team1Name'])), 'Won By {}'.format(sortname_conveter(data['teamVsTeamSeason']['teamsName']['team2Name'])), 'Draw']
    trace = go.Pie(labels=labels, values=[data['teamVsTeamSeason']['matchesWinDraw']['matchesWonByTeam1'], data['teamVsTeamSeason']['matchesWinDraw']['matchesWonByTeam2'], data['teamVsTeamSeason']['matchesWinDraw']['matchesDraw']])

    fig = go.Figure(data=[trace])
    fig.update_xaxes(tickangle=20)
    fig.update_traces(textinfo='value+percent')
    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for the batsman across all seasons
def batsmanAllSeasons(batsman):
    # Fetch the performance details of the batsman across all seasons from the API
    data = api.batsmanAllSeasons(batsman)

    # Set the title for the Streamlit dashboard
    st.title('All Seasons Analysis')
    # Insert a visual divider for clarity
    st.divider()

    # Create five columns to display various batting metrics for the batsman
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display the number of seasons and matches played by the batsman
    with col1:
        st.metric('Total Seasons Played', data['batsmanAllSeasons']['totalSeasonsPlayed'])
    with col2:
        st.metric('Total Matches Played', data['batsmanAllSeasons']['totalMatchesPlayed'])

    # Display the total runs, fours and sixes hit by the batsman
    with col3:
        st.metric('Total Run', data['batsmanAllSeasons']['totalRuns'])
    with col4:
        st.metric('Fours/Sixes', str(data['batsmanAllSeasons']['totalFours']) + '/' + str(data['batsmanAllSeasons']['totalSixes']))

    # Display the number of fifties and centuries scored by the batsman
    with col5:
        st.metric('Fifties/Centuries', str(data['batsmanAllSeasons']['totalFifties']) + '/' + str(data['batsmanAllSeasons']['totalCenturies']))

    # Display other batting metrics like highest score, average, strike rate, and Man of the Match awards
    col6, col7, col8, col9 = st.columns(4)
    with col6:
        st.metric('Highest Score', data['batsmanAllSeasons']['highestScore'])
    with col7:
        st.metric('Average', data['batsmanAllSeasons']['average'])
    with col8:
        st.metric('Strike Rate', data['batsmanAllSeasons']['strikeRate'])
    with col9:
        st.metric('Total MOM', data['batsmanAllSeasons']['totalMOM'])

    # Insert a divider for visual clarity
    st.divider()

    # Display the current team the batsman is playing in
    st.subheader('Playing In')
    st.success(data['batsmanAllSeasons']['playingIn'])

    # Insert another divider
    st.divider()

    # If the batsman has played for more than one team, display those teams
    if data['batsmanAllSeasons']['playedIn']['teams']:
        st.subheader('Played In')
        st.table(pd.DataFrame(data['batsmanAllSeasons']['playedIn']['teams'], columns=['Team Name'], index=range(1, len(data['batsmanAllSeasons']['playedIn']['teams']) + 1)))

        # Insert a divider
        st.divider()

    # Display a scatter plot for the batsman's runs across different seasons
    st.subheader('Season Wise Runs')

    trace = go.Scatter(x=data['batsmanAllSeasons']['seasonWiseRuns']['seasons'], y=data['batsmanAllSeasons']['seasonWiseRuns']['runs'])
    layout = go.Layout(xaxis={'title': 'Seasons'}, yaxis={'title': 'Runs'})

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_xaxes()
    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for the batsman for a particular season
def batsmanSeason(batsman, season):
    # Fetch the performance details of the batsman for a particular season from the API
    data = api.batsmanSeason(batsman, season)

    # Set the title for the Streamlit dashboard indicating the season being analyzed
    st.title('{} Season Analysis'.format(season))

    # Insert a visual divider for clarity
    st.divider()

    # Create four columns to display various batting metrics for the batsman for the specified season
    col1, col2, col3, col4 = st.columns(4)

    # Display the number of matches played, total runs scored, and fours/sixes hit
    with col1:
        st.metric('Total Matches Played', data['batsmanSeason']['totalMatchesPlayed'])
    with col2:
        st.metric('Total Run', data['batsmanSeason']['totalRuns'])
    with col3:
        st.metric('Fours/Sixes', str(data['batsmanSeason']['totalFours']) + '/' + str(data['batsmanSeason']['totalSixes']))

    # Display the number of fifties and centuries scored in the season
    with col4:
        st.metric('Fifties/Centuries', str(data['batsmanSeason']['totalFifties']) + '/' + str(data['batsmanSeason']['totalCenturies']))

    # Create another set of columns to display additional batting metrics
    col5, col6, col7, col8 = st.columns(4)

    # Display the highest score, batting average, strike rate, and number of Man of the Match awards in the season
    with col5:
        st.metric('Highest Score', data['batsmanSeason']['highestScore'])
    with col6:
        st.metric('Average', data['batsmanSeason']['average'])
    with col7:
        st.metric('Strike Rate', data['batsmanSeason']['strikeRate'])
    with col8:
        st.metric('Total MOM', data['batsmanSeason']['totalMOM'])

    # Insert a divider for visual clarity
    st.divider()

    # Display the current team the batsman played for in the season
    st.subheader('Playing In')
    st.success(data['batsmanSeason']['playingIn'])

    # Insert another divider
    st.divider()

    # Display the batsman's score against all teams in the season
    st.subheader('Score Against All Teams')
    st.table(pd.DataFrame(list(zip(data['batsmanSeason']['scoreAgainstAllTeams']['teams'], data['batsmanSeason']['scoreAgainstAllTeams']['runs'])), columns=['Team Name', 'Runs'], index=range(1, len(data['batsmanSeason']['scoreAgainstAllTeams']['teams']) + 1)))

    # Insert a divider
    st.divider()

    # Display a scatter plot of the batsman's runs across different matches in the season
    st.subheader('Matches Wise Runs')

    trace = go.Scatter(x=data['batsmanSeason']['seasonWiseRuns']['matches'], y=data['batsmanSeason']['seasonWiseRuns']['runs'])
    layout = go.Layout(xaxis={'title': 'Matches'}, yaxis={'title': 'Runs'})

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_xaxes()

    # Render the plotly chart on Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for the bowler across all seasons
def bowlerAllSeasons(bowler):
    # Fetch the performance details of the bowler across all seasons from the API
    data = api.bowlerAllSeasons(bowler)

    # Set the title for the Streamlit dashboard to indicate the analysis spans all seasons
    st.title('All Season Analysis')

    # Insert a visual divider for clarity
    st.divider()

    # Create five columns to display various bowling metrics for the bowler across all seasons
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display metrics such as total seasons played, matches played, wickets taken, fours/sixes given, and economy rate
    with col1:
        st.metric('Total Seasons Played', data['bowlerAllSeasons']['totalSeasonsPlayed'])
    with col2:
        st.metric('Total Matches Played', data['bowlerAllSeasons']['totalMatchesPlayed'])
    with col3:
        st.metric('Total Wickets', data['bowlerAllSeasons']['totalWickets'])
    with col4:
        st.metric('Fours/Sixes', str(data['bowlerAllSeasons']['totalFours']) + '/' + str(data['bowlerAllSeasons']['totalSixes']))
    with col5:
        st.metric('Economy', data['bowlerAllSeasons']['economy'])

    # Display additional metrics such as average, strike rate, best bowling figure, 3-wicket hauls, and Man of the Match awards
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.metric('Average', data['bowlerAllSeasons']['average'])
    with col7:
        st.metric('Strike Rate', data['bowlerAllSeasons']['strikeRate'])
    with col8:
        st.metric('Best Figure', data['bowlerAllSeasons']['bestFigure'])
    with col9:
        st.metric('Total 3+W', data['bowlerAllSeasons']['totalW3'])
    with col10:
        st.metric('Total MOM', data['bowlerAllSeasons']['totalMOM'])

    # Insert another visual divider
    st.divider()

    # Display the current team the bowler is playing for
    st.subheader('Playing In')
    st.success(data['bowlerAllSeasons']['playingIn'])

    # If the bowler has played for multiple teams, display the list of teams
    if data['bowlerAllSeasons']['playedIn']['teams']:
        st.subheader('Played In')
        st.table(pd.DataFrame(data['bowlerAllSeasons']['playedIn']['teams'], columns=['Team Name'], index=range(1, len(data['bowlerAllSeasons']['playedIn']['teams']) + 1)))

    # Insert another visual divider
    st.divider()

    # Display a scatter plot of the bowler's wickets across different seasons
    st.subheader('Season Wise Wickets')

    trace = go.Scatter(x=data['bowlerAllSeasons']['seasonWiseWickets']['seasons'], y=data['bowlerAllSeasons']['seasonWiseWickets']['wickets'])
    layout = go.Layout(xaxis={'title': 'Seasons'}, yaxis={'title': 'Wickets'})

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_xaxes()

    # Render the plotly chart on Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Function to fetch and visualize IPL data for the bowler for a specific season
def bowlerSeason(bowler, season):
    # Fetch the performance details of the bowler for a specific season from the API
    data = api.bowlerSeason(bowler, season)

    # Set the title for the Streamlit dashboard to indicate the analysis is for a specific season
    st.title('{} Season Analysis'.format(season))

    # Insert a visual divider for clarity
    st.divider()

    # Create four columns to display various primary bowling metrics for the bowler in the given season
    col1, col2, col3, col4 = st.columns(4)

    # Display metrics such as matches played, wickets taken, fours/sixes given, and economy rate for the season
    with col1:
        st.metric('Total Matches Played', data['bowlerSeason']['totalMatchesPlayed'])
    with col2:
        st.metric('Total Wickets', data['bowlerSeason']['totalWickets'])
    with col3:
        st.metric('Fours/Sixes', str(data['bowlerSeason']['totalFours']) + '/' + str(data['bowlerSeason']['totalSixes']))
    with col4:
        st.metric('Economy', data['bowlerSeason']['economy'])

    # Display additional metrics such as average, strike rate, best bowling figure, 3-wicket hauls, and Man of the Match awards
    col5, col6, col7, col8, col9 = st.columns(5)
    with col5:
        st.metric('Average', data['bowlerSeason']['average'])
    with col6:
        st.metric('Strike Rate', data['bowlerSeason']['strikeRate'])
    with col7:
        st.metric('Best Figure', data['bowlerSeason']['bestFigure'])
    with col8:
        st.metric('Total 3+W', data['bowlerSeason']['totalW3'])
    with col9:
        st.metric('Total MOM', data['bowlerSeason']['totalMOM'])

    # Insert another visual divider
    st.divider()

    # Display the current team the bowler is playing for in this season
    st.subheader('Playing In')
    st.success(data['bowlerSeason']['playingIn'])

    # Insert another visual divider
    st.divider()

    # Display a table showing wickets taken by the bowler against all teams in this season
    st.subheader('Wickets Against All Teams')
    st.table(pd.DataFrame(list(zip(data['bowlerSeason']['wicketsAgainstAllTeams']['teams'], data['bowlerSeason']['wicketsAgainstAllTeams']['wickets'])), columns=['Team Name', 'Wickets'], index=range(1, len(data['bowlerSeason']['wicketsAgainstAllTeams']['teams']) + 1)))

    # Insert another visual divider
    st.divider()

    # Display a scatter plot representing wickets taken by the bowler in each match of this season
    st.subheader('Matches Wise Wickets')

    trace = go.Scatter(x=data['bowlerSeason']['matchesWiseWickets']['matches'], y=data['bowlerSeason']['matchesWiseWickets']['wickets'])
    layout = go.Layout(xaxis={'title': 'Matches'}, yaxis={'title': 'Wickets'})

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_xaxes()

    # Render the plotly chart on Streamlit
    st.plotly_chart(fig, use_container_width=True)