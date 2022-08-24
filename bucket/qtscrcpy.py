{
    "homepage": "https://github.com/barry-ran/QtScrcpy",
    "description": "QtScrcpy connects to Android devices via USB (or via TCP/IP) for display and control. It does NOT require the root privileges.",
    "version": "2.0.1",
    "license": "Apache-2.0",
    "architecture": {
        "64bit": {
            "url": "https://github.com/barry-ran/QtScrcpy/releases/download/v2.0.1/QtScrcpy-win-x64-v2.0.1.zip",
            "hash": "f0385bbe91771b648bd26ad3e959ab5b8c9d6bc4ff307897f7c591f7f4050fce",
            "extract_dir": "QtScrcpy-win-x64-v2.0.1"
        },
        "32bit": {
            "url": "https://github.com/barry-ran/QtScrcpy/releases/download/v2.0.1/QtScrcpy-win-x86-v2.0.1.zip",
            "hash": "e3ee05e7aba1d9e6b73d6f1ff4fcb681fa3566df7ab4354563ae8ad18484747e",
            "extract_dir": "QtScrcpy-win-x86-v2.0.1"
        }
    },
    "bin": "QtScrcpy.exe",
    "shortcuts": [
        [
            "QtScrcpy.exe",
            "QtScrcpy"
        ]
    ],
    "checkver": "github",
    "autoupdate": {
        "architecture": {
            "64bit": {
                "url": "https://github.com/barry-ran/QtScrcpy/releases/download/v$version/QtScrcpy-win-x64-v$version.zip",
                "extract_dir": "QtScrcpy-win-x64-v$version"
            },
            "32bit": {
                "url": "https://github.com/barry-ran/QtScrcpy/releases/download/v$version/QtScrcpy-win-x86-v$version.zip",
                "extract_dir": "QtScrcpy-win-x86-v$version"
            }
        }
    }
}