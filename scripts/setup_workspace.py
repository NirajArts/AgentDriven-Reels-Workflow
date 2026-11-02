"""Create private configuration from public templates without overwriting."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    for source, target in [('.env.example', '.env'),
                           ('elevenlabs_voice_id.example.txt', 'elevenlabs_voice_id.txt')]:
        content = (ROOT / source).read_text(encoding='utf-8')
        try:
            with (ROOT / target).open('x', encoding='utf-8') as stream:
                stream.write(content)
            print(f'Created {target}; fill your own values locally.')
        except FileExistsError:
            print(f'Kept existing {target}.')
    print('No downloads, network requests or app launches were performed.')

if __name__ == '__main__':
    main()
