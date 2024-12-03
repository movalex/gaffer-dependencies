{

	"downloads" : [

		"https://github.com/RenderKit/embree/releases/download/v4.3.3/embree-4.3.3.x86_64.macosx.zip"
	],

	"url" : "https://www.embree.org/",

	"dependencies" : [ "TBB" ],

	"commands" : [
		"rsync -av ./* {buildDir}",
        "wget https://raw.githubusercontent.com/RenderKit/embree/refs/heads/master/LICENSE.txt",
        "cp LICENSE.txt {buildDir}/doc/licenses/Embree"
	],

	"manifest" : [

		"include/embree4",

		"lib/libembree4*{sharedLibraryExtension}*",

	],

}
