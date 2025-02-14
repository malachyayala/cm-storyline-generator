from openai import OpenAI
import numpy as np
import json

client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
MODEL = "deepseek-r1-distill-llama-8b"

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

clubHistoryPrompt = f"""Im doing a fifa career mode, give me an in depth backstory of the club {randomClub} in a paragraph that's longer than 10 sentences with at least 5 sentences about their 2 biggest rivals in the same paragraph. Make it sound like a historian wrote it. 
                      Write a paragraph about the history of the league {randomClub} are in, focusing on the 4 most successful clubs and the 5 biggest rivalries and why theyre rivals. in no less than 6 sentences. Make it sound like a historian wrote it. 
                      Give me a 7 sentence paragraph about {randomClub} playing style and transfer philosophy. Give me one more paragraph about what you feel is most relevent in terms of if {randomClub} have had any influence on soccer, their most successful season in the league and continental competitions, club legends, and current key players. Make it sound like a historian wrote it""" 



# Define the conversation with the AI
messages = [
    {"role": "user", "content": clubHistoryPrompt}
]

# Define the expected response structure
""" storyline_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "storyline",
        "schema": {
            "type": "object",
            "properties": {
                "storylines": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "backstory": {"type": "string"},
                            "leagueHistory": {"type": "string"},
                            "playStyle": {"type": "string"}
                        },
                        "required": ["backstory", "leagueHistory", "playstyle"]
                    },
                    "minItems": 1,
                }
            },
            "required": ["storylines"]
        },
    }
} """

# Get response from AI
response = client.chat.completions.create(
    model="your-model",
    messages=messages,
)

# Parse and display the results
""" results = json.loads(response.choices[0].message.content)
print(json.dumps(results, indent=2)) """

print(response.choices[0].message.content)
