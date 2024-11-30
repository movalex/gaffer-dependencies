{

	"downloads" : [

		"https://github.com/OpenImageIO/oiio/archive/refs/tags/v2.5.10.1.tar.gz"

	],

	"url" : "http://www.openimageio.org",

	"license" : "LICENSE.md",

	"dependencies" : [ "Boost", "Python", "PyBind11", "OpenEXR", "LibTIFF", "LibPNG", "OpenJPEG", "LibJPEG-Turbo", "OpenColorIO", "LibRaw", "PugiXML", "Fmt", "LibWebP", "TBB", "FreeType" ],

	"environment" : {

		"PATH" : "/usr/local/opt/openimageio/bin:$PATH",
		"LD_LIBRARY_PATH" : "/usr/local/opt/openimageio/lib:$LD_LIBRARY_PATH"

	},

	"commands" : [

		# Skip building and directly use the Homebrew installation
		"echo 'Using Homebrew-installed OpenImageIO'",

		# Ensure required directories exist in the expected build directory
		# "mkdir -p {buildDir}/include",
		# "mkdir -p {buildDir}/lib",
		# "mkdir -p {buildDir}/bin",

		# Symlink Homebrew-installed OpenImageIO files to {buildDir}
		"ln -sf /usr/local/opt/openimageio/include/OpenImageIO {buildDir}/include/OpenImageIO",
		"ln -sf /usr/local/opt/openimageio/lib/libOpenImageIO* {buildDir}/lib/",
		"ln -sf /usr/local/opt/openimageio/bin/* {buildDir}/bin/"

	],

	"variables" : {

		"extraCommands" : "",

	},

	"manifest" : [

		"bin/maketx",
		"bin/oiiotool",

		"include/OpenImageIO",
		"lib/libOpenImageIO*{sharedLibraryExtension}*",

		"doc/openimageio.pdf"

	],

	"platform:macos" : {

		"variables" : {

			"extraCommands" : "ln -sf /usr/local/opt/openimageio/lib/python{pythonVersion}/site-packages/OpenImageIO {pythonLibDir}/python{pythonVersion}/site-packages/OpenImageIO"

		}

	}

}

