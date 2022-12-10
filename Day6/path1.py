from pathlib import Path


base = Path.home()
guide = Path(base,'Europe','France',Path('Paris', 'Eiffel_Tower.txt'))
guide2 = guide.with_name('Notre_Dame')
print(guide.parent)