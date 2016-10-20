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
            "locators/positional-filter" : {
                files: [{
                    src: ["js/locators/positional-filter.js"],
                    dest: "germanium/locators/positional-filter.js"
                }]
            },
            "locators/inside-filter" : {
                files: [{
                    src: ["js/locators/inside-filter.js"],
                    dest: "germanium/locators/inside-filter.js"
                }]
            },
            "util/child-nodes" : {
                files: [{
                    src: ["js/util/child-nodes.js"],
                    dest: "germanium/util/child-nodes.js"
                }]
            },
            "points/box" : {
                files: [{
                    src: ["js/points/box.js"],
                    dest: "germanium/points/box.js"
                }]
            }
        },

        uglify: {
            options: {
                bare_returns: true,
                mangle: true,
                compress: true
            },
            "locators/positional-filter" : {
                files: {
                    "germanium/locators/positional-filter.min.js" : [
                        "germanium/locators/positional-filter.js"
                    ]
                }
            },
            "locators/inside-filter" : {
                files: {
                    "germanium/locators/inside-filter.min.js" : [
                        "germanium/locators/inside-filter.js"
                    ]
                }
            },
            "util/child-nodes" : {
                files: {
                    "germanium/util/child-nodes.min.js" : [
                        "germanium/util/child-nodes.js"
                    ]
                }
            },
            "points/box" : {
                files: {
                    "germanium/points/box.min.js" : [
                        "germanium/points/box.js"
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
