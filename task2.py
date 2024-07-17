import re


def extract_image_links(html_text):
    image_ = r'\w{4,5}\W{3}\w{7}.\w{3}.\w{5}\d.(?:jpg|jpeg|gif|png)'
    html_text = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'>"
                 " <img src='https://example.com/image3.gif'>")
    html_ = re.search(image_, html_text)
    searching_iterator = re.finditer(image_, html_text)
    for matched in searching_iterator:
        print(f'Cовпадение: {matched.group()}')


extract_image_links('text')