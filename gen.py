import numpy as np

'''
- Version of fifa
- League selection
- Country selection
- International team and challenge
- Mods
- Storyline generator
Im doing a fifa career mode, give me an in depth back story of the club RB Leipzig in 3 paragraphs with a small part about their playing style and transfer policy historically
'''

with open('cm/fifaClubTeams.txt') as clubs:
    # Read all the lines into a list
    allClubs = clubs.readlines()
randomClub = np.random.choice(allClubs)
print("Your starter team is: " + randomClub)

with open('cm/fifaChallenges.txt') as challenges:
    # Read all the lines into a list
    allChallenges = challenges.readlines()
randomChallenge = np.random.choice(allChallenges)
print("Your save challenge is: " + randomChallenge)

with open('cm/fifaFormations.txt') as formations:
    # Read all the lines into a list
    allFormations = formations.readlines()
randomFormation = np.random.choice(allFormations)
print("Your formation is: " + randomFormation)

#breakitup?
""" clubHistoryPrompt = f"Im doing a fifa career mode, give me an in depth back story of the club {randomClub} in a paragraph that's longer than 10 sentences with at least 5 sentences about their 2 biggest rivals in the same paragraph. Make it sound like a historian wrote it" 
leagueHistoryPrompt = f"Write a paragraph about the history of the league {randomClub} are in, focusing on the 4 most successful clubs and the 5 biggest rivalries and why theyre rivals. in no less than 6 sentences. Make it sound like a historian wrote it" 
stylePhilosophyPrompt = f"Give me a 7 sentence paragraph about {randomClub} playing style and transfer philosophy. Give me one more paragraph about what you feel is most relevent in terms of if {randomClub} have had any influence on soccer, their most successful season in the league and continental competitions, club legends, and current key players. Make it sound like a historian wrote it" 

LOprompts = [clubHistoryPrompt, leagueHistoryPrompt, stylePhilosophyPrompt]
createP = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [{"role": "user", "content": LOprompts[1]}]) """
#for p in LOprompts:
#    createP = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [{"role": "user", "content": p}])
#    print(createP.choices[0].message.content)


'''
clubOrNational = input("Would you like to select a national or club team?: ")
if clubOrNational.casefold() == "Club".casefold():
    line = random.choice(open('/Users/mj/Desktop/VSCodeStuff/Teams/fifaClubTeams.txt').readlines())
    print(line)
elif clubOrNational.casefold() == "National".casefold():
    line = random.choice(open('/Users/mj/Desktop/VSCodeStuff/Teams/fifaNationalTeams.txt').readlines())
'''