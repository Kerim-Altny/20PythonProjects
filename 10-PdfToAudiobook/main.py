import os
import boto3
from pypdf import PdfReader
from dotenv import load_dotenv


load_dotenv()

# Initialize AWS Polly Client
def get_polly_client():
    print("☁️ Connecting to AWS Polly...")
    
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name='eu-central-1'
    )
    return session.client('polly')

# Extract Text from PDF
def extract_text(pdf_path):
    print(f"📄 Extracting text from '{pdf_path}'...")
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + " "
    return full_text

# Convert Text to Speech
def text_to_speech(polly_client, text, output_file="audiobook.mp3"):
    print("🎙️ Converting text to speech (This may take a while depending on text length)...")
    clean_text = text.replace('\n', ' ')
    ssml_text = f"<speak><prosody rate='125%'>{clean_text}</prosody></speak>"
    
    try:
        response = polly_client.synthesize_speech(
            VoiceId='Filiz',        
            OutputFormat='mp3',
            TextType='ssml',
            Text=ssml_text,
            Engine='standard'       
        )

        if "AudioStream" in response:
            with open(output_file, "wb") as file:
                file.write(response["AudioStream"].read())
            print(f"✅ Success! Audio file saved as: {output_file}")
            os.system(f"start {output_file}")
            
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    PDF_FILE_NAME = "test.pdf"  
    
    
    text_to_read = extract_text(PDF_FILE_NAME)
    
    test_text = text_to_read[:3000] 
    
    if test_text.strip():
        client = get_polly_client()
        text_to_speech(client, test_text)
    else:
        print("⚠️ Could not extract text from PDF, or the file is empty.")