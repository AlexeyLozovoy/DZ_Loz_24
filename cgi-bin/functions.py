def header(title, name):
    print('COntent-type text/html')
    print('')

    with open('master.html', 'r') as html:
        print(html.read())
    
    with open('header.html', 'r') as html:
        print(html.read())

    with open(name, 'r') as html:
        print(html.read())

    with open('footer.html', 'r') as html:
        print(html.read())

    return print(f"<title>{title}</title>")
