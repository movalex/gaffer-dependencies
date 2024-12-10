{

	"downloads" : [

		"https://download.osgeo.org/libtiff/tiff-4.7.0.zip",

	],

	"url" : "http://www.libtiff.org",

	"license" : "LICENSE.md",

	"dependencies" : [ "LibJPEG-Turbo", "LibWebP"],

	"environment" : {

		# Needed to make sure we link against the libjpeg
		# in the Gaffer distribution and not the system
		# libjpeg.
		"CPPFLAGS" : "-I{buildDir}/include",
		"LDFLAGS" : "-L{buildDir}/lib -L/usr/local/lib",

	},

	"commands" : [

		"./configure --without-x --prefix={buildDir}",
		"make -j {jobs}",
		"make install"

	],

	"manifest" : [

		"include/tiff*",
		"lib/libtiff*{sharedLibraryExtension}*",

	],

}
