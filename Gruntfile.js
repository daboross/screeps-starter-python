module.exports = function (grunt) {

    grunt.loadNpmTasks('grunt-screeps');

    grunt.initConfig({
        screeps: {
            options: {
                // Trim right in order to remove any newlines at the end of the files.
                email: grunt.file.read('./.screeps-email').trimRight(),
                password: grunt.file.read('./.screeps-password').trimRight(),
                branch: grunt.option('branch') || 'v2',
                ptr: grunt.option('ptr') || false
            },
            dist: {
                src: ['dist/*.js']
            }
        }
    });
};
