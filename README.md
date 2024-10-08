# CoverLetterWiz
Automate the creation of personalized job application cover letters by leveraging OpenAI's GPT-3.5 to generate custom letters based on your resume and job description.


Cover Letter Wiz is a Python script designed to streamline the process of creating personalized job application cover letters. By utilizing OpenAI's GPT-3.5, the script reads a job description and resume, automatically extracts key details such as the company name and role, and generates a customized cover letter, saving you time and effort.

## Features

- **Automatic Role and Company Name Extraction**: Sends the job description to OpenAI GPT-3.5 to automatically extract the role and company name, ensuring accurate cover letters for various job descriptions.
- **Resume Parsing**: Reads your resume from a PDF file and incorporates the details into the generated cover letter.
- **Job Description Parsing**: Reads the job description from a `.txt` file and uses it as a prompt to generate the personalized cover letter.
- **Tailored Cover Letter Generation**: Creates a professional, custom cover letter that is specific to the job and company.
- **File Output**: Saves the generated cover letter as a `.txt` file, with the file name structured as `CoverLetter_<company_name>_<role_name>.txt`.

## How It Works

1. The script reads the **API key** from a file (`open_ai_key.txt`).
2. It reads the **job description** from a text file (`job_description.txt`), and uses OpenAI GPT-3.5 to extract the company name and role.
3. The **resume** is read from a PDF file and is included as part of the cover letter generation process.
4. A custom cover letter is generated by OpenAI based on the job description and resume.
5. The generated cover letter is saved as a `.txt` file named `CoverLetter_<company_name>_<role_name>.txt`.

## Files

- **`open_ai_key.txt`**: Contains your OpenAI API key.
- **`job_description.txt`**: Contains the job description text.
- **`Resume_Path.pdf`**: Your resume in PDF format.
- **Generated Cover Letter**: The generated cover letter is saved as a `.txt` file in the format `CoverLetter_<company_name>_<role_name>.txt`.

## Requirements

- Python 3.x
- OpenAI Python library (`openai`)
- `PyPDF2` for parsing PDF resumes
- An OpenAI API key (saved in `open_ai_key.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhinaavsingh/Cover-Letter-Wiz.git
   ```
2. Navigate to the directory:
   ```bash
   cd Cover-Letter-Wiz
   ```
3. Install the required libraries from the requirements.txt file::
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key to `open_ai_key.txt`.

5. Replace the default `job_description.txt` and `Resume_Path.pdf` files with your own job description and resume.

## Usage

1. Ensure your **API key**, **job description**, and **resume** files are properly placed.
2. Run the script:
   ```bash
   python cover_letter_wiz.py
   ```
3. The generated cover letter will be saved in the current directory with the file name `CoverLetter_<company_name>_<role_name>.txt`.

## Example

- **Job Description**: Stored in `job_description.txt`
- **Resume**: Your resume in `Resume_Path.pdf`

The script will generate a cover letter based on the provided information, and the output file will be named `CoverLetter_Meta_Product_Manager.txt` (as an example).

## License

This project is licensed under the MIT License.

---

Let me know if you'd like any additional adjustments or changes for the repo!
