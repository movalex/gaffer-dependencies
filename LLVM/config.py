{

	"downloads" : [

		"https://github.com/llvm/llvm-project/releases/download/llvmorg-19.1.3/LLVM-19.1.3-macOS-X64.tar.xz",

	],

	"url" : "https://llvm.org",

	"commands" : [
		"rsync -av ./* {buildDir}",
		"wget https://raw.githubusercontent.com/llvm/llvm-project/refs/heads/main/LICENSE.TXT",
        "cp LICENSE.TXT {buildDir}/doc/licenses/LLVM"
	],

	"variables" : {

		"buildTargets" : "'Native'",

	},

	"platform:linux" : {

		"variables" : {

			"buildTargets" : "'Native;NVPTX'",

		},

	},

}
