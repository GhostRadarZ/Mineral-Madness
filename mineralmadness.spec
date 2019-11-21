# -*- mode: python -*-

block_cipher = None

spec_root = os.path.abspath(SPECPATH)

a = Analysis(['src//mineralmadness.py'],
             pathex=[spec_root],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

toc = Tree('./src', excludes=['*.py', 'build', '__pycache__', 'dist', '*.spec'])
a.datas += toc;

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mineralmadness',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon=os.path.join(spec_root, 'logo.ico'))
