# Neural Audio book creator

Using the utilities from this repository, you can voice any book in text format using a neural network!
Moreover, you can use any voice, you only need a quality file wav.


# How to use it

Clone this repo, than change your work directory to cloned repo

This repo has example of input.txt and text-splitter\out files

Delete files from text-splitter\out and coqui_tts\outputs before start

Then create file text-splitter\input.txt and place text from your book.

Install python (I test it on 3.9.8 version)

Install requirements via pip:
```
pip install -r requirements.txt
```

After that run text-splitter\text-splitter.py

It will split the file input.txt into parts and save it in path text-splitter\out

Next step is run text to audio convertion.

Before we start, open file coqui_tts\text2audio.py in text editor and change settings:

```
charvoice="female_01.wav" # Neural voice, used voices here coqui_tts\voices. You can add any good wav to this dir and then use

ttslanguage="Russian" # What language will the voice acting be performed in. All list available here coqui_tts\languages.json

model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda") # If you dont have Nvidia GPU change "cuda" to "cpu"

```

Now, when you complete with audio settings, run file coqui_tts\text2audio.py

After launch, the process of converting text to audio will begin, the resulting files will be saved to a directory coqui_tts\outputs and numbered

Once the conversion process is complete, you can enjoy your new audiobook!