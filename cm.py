import os
from openai import OpenAI
import numpy as np
import json


def get_random_item(filename: str) -> str:
    with open(filename) as file:
        items = file.readlines()
    return np.random.choice(items).strip()

def generate_club_history_prompt(randomClub: str) -> str:
    return f"""
    I'm doing a FIFA career mode trying to generate important information to make my career mode 
    more immersive and I need you to as a fifa career mode expert. 
    Please provie me with the following information about {randomClub}:

    1. **Club Backstory**: 
       - Write an in-depth backstory of the club in a paragraph longer than 10 sentences.
       - Include at least 5 sentences about their 2 biggest rivals.
       - Make it sound like a historian wrote it.

    2. **League History**:
       - Write a paragraph about the history of the league {randomClub} is in.
       - Focus on the 4 most successful clubs and the 5 biggest rivalries, explaining why they are rivals.
       - Ensure it is no less than 6 sentences and sounds like a historian wrote it.

    3. **Club Philosophy**:
       - Provide a 7-sentence paragraph about {randomClub}'s playing style and transfer philosophy.

    4. **Club Influence and Achievements**:
       - Write a paragraph about {randomClub}'s influence on soccer.
       - Include details about their most successful season in the league and continental competitions.
       - Mention club legends and current key players.
       - Make it sound like a historian wrote it.
    """

def get_ai_response(prompt: str) -> str:
    api_key = 'lm-studio'
    if not api_key:
        raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")
    
    client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
    
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model='deepseek-r1-distill-qwen-32b',
        messages=messages,
        stream=False
    )
    
    return response.choices[0].message.content

def main() -> None:
    randomClub = get_random_item('fifaClubTeams.txt')
    print("Your starter team is: " + randomClub)

    randomChallenge = get_random_item('fifaChallenges.txt')
    print("Your save challenge is: " + randomChallenge)

    randomFormation = get_random_item('fifaFormations.txt')
    print("Your formation is: " + randomFormation)

    clubHistoryPrompt = generate_club_history_prompt(randomClub)
    
    final = get_ai_response(clubHistoryPrompt)

    noThinkResponse = final.split('</think>')[-1].strip()
    print(noThinkResponse)

if __name__ == "__main__":
    main()