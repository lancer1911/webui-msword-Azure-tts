import os
import docx
from pydub import AudioSegment
import azure.cognitiveservices.speech as speechsdk
from tqdm import tqdm

def read_docx(docx_file_path):
    doc = docx.Document(docx_file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def text_to_speech(text, output_filename, subscription_key, region, voice_shortname, speech_recognition_language):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region, speech_recognition_language=speech_recognition_language)
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz128KBitRateMonoMp3)
    speech_config.speech_synthesis_voice_name = voice_shortname

    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_filename)
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
    split_length = 2500 if language == "zh-CN" else 2000
    texts = [text[i:i + split_length] for i in range(0, len(text), split_length)]

    input_filename_without_ext, _ = os.path.splitext(os.path.basename(docx_file_path))
    output_filenames = []
    
    # Wrap your texts list with tqdm for a progress bar
    for i, text in enumerate(tqdm(texts, desc="Converting text to speech")):
        output_filename = f"./uploads/{input_filename_without_ext}-Azure-tts-part{i}.mp3"
        text_to_speech(text, output_filename, subscription_key, region, voice, language)
        output_filenames.append(output_filename)

    # Combine all MP3 files into one
    combined = AudioSegment.empty()
    for filename in output_filenames:
        sound = AudioSegment.from_mp3(filename)
        combined += sound

    # Save the combined audio to a file
    combined_filename = f"./uploads/{input_filename_without_ext}-Azure-tts.mp3"
    combined.export(combined_filename, format="mp3")

    # Optionally, delete the individual MP3 files
    for filename in output_filenames:
        os.remove(filename)
        
    print(f"All parts combined and saved to {combined_filename}")
    return combined_filename
