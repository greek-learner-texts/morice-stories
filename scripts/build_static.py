WORK_LIST = ["preface", "hints", "morice"]
TITLES = {"preface": "Preface", "hints": "Hints to Beginners", "morice": "Stories in Attic Greek"}

for WORK in WORK_LIST:
    print("processing", WORK)
    SRC = f"../text/{WORK}.txt"
    DEST = f"../docs/{WORK}.html"
    TITLE = TITLES[WORK]
    HEADER = f"""\
    <!DOCTYPE html>
    <html lang="grc">
    <meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css?family=Noto+Serif:400,700&amp;subset=greek,greek-ext" rel="stylesheet">
    <link rel="stylesheet"
    <link href="style.css" rel="stylesheet">
    </head>
    <body>
      <div class="container alpheios-enabled" lang="grc">
      <nav>&#x2191; <a href="./">Morice Stories in Attic Greek</a></nav>
    """
    FOOTER = """\
        <br/><br/>
        <nav>&#x2191; <a href="./">Morice Stories in Attic Greek</a></nav>
        <br/>
        <p>This work is licensed under a <a href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.</p>
        <p>The source is available at <a href="https://github.com/greek-learner-texts/morice-stories">https://github.com/greek-learner-texts/morice-stories</a>.</p>
        </div>
    </body>
    </html>
    """
# 
# first number = story or section in Hints
# second number 00 = standalone story, section in later longer stories. 
# 128.00.000 TROUBLES IN CORCYRA - story 128, main title
# 128.01.000 Prosecution of Peithias, and his revenge - story 128, section 1, 000 = section title
# third number = continuous paragraph number
    with open(SRC, encoding="utf-8") as f:
        with open(DEST, "w", encoding="utf-8") as g:
            prev_section = None
            prev_chapter = None
            print(HEADER, file=g)
            for line in f:
                parts = line.strip().split(maxsplit=1)
                ref = parts[0].split(".")
                if len(ref) == 2:
                    section = None
                    chapter, verse = ref
                else:
                    section, chapter, verse = ref
                if prev_section != section:
                    if prev_section is not None:
                        print("   </div>""", file=g)
                        print("   </div>""", file=g)
                    print("""   <div class="section">""", file=g)
                    prev_section = section
                    prev_chapter = None
                if prev_chapter != chapter:
                    if prev_chapter is not None:
                        if prev_chapter == "0":
                            if section is None:
                                print("""    </div>""", file=g)
                        else:
                            print("""    </div>""", file=g)
                    if chapter == "0":
                        if section is None:
                            print("""    <div class="preamble">""", file=g)
                    else:
                        if chapter == "SB":
                            print(f"""    <div class="subscription">{parts[1]}""", file=g)
                        elif chapter == "EP":
                            print("""    <div class="epilogue">""", file=g)
                        else:
                            print("""    <div class="chapter">""", file=g)
                            print(f"""      <h3 class="chapter_ref">{parts[1]}</h3>""", file=g)
                    prev_chapter = chapter
                
                else:
                    if chapter == "EP" and verse == "0":
                        print(f"""<h3 class="epilogue_title">{parts[1]}</h3>""", file=g)
                    else:
                        if verse != "0":
                            print(f"""      <span class="verse_ref">{verse}</span>""", end="&nbsp;", file=g)
                        print(parts[1], file=g)
            print("""    </div>""", file=g)
            if section is not None:
                print("""    </div>""", file=g)
            print(FOOTER, file=g)
print("Finished!\a")