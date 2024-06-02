def styling_text(text, fontPt=None, fontWeight=None, color="#000000"):
    beginning = "<html><head/><body><p>"
    end = "</p></body></html>"
    styles = str()
    if (fontPt != None):
        styles += f"font-size:{fontPt};"
    if (fontWeight != None):
        styles += f"font-weight:{fontWeight};"

    text_with_style = f"<span style=\"{styles}color:{color};\">{text}</span>"

    return beginning + text_with_style + end
