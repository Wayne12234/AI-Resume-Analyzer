# Import Gemini AI
from google import genai

# Import PDF reader
from pypdf import PdfReader


# Connect Gemini API
client = genai.Client(api_key="YOUR API KEY")


# Open PDF file
reader = PdfReader("RESume.pdf")


# Empty variable to store extracted text
resume_text = ""


# Loop through all PDF pages
for page in reader.pages:

    # Extract text from current page
    text = page.extract_text()

    # Add text into resume_text
    resume_text += text


# Create prompt for Gemini
prompt = "Analyze this resume:\n" + resume_text


# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)


# Print AI response
print(response.text)
