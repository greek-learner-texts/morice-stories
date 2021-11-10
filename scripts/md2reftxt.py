#!/usr/bin/env python3

import re

lines = open("orig/morice.md").readlines()

story_num = 0
paragraph_num = 0
for line in lines[33:]:
    if m := re.match(r"### (.+)$", line):
        story_num += 1
        section_num = 0
        story_title = m.group(1)
        print(f"{story_num:03d}.00.000 {story_title}")
    elif m := re.match(r"#### (\d+)\. (.+)$", line):
        section_num += 1
        section_title = m.group(2)
        assert int(m.group(1)) == section_num
        print(f"{story_num:03d}.{section_num:02d}.000 {section_title}")
    elif m := re.match(r"\n$", line):
        pass
    elif m := re.match(r"(\d+)\. (.+)$", line):
        paragraph_num += 1
        text = m.group(2)
        assert int(m.group(1)) == paragraph_num
        print(f"{story_num:03d}.{section_num:02d}.{paragraph_num:03d} {text}")
    else:
        print(line)
        print("@@@")
        quit()
