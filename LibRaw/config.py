{

	"downloads" : [

		"https://www.libraw.org/data/LibRaw-0.21.3.tar.gz",

	],

	"url" : "https://www.libraw.org/",

	"license" : "LICENSE.LGPL",
    
	"environment" : {

		"CPPFLAGS" : "-I{buildDir}/include -I/usr/local/include",
		"LDFLAGS" : "-L{buildDir}/lib -L/usr/local/lib",

	},
	"commands" : [

		"./configure --disable-examples --prefix={buildDir}",
		"make -j {jobs}",
		"make install"

	],

	"manifest" : [

		"include/libraw",
		"lib/libraw*{sharedLibraryExtension}*",

	],

}
