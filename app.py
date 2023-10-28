# Importing necessary libraries and modules
import streamlit as st
import analysis

# Setting the page title for the Streamlit app
st.set_page_config(page_title='IPL Analytics Dashboard')

# Sidebar title
st.sidebar.title('IPL Analytics Dashboard')

# Dropdown menu for user to select the type of analysis they want
option = st.sidebar.selectbox('Select Analysis :', ['Season Wise', 'Team Wise', 'Team Vs Team Wise', 'Batsman Wise', 'Bowler Wise'])

# Dropdown menu for user to select the IPL season
season = st.sidebar.selectbox('Select Season :', ['All Seasons', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014',
                               '2013', '2012', '2011', '2010', '2009', '2008'])

# Logic for Team Wise analysis
if option == 'Team Wise':
    if season == 'All Seasons':
        team = st.sidebar.selectbox('Select Team :',['Chennai Super Kings', 'Deccan Chargers', 'Delhi Capitals', 'Gujarat Lions', 'Gujarat Titans', 'Kochi Tuskers Kerala', 'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians', 'Pune Warriors', 'Punjab Kings', 'Rajasthan Royals', 'Rising Pune Supergiant', 'Royal Challengers Bangalore','Sunrisers Hyderabad'])

    else:
        # Fetching the teams of the selected season
        teams = analysis.teamsPerSeason(season)
        team = st.sidebar.selectbox('Select Team :', teams)

# Logic for Team Vs Team analysis
elif option == 'Team Vs Team Wise':
    if season == 'All Seasons':
        team1 = st.sidebar.selectbox('Select Team 1 :',['Chennai Super Kings', 'Deccan Chargers', 'Delhi Capitals', 'Gujarat Lions','Gujarat Titans', 'Kochi Tuskers Kerala', 'Kolkata Knight Riders','Lucknow Super Giants', 'Mumbai Indians', 'Pune Warriors', 'Punjab Kings', 'Rajasthan Royals', 'Rising Pune Supergiant', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

        # Fetching the teams that played against the selected team
        teams = analysis.teamsPerTeam(team1)
        team2 = st.sidebar.selectbox('Select Team 2 :', teams)

    else:
        # Fetching the teams of the selected season
        teams1 = analysis.teamsPerSeason(season)
        team1 = st.sidebar.selectbox('Select Team 1 :', teams1)

        # Fetching the teams that played against the selected team of the selected season
        teams2 = analysis.teamsPerSeasonTeam(season, team1)
        team2 = st.sidebar.selectbox('Select Team 2 :', teams2)

# Logic for Batsman Wise analysis
elif option == 'Batsman Wise':
    if season == 'All Seasons':
        # Fetching all batsmen from all seasons
        batsmen_names = analysis.batsmenPerAllSeasons()
        batsman = st.sidebar.selectbox('Select Batsman :', batsmen_names)

    else:
        # Fetching batsmen of the selected season
        batsmen_names = analysis.batsmenPerSeason(season)
        batsman = st.sidebar.selectbox('Select Batsman :', batsmen_names)

# Logic for Bowler Wise analysis
elif option == 'Bowler Wise':
    if season == 'All Seasons':
        # Fetching all bowlers from all seasons
        bowlers_names = analysis.bowlersPerAllSeasons()
        bowler = st.sidebar.selectbox('Select Bowler :', bowlers_names)

    else:
        # Fetching bowlers of the selected season
        bowlers_names = analysis.bowlersPerSeason(season)
        bowler = st.sidebar.selectbox('Select Bowler :', bowlers_names)

# Button to trigger the analysis
btn = st.sidebar.button('Analyse')

# Actions to be performed upon clicking the Analyse button
if btn:
    # Logic to display analysis based on user selection
    if option == 'Season Wise':
        if season == 'All Seasons':
            analysis.overallAllSeasons()
        else:
            analysis.overallSeason(season)

    elif option == 'Team Wise':
        if season == 'All Seasons':
            analysis.teamAllSeasons(team)
        else:
            analysis.teamSeason(team, season)

    elif option == 'Team Vs Team Wise':
        if season == 'All Seasons':
            analysis.teamVsTeamAllSeasons(team1, team2)
        else:
            analysis.teamVsTeamSeason(team1, team2, season)

    elif option == 'Batsman Wise':
        if season == 'All Seasons':
            analysis.batsmanAllSeasons(batsman)
        else:
            analysis.batsmanSeason(batsman, season)

    elif option == 'Bowler Wise':
        if season == 'All Seasons':
            analysis.bowlerAllSeasons(bowler)
        else:
            analysis.bowlerSeason(bowler, season)