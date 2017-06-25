import mammoth


style_map = """
p[style-name='Section Title'] => h1:fresh
p[style-name='Subsection Title'] => h2:fresh
"""
# KeyError: "There is no item named 'word/styles.xml' in the archive"
with open("../../res/paper.doc", "rb") as doc_file:
    print(doc_file.name)
    result = mammoth.convert_to_html(doc_file, style_map=style_map)
    html = result.value  # The generated HTML
    messages = result.messages  # Any messages, such as warnings during conversion
    print(html)
