from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def generate_cv_pdf(cv_data, output_path="generated/improved_cv.pdf"):
    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template("cv_template.html")

    html_content = template.render(cv=cv_data)

    HTML(string=html_content).write_pdf(output_path)

    return output_path