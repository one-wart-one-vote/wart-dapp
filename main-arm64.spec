# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='wart-dapp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='wart-dapp'
)

app = BUNDLE(
    coll,
    name='wart-dapp.app',
    icon=None,
    bundle_identifier='com.wart.dapp',
    info_plist={
        'CFBundleName': 'Wart DApp',
        'CFBundleDisplayName': 'Wart DApp',
        'CFBundleExecutable': 'wart-dapp',
        'CFBundlePackageType': 'APPL',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
        'LSBackgroundOnly': False,
        'LSMinimumSystemVersion': '10.15',
    }
)