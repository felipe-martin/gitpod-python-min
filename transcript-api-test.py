from youtube_transcript_api import YouTubeTranscriptApi
# the base class to inherit from when creating your own formatter.
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import JSONFormatter

class TernaFormatter(Formatter):
    def format_transcript(self, transcript, **kwargs):
        """Converts a transcript into a terna (start;duration;text) string.
        :param transcript:
        :return: A terna string representation of the transcript.'
        :rtype str
        """
        return '\n'.join("{};{};{}".format(line['start'], line['duration'], line['text']) for line in transcript)

    def format_transcripts(self, transcripts, **kwargs):
        """Converts a list of transcripts into a terna (start;duration;text) string.
        :param transcripts:
        :return: A terna string representation of the transcripts.'
        :rtype str
        """
        return '|\n|'.join([self.format_transcript(transcript, **kwargs) for transcript in transcripts])

# Ingresa aquí la ID del video de YouTube
video_id = 'PbW-1k3ZOA4'
#video_id = 'PHr8xPBhHJU'

# Obtiene la transcripción del video de YouTube
transcript_languages = YouTubeTranscriptApi.list_transcripts(video_id)
#print(transcript_languages)

transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es','en'], preserve_formatting=True)

# Crea una instancia del formateador de texto
formatter = TernaFormatter()

# Formatea la transcripción como una cadena de texto
text_formatted = formatter.format_transcript(transcript)

# Imprime la transcripción del video
print(text_formatted)

