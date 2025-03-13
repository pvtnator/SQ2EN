# Succubus and the Blank Book translation project.
Partially edited MTL, partially manual translation using a combination of many tools and basic understanding of Japanese, and a lot of cross-checking for names and references.
Feel free to report issues and provide feedback either here in the Issues section, the F95/ULMF thread or wherever you see me.

### Original work by SQDT. The official game is required to apply this patch.

## Progress
Everything is translated. 

## Installation Instructions
You can either patch it from source or apply the latest release version.
It is recommended to get the latest release version from the releases section on the right side of the page.
In this case, follow these steps:

1. Download and extract the zip. ApplyPatch.bat and ENPatchData should be in the game installation folder (where the .exe is).
2. Run ApplyPatch.
3. A prompt will open to input password.
   Drag and drop SQT_Battle(Stella).mp3 (from Audio/BGM) 
   to the input field and click decrypt, and close the prompt when it's done.
4. The rest of it should complete automatically.

Further details can be found in the readme included in the zip file.

## Patching Instructions
This project uses RPGMaker Trans https://rpgmakertrans.bitbucket.io/index.html.
For easier patching, get the command line (CLI) version.
In addition, some python scripts. Make sure to have up to date Python installed (3.5+ is fine I think).

1. Have unmodified latest version of the game (sqt2.1.0 in SQ_Patch.rb)
2. Place RPGMaker Trans into a folder called "rpgmt_cli_v4.5" such that this and the game folder are in the same directory.
4. Run the "patch.bat", which will execute "patcher.py" with python.
   If your python goes by "python3", try editing the .bat. You can also run those scripts directly yourself.
5. Now the game should be decrypted and the individual files are in the data folder.
   In the unpatched game's root folder, rename the files starting with "Q_" so you remove that prefix, then copy them to the data folder.
   These are patch files, but we need them in the data folder so they get translated.
   Now patch the game again.
6. After updates, apply the patches the same way. No need to delete the game or anything, normally at least.

Note that as things are, this won't modify your saves, and your saves contain some strings, which leads to some bugs.
In other words, it's best to start a new save after applying this mod, but as far as I know, the bugs should be minor in this case.
Note also that when you load a save, the current map is loaded from the save and changes won't be applied until you re-enter that map.
