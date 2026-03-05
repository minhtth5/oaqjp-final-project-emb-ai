import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP Library.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        str: The text attribute of the response object from the Emotion Detection API
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=input_json, headers=headers)

        # Convert response text to Python dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotion scores
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return required format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    
emotion_detector("I love this new technology.")