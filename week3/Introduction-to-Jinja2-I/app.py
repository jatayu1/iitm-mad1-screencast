from jinja2 import Template

TEMPLATE = """
Hello {{ name }} !
"""

def main():
    template = Template(TEMPLATE)
    print(template.render(name='akash'))

if __name__ == "__main__":
    main()