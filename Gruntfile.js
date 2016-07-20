/**
 * Grunt project configuration.
 */
module.exports = function(grunt) {
    // configuration for the plugins.
    grunt.initConfig({
        concat: {
            options: {
                sourceMap: false
            },
            "positional-filter" : {
                files: [{
                    src: ["js/locators/positional-filter.js"],
                    dest: "germanium/locators/positional-filter.js"
                }]
            },
            "inside-filter" : {
                files: [{
                    src: ["js/locators/inside-filter.js"],
                    dest: "germanium/locators/inside-filter.js"
                }]
            }
        },

        uglify: {
            options: {
                bare_returns: true,
                mangle: true,
                compress: true
            },
            "positional-filter" : {
                files: {
                    "germanium/locators/positional-filter.min.js" : [
                        "germanium/locators/positional-filter.js"
                    ]
                }
            },
            "inside-filter" : {
                files: {
                    "germanium/locators/inside-filter.min.js" : [
                        "germanium/locators/inside-filter.js"
                    ]
                }
            }
        }
    });

    // load NPM tasks:
    // grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-contrib-concat");
    grunt.loadNpmTasks("grunt-contrib-uglify");

    // register our tasks:
    grunt.registerTask("default", ['concat', 'uglify']);
};
