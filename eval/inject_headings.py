#!/usr/bin/env python3
"""Inject canonical layer headings into pdftotext-flattened gold paper.md.

Strategy: search for common section markers as substrings, inject `## <heading>` before each.
Uses layer-keyword-bearing heading names so the instrumentation layer classifier matches them.
"""
import re
import sys

# Patterns to detect and the canonical layer heading to inject.
# Order matters: more specific patterns first.
INJECTIONS = [
    # Abstract
    ('Abstract\n', 'Abstract'),
    ('\nA BST R A C T', 'Abstract'),
    ('ABSTRACT\n', 'Abstract'),
    # Introduction
    ('1. Introduction', 'Introduction'),
    ('1 Introduction', 'Introduction'),
    ('\nIntroduction\n', 'Introduction'),
    ('\nINTRODUCTION', 'Introduction'),
    # Conceptual framework / Related work
    ('Related Work', 'Conceptual Framework: Related Work'),
    ('Related work', 'Conceptual Framework: Related Work'),
    ('Background and related', 'Conceptual Framework: Background and Related Work'),
    ('Background\n', 'Conceptual Framework: Background'),
    ('Theoretical Framework', 'Conceptual Framework'),
    ('Conceptual Framework', 'Conceptual Framework'),
    # The work
    ('The Artwork', 'The Work'),
    ('The Installation', 'The Work and Installation'),
    ('The Work', 'The Work'),
    ('Description of the', 'The Work and Description'),
    # Realization / Implementation / System / Method
    ('Implementation\n', 'Realization: Implementation'),
    ('System Architecture', 'Realization: System Architecture'),
    ('Method\n', 'Realization: Method'),
    ('Methods\n', 'Realization: Methods'),
    ('Methodology\n', 'Realization: Methodology'),
    ('Technical', 'Realization: Technical Setup'),
    # Discussion / Reflection
    ('Discussion\n', 'Discussion'),
    ('\nDiscussion ', 'Discussion'),
    ('Reflection\n', 'Reflection and Discussion'),
    ('Findings\n', 'Discussion: Findings'),
    # Conclusion
    ('Conclusion\n', 'Conclusion'),
    ('Conclusions\n', 'Conclusion'),
    ('\nCONCLUSION', 'Conclusion'),
    # References / Acknowledgments / Author bio (boundaries)
    ('References\n', 'References'),
    ('Acknowledgments', 'Acknowledgments'),
    ('Acknowledgements', 'Acknowledgements'),
    ('Author Biography', 'Author Biography'),
    ('Author(s) Biography', 'Author Biography'),
    ('Author Bios', 'Author Biographies'),
]


def inject(path: str) -> None:
    text = open(path).read()
    already = set()
    for line in text.splitlines():
        if line.startswith('##'):
            already.add(line.strip())
    injected = []
    for frag, head in INJECTIONS:
        head_line = f'## {head}'
        if head_line in already:
            continue
        pos = text.find(frag)
        if pos == -1:
            continue
        text = text[:pos] + f'\n\n{head_line}\n\n' + text[pos:]
        already.add(head_line)
        injected.append(head)

    with open(path, 'w') as fp:
        fp.write(text)

    final = [ln.rstrip() for ln in text.splitlines() if ln.startswith('#')]
    print(f'{path}:')
    for ln in final:
        print(f'  {ln[:100]}')
    print(f'  ({len(injected)} new injections)')
    print()


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        inject(arg)
