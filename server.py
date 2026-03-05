"""
Flask server for Emotion Detection web application.

This server exposes two routes:
1. "/" - Renders the homepage.
2. "/emotionDetector" - Processes emotion detection requests.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)

    @app.route("/")
    def render_index_page():
        """
        Render the main index page.

        Returns:
            str: Rendered HTML template.
        """
        return render_template("index.html")

    @app.route("/emotionDetector")
    def emotion_detector_route():
        """
        Handle emotion detection requests.

        Returns:
            str: Formatted emotion analysis result.
        """
        text_to_analyze = request.args.get("textToAnalyze")

        response = emotion_detector(text_to_analyze)

        if response["dominant_emotion"] is None:
            return "Invalid text! Please try again."

        formatted_response = (
            "For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )

        return formatted_response

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
