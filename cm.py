from openai import OpenAI
import numpy as np
import json

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="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")

with open('fifaClubTeams.txt') as clubs:
    # Read all the lines into a list
    allClubs = clubs.readlines()
randomClub = np.random.choice(allClubs)
print("Your starter team is: " + randomClub)

with open('fifaChallenges.txt') as challenges:
    # Read all the lines into a list
    allChallenges = challenges.readlines()
randomChallenge = np.random.choice(allChallenges)
print("Your save challenge is: " + randomChallenge)

with open('fifaFormations.txt') as formations:
    # Read all the lines into a list
    allFormations = formations.readlines()
randomFormation = np.random.choice(allFormations)
print("Your formation is: " + randomFormation)

clubHistoryPrompt = f"""
I'm doing a FIFA career mode. Please provide the following information about the club {randomClub}:

1. **Club Backstory**: 
   - Write an in-depth backstory of the club in a paragraph longer than 10 sentences.
   - Include at least 5 sentences about their 2 biggest rivals.
   - Make it sound like a historian wrote it.

2. **League History**:
   - Write a paragraph about the history of the league {randomClub} is in.
   - Focus on the 4 most successful clubs and the 5 biggest rivalries, explaining why they are rivals.
   - Ensure it is no less than 6 sentences and sounds like a historian wrote it.

3. **Playing Style and Transfer Philosophy**:
   - Provide a 7-sentence paragraph about {randomClub}'s playing style and transfer philosophy.

4. **Club Influence and Achievements**:
   - Write a paragraph about {randomClub}'s influence on soccer.
   - Include details about their most successful season in the league and continental competitions.
   - Mention club legends and current key players.
   - Make it sound like a historian wrote it.
"""


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
messages = [
    {"role": "user", "content": clubHistoryPrompt}
]

response = client.chat.completions.create(
    model="deepseek/deepseek-r1-distill-llama-70b:free",
    messages=messages,
    stream=False
)

final = response.choices[0].message.content
            
noThinkResponse = final.split('</think>')[-1].strip()

print(noThinkResponse)

# Parse and display the results
""" results = json.loads(response.choices[0].message.content)
print(json.dumps(results, indent=2)) """
