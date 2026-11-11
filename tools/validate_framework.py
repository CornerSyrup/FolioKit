"""Validate this framework's schemas, templates and internal Markdown links.
Does not certify generated images or a production workshop.
"""
import json
import re
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT = Path(__file__).resolve().parent.parent

def validate(root=ROOT):
    count = 0
    for path in sorted((root / 'schemas').glob('*.schema.json')):
        schema = json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        name = path.name.removesuffix('.schema.json')
        record = json.loads((root / 'templates' / (name + '.json')).read_text(encoding='utf-8'))
        Draft202012Validator(schema).validate(record)
        count += 1
    for path in root.rglob('*.md'):
        for link in re.findall(r'`((?:prompts|specs|tools)/[^` ]+\.(?:md|py))`', path.read_text(encoding='utf-8')):
            if not (root / link).is_file():
                raise ValueError(f'Missing internal reference: {path}: {link}')
    return count

if __name__ == '__main__':
    n = validate()
    print(f'PASS: {n} schemas, {n} draft templates and internal file references.')
    print('NOT CHECKED: production readiness, image fidelity, assembly, PDF or HTML behaviour.')
