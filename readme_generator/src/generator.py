import requests

def download_file(url):
	response = requests.get(url)
	return response.text

def replace(file_content, old_string, new_string):
	modified_content = file_content.replace(old_string, new_string)
	return modified_content

def main():
	# URLs of the files to be downloaded
	readme_url = "https://raw.githubusercontent.com/Cutwell/readme-template/main/README.md"
	contributing_url = "https://raw.githubusercontent.com/Cutwell/readme-template/main/.github/CONTRIBUTING.md"
	pull_request_template_url = "https://raw.githubusercontent.com/Cutwell/readme-template/main/.github/PULL_REQUEST_TEMPLATE.md"
	logo_svg_url = "https://raw.githubusercontent.com/Cutwell/readme-template/main/logo.svg"

	# Download files
	readme_content = download_file(readme_url)
	contributing_content = download_file(contributing_url)
	pull_request_template_content = download_file(pull_request_template_url)
	logo_svg_content = download_file(logo_svg_url)

	# Prompt user for GitHub username and repository name
	github_username = input("Enter your GitHub username: ")
	repository_name = input("Enter your repository name: ")

	# Define old and new strings for find and replace
	old_string = "Cutwell/readme-template"
	new_string = f"{github_username}/{repository_name}"

	# Perform find and replace
	modified_readme = readme_content.replace(old_string, new_string)
	modified_contributing = contributing_content.replace(old_string, new_string)
	modified_pull_request_template = pull_request_template_content.replace(old_string, new_string)

	# Save modified content back to files
	with open("README.md", "w") as readme_file:
		readme_file.write(modified_readme)

	with open("CONTRIBUTING.md", "w") as contributing_file:
		contributing_file.write(modified_contributing)

	with open("PULL_REQUEST_TEMPLATE.md", "w") as pull_request_template_file:
		pull_request_template_file.write(modified_pull_request_template)
	
	with open("logo.svg", "w") as logo_svg_file:
		logo_svg_file.write(logo_svg_content)

if __name__ == "__main__":
	main()
