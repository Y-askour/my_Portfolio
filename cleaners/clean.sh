echo "remove .swp files : y or n"
read var
if  [ $var == 'y' ]
then
	rm -rf .*.swp
fi

echo "remove .swo files : y or n"
read var
if  [ $var == 'y' ]
then
	rm -rf .*.swo
fi

echo "remove .dSYM files : y or n"
read var
if  [ $var == 'y' ]
then
		rm -rf *.dSYM
fi

echo "remove trash macos files : y or n"
read var
if  [ $var == 'y' ]
then
			rm -rf *.DS_Store
			rm -rf *.AppleDouble
			rm -rf *.LSOverride
			rm -rf *.LSOverride
			rm -rf *.LSOverride
			rm -rf *.LSOverride
			rm -rf .DocumentRevisions-V100 .fseventsd .Spotlight-V100 .TemporaryItems .Trashes .VolumeIcon.icns .com.apple .timemachine.donotpresent __MACOSX
			rm -rf .vscode
			rm -rf .config
			rm -rf .Trash
			rm -rf .lldb
			rm -rf .npm
			rm -rf .viminfo
			rm -rf .fig
			rm -rf .zcomp*
			rm -rf .zsh_history

fi


