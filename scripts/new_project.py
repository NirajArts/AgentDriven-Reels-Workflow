"""Copy the project template to the next unused ProjectNNN directory."""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--number', type=int, help='Optional explicit project number')
    args = parser.parse_args()
    projects = ROOT / 'Projects'
    projects.mkdir(exist_ok=True)
    number = args.number
    if number is None:
        number = 1
        while (projects / f'Project{number:03d}').exists():
            number += 1
    if not 1 <= number <= 9999:
        parser.error('Project number must be between 1 and 9999.')
    destination = projects / f'Project{number:03d}'
    if destination.exists():
        parser.error('Destination already exists; nothing was changed.')
    # copytree refuses an existing destination, including a concurrent creator.
    shutil.copytree(ROOT / 'Templates/Project', destination)
    print(f'Created Projects/{destination.name}. Start with Docs/Brief.md.')

if __name__ == '__main__':
    main()
