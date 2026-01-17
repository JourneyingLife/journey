import markdown2

# Read the markdown file
with open('Journey_Novel.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown2.markdown(md_content, extras=['fenced-code-blocks', 'tables'])

# Fix image paths for HTML in read_version/ folder
html_content = html_content.replace('src="Pictures/', 'src="../Pictures/')

# Add CSS styling
css = """
<style>
    body {
        font-family: 'Georgia', serif;
        line-height: 1.6;
        font-size: 12pt;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    h1 {
        font-size: 24pt;
        margin-top: 20pt;
        margin-bottom: 10pt;
        page-break-before: always;
        page-break-after: avoid;
        break-before: always;
        break-after: avoid;
    }
    h1:first-of-type {
        page-break-before: avoid;
        break-before: avoid;
    }
    h2 {
        font-size: 18pt;
        margin-top: 15pt;
        margin-bottom: 8pt;
        page-break-before: auto;
        page-break-after: avoid;
        page-break-inside: avoid;
        break-before: auto;
        break-after: avoid;
        break-inside: avoid;
    }
    h3 {
        font-size: 14pt;
        font-style: italic;
        margin-top: 10pt;
        margin-bottom: 5pt;
        page-break-after: avoid;
        page-break-inside: avoid;
        break-after: avoid;
        break-inside: avoid;
    }
    p {
        text-align: justify;
        margin-bottom: 10pt;
        orphans: 3;
        widows: 3;
    }
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 20px auto;
        page-break-inside: avoid;
        break-inside: avoid;
    }
    hr {
        page-break-after: always;
        break-after: always;
        border: none;
        margin: 30px 0;
    }
    @media print {
        body {
            max-width: 100%;
        }
        @page {
            margin: 1in;
            size: letter;
        }
    }
</style>
"""

# Wrap HTML with proper structure
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Journey - A Novel</title>
    {css}
</head>
<body>
{html_content}
</body>
</html>
"""

# Save HTML file
with open('read_version/Journey_Novel.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("HTML regenerated with JPG images")
