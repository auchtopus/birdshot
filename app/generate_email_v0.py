import os, sys, shutil
import yaml

def generate_email(job_name, company_name, recruiter, heard_about):
    head = f"""
    <head>
        <meta charset='UTF-8'>
        <meta name="Description" content="test email">
    </head>
    """



    # job_name = f"""test_job"""
    # company_name = f"""test_name"""
    # recruiter = f"""recruiter_name"""

    # heard_about = f""""""


    body = f"""
    <body>

    <p>
    Dear {recruiter},
    </p>

    <p>
    My name is Anthony Jiang, a CS/Math student at Yale '23. I'm considering taking a leave of absence in fall or an entire gap year, and am hoping to fill the {job_name} role at {company_name}. {heard_about} I have intermediate experience with python, especially data analysis and machine learning libraries, as well as some experience in C. However, with two months left in the summer, if you need me to learn a new language/tech stack, I’d be eager to do so unpaid before taking on a paid role in fall. 
    </p>
    <p>
    At Yale, I've completed 223 Data Structures/Programming Techinques and 244 Discrete Math. I have intermediate python experience through my work with Professor Aaron Dollar’s new Yale Tech for Conservation Lab and personal projects. With YTFC lab, I’ve been using tensorflow/keras to build convolutional neural networks that can speciate leaves, as well as building custom tooling, data pipelines, and verification scripts in python for the other models in the group. I also do analysis on the results, and will be 3rd author on the current paper push. All in all, I'm competent with tensorflow/keras and have experience working with PyTorch. I'm also familiar  with the math underlying deep neural networks as a whole, CNNs, PCAs, and SVMs, and have a working understanding of Mask-RCNN as well as LSTM. 
    </p>
    <p>
    Outside of my work with the lab, I have solid experience with data analysis roles. After my junior year of high school, I interned with the Democrat Mark Phariss’ Campaign for Texas Senate, working on the “data desk”. Besides generating the standard crop of data metrics (sign placement efficiencies, volunteer utilizations, etc.), I used python HTML scraping packages to find the publically available school emails of teachers across the senate district, adding over 5,000 addresses to our email panlist. I’m currently working on an algorithmic python trader using the Alpaca API. Thus far, I’ve built a sentiment analyzer using VADER, and am adding a revenue correlation and LSTM module. 
    </p>
    <p>
    Finally, I also have a strong mathematical foundation, reaching a top 500 finish (out of over 4,000) in the 2019 William H. Putnam competition, the premier undergraduate proof-based math competition. 
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

    with open(f"../email_templates/{company_name}.html", "w") as output_file:
        print(head, file=output_file)
        print(body, file=output_file)
