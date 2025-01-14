# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['penpalmain.py'],
    pathex=['C:\\Users\\raque\\OneDrive\\Documents\\PENPAL\\PENPAL-main'],
    binaries=[],
    datas=[
        ('resources', 'resources'),
        ('BACKEND', 'BACKEND'),
        ('FRONTEND', 'FRONTEND'),
        ('README.txt', 'README.txt'),
        ('requirements.txt', 'requirements.txt'),
        ('credentials.bak', 'credentials.bak'),
        ('credentials.dir', 'credentials.dir'),
        # Add other necessary files and directories here
    ],
    hiddenimports=[
        'shelve',
        'mysql',
        'mysql.connector',
        'mysql.connector.errorcode',
        'mysql.connector.connection',
        'mysql.connector.cursor',
        'requests',
        'argon2',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='penpalmain',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)