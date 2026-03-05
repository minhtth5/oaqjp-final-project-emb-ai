from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    # Get text from query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detection function
    response = emotion_detector(text_to_analyze)

    # If API returned valid result
    if response is not None:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']

        # Format output exactly as required
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {anger}, "
            f"'disgust': {disgust}, "
            f"'fear': {fear}, "
            f"'joy': {joy} and "
            f"'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )

        return formatted_response

    else:
        return "Invalid text! Please try again."

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
