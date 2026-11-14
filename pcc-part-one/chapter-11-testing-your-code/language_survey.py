from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
langugae_survey = AnonymousSurvey(question)

langugae_survey.show_question()
print("Enter 'q' to leave at any time.\n")
while True:
    response = input("Language: ").lower().strip()
    if response == "q":
        break
    langugae_survey.store_response(response)

print("\nThank you to everyone who participated in this survey!")
langugae_survey.show_results()
