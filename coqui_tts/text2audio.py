import html
import json
import os
import random
import time
from pathlib import Path
import re

from TTS.api import TTS
from TTS.utils.synthesizer import Synthesizer

os.environ["COQUI_TOS_AGREED"] = "1"

params = {

    "remove_trailing_dots": False

}

this_dir = str(Path(__file__).parent.resolve())
model = None
with open(Path(f"{this_dir}/languages.json"), encoding='utf8') as f:
    languages = json.load(f)








def random_sentence():
    with open(Path("./coqui_tts/harvard_sentences.txt")) as f:
        return random.choice(list(f))




random_sentence()


charvoice="female_01.wav"

ttslanguage="Russian"

print("[XTTS] Loading XTTS...")

model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

print("[XTTS] Done!")
Path(f"{this_dir}/outputs").mkdir(parents=True, exist_ok=True)


def voice_preview(string,filename ='none'):
    string = html.unescape(string) or random_sentence()

    if filename == 'none':
        print("filename parameter not set")
        output_file = Path('./coqui_tts/outputs/voice_preview.wav')
    else:
        filename
        output_file = Path('./coqui_tts/outputs/' + filename + '.wav')

    model.tts_to_file(
        text=string,
        file_path=output_file,
        speaker_wav=[f"{this_dir}/voices/{charvoice}"],
        language=languages[ttslanguage]
    )

    return f'<audio src="file/{output_file.as_posix()}?{int(time.time())}" controls autoplay></audio>'



directory = 'text-splitter\out'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        
        
        file_name = str((re.findall(r'\d+',filename))[0])

        
        with open(file_path, 'r', encoding="utf8") as file:

            file_content = ((file.read().rstrip()).replace('—\xa0','')).replace('\xa0—','')

        

        print(f"file_name: {file_name}")
        print("File content:")
        
        text=file_content
        filename=file_name
        voice_preview(text,filename)
        
