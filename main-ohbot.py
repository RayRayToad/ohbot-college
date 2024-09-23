from ohbot import ohbot
import random
import speech_recognition as sr
import time

# Initialize speech recognition
recognizer = sr.Recognizer()

# Define quiz questions
questions = [
    ("What is the capital of France?", ["A) London", "B) Paris", "C) Rome"], "B"),
    ("What is 2 + 2?", ["A) 3", "B) 4", "C) 5"], "B"),
    ("What is the largest planet in the solar system?", ["A) Earth", "B) Mars", "C) Jupiter"], "C")
]

# Function to get voice input from the user
def get_voice_answer():
    with sr.Microphone() as source:
        ohbot.say("Please say your answer.")
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # Convert speech to text and capitalize the answer for comparison
            return recognizer.recognize_google(audio).upper()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."

# Main quiz function
def quiz_game():
    ohbot.reset()
    ohbot.say("Welcome to Ohbot's voice-controlled quiz game!")
    score = 0

    random.shuffle(questions)  # Shuffle questions for randomness

    for question, choices, correct_answer in questions:
        ohbot.say(question)
        for choice in choices:
            ohbot.say(choice)
        
        # Get user answer via voice recognition
        user_answer = get_voice_answer()
        print(f"User said: {user_answer}")
        
        # Check if the answer is correct
        if user_answer == correct_answer:
            ohbot.say("Correct!")
            score += 1
            ohbot.move(ohbot.HEADNOD, 10)  # Nod in approval
        else:
            ohbot.say(f"Sorry, that's not correct. The right answer is {correct_answer}.")
            ohbot.move(ohbot.HEADTURN, 0)  # Shake head
        
        ohbot.wait(1)

    # End of the quiz - Show score
    ohbot.say(f"Your final score is {score} out of {len(questions)}")
    ohbot.reset()

# Run the quiz
quiz_game()
