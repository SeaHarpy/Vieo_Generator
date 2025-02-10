import edge_tts
import asyncio

async def generate_audio(text, voice, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"Audio file saved as: {output_file}")

if __name__ == "__main__":
    # Define text, voice, and output file
    text = "Hello my name is Perl. I love to swim and splash my friends!"
    voice = "en-GB-RyanNeural"
    output_file = "audioFile1.wav"

    # Run the async function
    asyncio.run(generate_audio(text, voice, output_file))
