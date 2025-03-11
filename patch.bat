xcopy ".\PrePatch\Data" "..\Succubus and the Blank Book\Data" /E /H /C /I /Y
"../rpgmt_cli_v4.5/rpgmt.exe" "..\Succubus and the Blank Book"
python patcher.py apply
python mapConditionReplace.py