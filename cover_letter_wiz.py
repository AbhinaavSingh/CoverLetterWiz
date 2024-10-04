import openai
import PyPDF2
from openai import OpenAI

# Set the path to your resume PDF as high up as possible
resume_path = "Path_To_Resume.pdf"

# Function to read the API key from a file
def read_api_key(file_path):
    try:
        with open(file_path, "r") as file:
            api_key = file.read().strip()
        return api_key
    except Exception as e:
        return f"An error occurred while reading the API key file: {str(e)}"

# Read the API key from 'open_ai_key.txt'
api_key = read_api_key("open_ai_key.txt")

# Initialize the OpenAI client with the API key
if "An error occurred" in api_key:
    print(api_key)
else:
    client = OpenAI(api_key=api_key)

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
            return text
    except Exception as e:
        return f"An error occurred while reading the PDF: {str(e)}"

def read_job_description(file_path):
    try:
        with open(file_path, "r") as file:
            job_description = file.read().strip()
        return job_description
    except Exception as e:
        return f"An error occurred while reading the job description file: {str(e)}"

def get_chatgpt_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def extract_company_and_role_from_jd(job_description):
    prompt = f"""
    Please extract the company name and the role title from the following job description:
    {job_description}
    
    Provide the response in the format:
    Company: <company name>
    Role: <role title>
    """
    response = get_chatgpt_response(prompt)
    
    # Split the response to extract company name and role
    try:
        lines = response.split("\n")
        company_name = lines[0].replace("Company:", "").strip()
        role_name = lines[1].replace("Role:", "").strip().replace(" ", "_")
        return company_name, role_name
    except Exception as e:
        return f"An error occurred while extracting company name and role: {str(e)}", None

def save_cover_letter_to_file(cover_letter, company_name, role_name):
    file_name = f"CoverLetter_{company_name}_{role_name}.txt"
    try:
        with open(file_name, "w") as file:
            file.write(cover_letter)
        print(f"Cover letter saved as {file_name}")
    except Exception as e:
        print(f"An error occurred while saving the file: {str(e)}")

if __name__ == "__main__":
    # Define the path to your job description text file
    job_description_file_path = "job_description.txt"

    # Read the job description from the file
    job_description = read_job_description(job_description_file_path)
    
    if "An error occurred" in job_description:
        print(job_description)
    else:
        # Extract the company name and role using ChatGPT
        company_name, role_name = extract_company_and_role_from_jd(job_description)
        
        if role_name is None:
            print(company_name)  # Print error message if extraction failed
        else:
            # Extract resume content from the PDF
            resume_content = extract_text_from_pdf(resume_path)

            # Prepare the prompt for ChatGPT by combining the job description and the resume
            prompt = f"""
            I am applying for the {role_name.replace('_', ' ')} position at {company_name}. 
            Below is the job description for the role:
            {job_description}
            
            Here is my resume:
            {resume_content}
            
            Based on my resume and the job description, please write a personalized cover letter for the position of {role_name.replace('_', ' ')} at {company_name}.
            """

            # Get the cover letter response from ChatGPT
            result = get_chatgpt_response(prompt)

            # Print the generated cover letter
            print(result)

            # Save the cover letter to a file
            save_cover_letter_to_file(result, company_name, role_name)
