"""
Convert MS Word documents to mp3 by Azure TTS API.
written by lancer1911
May 2, 2023
"""

import os
import docx
import azure.cognitiveservices.speech as speechsdk

def read_docx(docx_file_path):
    doc = docx.Document(docx_file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def text_to_speech(text, output_filename, subscription_key, region, voice_shortname, speech_recognition_language):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.speech_synthesis_voice_name = voice_shortname
    speech_config.speech_recognition_language = speech_recognition_language

    audio_config = speechsdk.AudioConfig(filename=output_filename)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text_async(text).get()
    
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized to [{output_filename}]")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")

def docx_to_mp3(docx_file_path, subscription_key, region, language, voice):
    text = read_docx(docx_file_path)
    output_filename = os.path.splitext(docx_file_path)[0] + "-Azure-tts.mp3"
    text_to_speech(text, output_filename, subscription_key, region, voice, language)
    return output_filename
