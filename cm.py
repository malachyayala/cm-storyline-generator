import os
from openai import OpenAI
import numpy as np
import json

def get_random_item(filename):
    with open(filename) as file:
        items = file.readlines()
    return np.random.choice(items).strip()

def generate_club_history_prompt(randomClub):
    return f"""
    I'm doing a FIFA career mode. Please provide the following information about the club {randomClub} in JSON format:

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

def get_ai_response(prompt):
    api_key = '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'
    if not api_key:
        raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")
    
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1-distill-llama-70b:free",
        messages=messages,
        stream=False
    )
    
    return response.choices[0].message.content

def main():
    randomClub = get_random_item('fifaClubTeams.txt')
    print("Your starter team is: " + randomClub)

    randomChallenge = get_random_item('fifaChallenges.txt')
    print("Your save challenge is: " + randomChallenge)

    randomFormation = get_random_item('fifaFormations.txt')
    print("Your formation is: " + randomFormation)

    clubHistoryPrompt = generate_club_history_prompt(randomClub)
    
    final = get_ai_response(clubHistoryPrompt)
    
    try:
        structured_response = json.loads(final)
        print(json.dumps(structured_response, indent=2))
    except json.JSONDecodeError:
        print("Failed to parse JSON response")
        print(final)

if __name__ == "__main__":
    main()