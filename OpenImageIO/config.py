{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/refs/tags/v2.5.14.0.tar.gz"

	],

	"url" : "http://www.openimageio.org",

	"license" : "LICENSE.md",

	"dependencies" : [ "Boost", "Python", "PyBind11", "OpenEXR", "LibTIFF", "LibPNG", "OpenJPEG", "LibJPEG-Turbo", "OpenColorIO", "LibRaw", "PugiXML", "Fmt", "LibWebP", "TBB", "FreeType" ],

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",
        "PKG_CONFIG_PATH": "{buildDir}/lib/pkgconfig:$PKG_CONFIG_PATH",
		"CPPFLAGS" : "-I{buildDir}/include -I/usr/local/include",
		"LDFLAGS" : "-L{buildDir}/lib -L/usr/local/lib",

	},

	"commands" : [
		# "sh src/build-scripts/build_libpng.bash",
		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_CXX_STANDARD=17"
            " -D CMAKE_CXX_FLAGS=-std=c++17"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D USE_FFMPEG=NO"
			" -D USE_GIF=0"
			" -D USE_OPENVDB=NO"
			" -D USE_PYTHON=YES"
			" -D USE_EXTERNAL_PUGIXML=YES"
			" -D BUILD_MISSING_FMT=NO"
			" -D OIIO_BUILD_TESTS=NO"
			" -D OIIO_DOWNLOAD_MISSING_TESTDATA=NO"
			" -D PYTHON_VERSION={pythonMajorVersion}"
			" -D Python_ROOT_DIR={buildDir}"
			" -D Python_FIND_STRATEGY=LOCATION"
			# These next two disable `iv`. This fails to
			# build on Mac due to OpenGL deprecations, and
			# we've never packaged it anyway.
			" -D USE_OPENGL=NO"
			" -D USE_QT=NO"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",
		"{extraCommands}",

	],

	"variables" : {

		"extraCommands" : "",

	},

	"manifest" : [

		"bin/maketx",
		"bin/oiiotool",

		"include/OpenImageIO",
		"lib/libOpenImageIO*{sharedLibraryExtension}*",

		"doc/openimageio.pdf",

	],

	"platform:macos" : {

		"variables" : {

			"extraCommands" : "mv {buildDir}/lib/python{pythonVersion}/site-packages/OpenImageIO {pythonLibDir}/python{pythonVersion}/site-packages/OpenImageIO"

		},

	},

}
