{

	"downloads" : [

		"https://github.com/uxlfoundation/oneTBB/releases/download/v2022.0.0/oneapi-tbb-2022.0.0-mac.tgz"

	],

	"url" : "http://threadingbuildingblocks.org/",

	"license" : "LICENSE.txt",

	"commands" : [
        
		"mkdir -p {buildDir}/include",
		"cp -r include/tbb {buildDir}/include",
		"cp -r include/oneapi {buildDir}/include",
		"mkdir -p {buildDir}/lib",
		"{installLibsCommand}",

	],

	"manifest" : [

		"include/tbb",
		"lib/libtbb*{sharedLibraryExtension}*",

	],

	"platform:linux" : {

		"environment" : {

			"tbb_os" : "linux",

		},

		"variables" : {

			"installLibsCommand" : "cp build/*_release/*.so* {buildDir}/lib",

		},

	},

	"platform:macos" : {

		"environment" : {

			"tbb_os" : "macos",

		},

		"variables" : {

			"installLibsCommand" : "cp lib/*.dylib {buildDir}/lib",

		},

	},

}
