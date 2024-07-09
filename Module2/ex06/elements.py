from elem  import Elem, Text

class Html(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="html", attr=attr, content=content, tag_type="double")

class Head(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="head", attr=attr, content=content, tag_type="double")

class Body(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="body", attr=attr, content=content, tag_type="double")

class Title(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="title", attr=attr, content=content, tag_type="double")

class Meta(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="meta", attr=attr, content=content, tag_type="simple")

class Img(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="img", attr=attr, content=content, tag_type="simple")

class Table(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="table", attr=attr, content=content, tag_type="double")

class Th(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="th", attr=attr, content=content, tag_type="double")

class Tr(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="tr", attr=attr, content=content, tag_type="double")

class Td(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="td", attr=attr, content=content, tag_type="double")

class Ul(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="ul", attr=attr, content=content, tag_type="double")

class Ol(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="ol", attr=attr, content=content, tag_type="double")

class Li(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="li", attr=attr, content=content, tag_type="double")

class H1(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="h1", attr=attr, content=content, tag_type="double")

class H2(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="h2", attr=attr, content=content, tag_type="double")

class P(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="p", attr=attr, content=content, tag_type="double")

class Div(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="div", attr=attr, content=content, tag_type="double")

class Span(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="span", attr=attr, content=content, tag_type="double")

class Hr(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="hr", attr=attr, content=content, tag_type="simple")

class Br(Elem):
    def __init__(Self, content=None, attr={}):
        super().__init__(tag="br", attr=attr, content=content, tag_type="simple")

if __name__ == "__main__":
    print( Html( [Head(), Body()] ) )
    print( Html( [Head(Title(Text('"Hello ground!"'))), Body([H1(Text('"Oh no, not again!"')), Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})])] ) )

    html_content = Html(attr={"lang": "en"}, content=[
        Head([
            Meta(attr={"charset": "UTF-8"}),
            Meta(attr={"name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
            Title(Text("Adrian Gonzalez Serrano"))
        ]),
        Body(attr= {"style": "text-align:center;"},content=[
            H1(Text("Adrian Gonzalez Serrano")),
            Hr(),
            P(Text("""
                Lausanne, Switzerland • adrian.gonser@icloud.com • +34 637543849 • adrgonza
            """)),
            H2(Text("About me")),
            P(Text("""
                I began in photojournalism but found my passion in software development and data science, completing over 30 projects at
                42Madrid. I developed strong time management skills and a deep understanding of C and Python. I am particularly
                interested in Web3 and blockchain applications, known for my dedication, curiosity, innovation, perseverance, and strong
                work ethic.
            """)),
            H2(Text("Education")),
            Table(content=[
                Tr(content=[
                    Th(Text("Institution")),
                    Th(Text("Location")),
                    Th(Text("Qualification")),
                    Th(Text("Year")),
                    Th(Text("Description"))
                ]),
                Tr(content=[
                    Td(Text("42 Lausanne")),
                    Td(Text("Lausanne, Switzerland")),
                    Td(Text("RNCP 7 Database and Data Architecture")),
                    Td(Text("2024-Current")),
                    Td(Text("I gained advanced expertise in designing, implementing, and managing complex database systems and data architectures, ensuring data integrity, security, and performance optimization."))
                ]),
                Tr(content=[
                    Td(Text("42 Lausanne")),
                    Td(Text("Lausanne, Switzerland")),
                    Td(Text("RNCP 7 Information Systems and Network Architecture")),
                    Td(Text("2024-Current")),
                    Td(Text("I acquired advanced skills in creating, implementing, and managing sophisticated information systems and network architectures, focusing on security, performance and system integration."))
                ]),
                Tr(content=[
                    Td(Text("42 Madrid")),
                    Td(Text("Madrid, Spain")),
                    Td(Text("Common Core")),
                    Td(Text("2022-2024")),
                    Td(attr={"style": "border-color: #424242;"}, content=Text("This experience provides professional skills in C programming, UNIX systems, network architecture, system administration, object-based programming, client-server projects, and basic web development."))
                ])
            ]),
            H2(Text("Skills & Interests")),
            Ul(content=[
                Li(Text("Technical: C, C++, Go, Python, GNU/Linux, Docker, Git, Virtual Machines (VMs), AWS/GCP (Cloud Platforms), SQL, HTML/CSS, JavaScript, RESTful APIs, Bash scripting, Network Security, Machine Learning (ML), Data Science, Agile methodologies.")),
                Li(content=[
                    Text("Language:"),
                    Ol(content=[
                        Li(Text("Spanish (Native)")),
                        Li(Text("English (C1)")),
                        Li(Text("French (B1)"))
                    ])
                ]),
                Li(Text("Interests: Finance and economics, skiing, climbing, surfing, driving and camping, new technology, blockchain."))
            ])
        ])
    ])
    with open("mycv.html", "w") as file:
        file.write(str(html_content))
    print(html_content)
