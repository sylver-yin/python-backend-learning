import pytest  # type: ignore
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """A survey that'll be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response("EngliSH")
    assert "EngliSH" in language_survey.responses


def test_store_three_responses(language_survey):
    respones = ["english", "Spanish", "Mandarin"]
    for response in respones:
        language_survey.store_response(response)

    for response in respones:
        assert response in language_survey.responses
