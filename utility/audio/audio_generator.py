import edge_tts
import json

async def generate_audio(text,outputFilename):
    communicate = edge_tts.Communicate(text,"en-GB-RyanNeural")
    await communicate.save(outputFilename)

    # dump to json
    metadata={"text": text}
    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(metadata, json_file, ensure_ascii=False, indent=4)
