import os, sys, shutil
import yaml


def generate_email_schema(template_path, **input_dict):
    pass


def generate_email(job_name, company_name, recruiter_email, heard_about):
    head = f"""
    <head>
        <meta charset='UTF-8'>
        <meta name="Description" content="Cold email">
    </head>
    """

    body = f"""
    <body>

    <p>
    To Whom it may concern,
    </p>

    <p>
    My name is Anthony Jiang, a CS/Math student at Yale '23, considering a leave of absence in fall or an entire gap year. I saw your company listed on crunchbase, and decided to reach out about potential fall internship opportunities. {heard_about} I have intermediate experience with python, especially data analysis and machine learning libraries, as well as some experience in C. However, with a month left in the summer, if you need me to learn a new language/tech stack, I’d be eager to do so unpaid before taking on a paid role in fall. 
    </p>
    <p>
    At Yale, I've completed 223 Data Structures/Programming Techinques and 244 Discrete Math. I have intermediate python experience through my work with Professor Aaron Dollar’s new Yale Tech for Conservation Lab and personal projects. With YTFC lab, I’ve been using tensorflow/keras to build convolutional neural networks that can speciate leaves, as well as building custom tooling, data pipelines, and verification scripts in python for the other models in the group; a paper is underway. All in all, I'm comfortable with tensorflow/keras and have worked with PyTorch. 
    </p>
    <p>
    Outside of my work with the lab, I have solid experience with data analysis roles. After my junior year of high school, I interned with the Democrat Mark Phariss’ Campaign for Texas Senate, working on the “data desk”. Besides generating the standard crop of data metrics (sign placement efficiencies, volunteer utilizations, etc.), I used python HTML scraping packages to find the publically available school emails of teachers across the senate district, adding over 5,000 addresses to our email panlist. I’m currently working on an algorithmic python trader using the Alpaca API. Thus far, I’ve built a sentiment analyzer using VADER, and am adding a revenue correlation and LSTM module. 
    </p>
    I would love to discuss with you any future opportunities at {company_name} or schedule a call.
    </p>
    <p>
    Thanks,
    <br>
    <br>
    Anthony Jiang
    </p>


    </body>
    """

    root_dir = "/Users/antonsquared/Projects/kennel"
    with open(f"{root_dir}/email_buffer/{company_name}.html", "w") as output_file: ## configure relative path?
        print(head, file=output_file)
        print(body, file=output_file)



if __name__ == "__main__":
    generate_email("1", "4", "3", "4")