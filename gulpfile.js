'use strict';

// Load npm modules
var gulp = require('gulp');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');

// Files and folders
var stylesWatch = ['./src/static/src/styles/**/*'];

var stylesSrc = [
  './src/static/bower_components/cookieconsent/build/cookieconsent.min.css',
  './src/static/src/styles/main.scss'
];

var scriptsWatch = ['./src/static/src/scripts/**/*.js'];

var scriptsSrc = [
  './src/static/bower_components/jquery/dist/jquery.js',
  './src/static/bower_components/Materialize/dist/js/materialize.js',
  './src/static/bower_components/cookieconsent/build/cookieconsent.min.js',
  './src/static/src/scripts/**/*.js'
];

var stylesDest = './src/static/dist/css/';
var scriptsDest = './src/static/dist/js/';

// Sass
gulp.task('styles', function() {
  return gulp.src(stylesSrc)
    .pipe(concat('main.min.css'))
    .pipe(sourcemaps.init())
      .pipe(sass({outputStyle: 'compressed'}))
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest(stylesDest));
});

// Javascript
gulp.task('scripts', function() {
  return gulp.src(scriptsSrc)
    .pipe(sourcemaps.init())
      .pipe(concat('main.min.js'))
      .pipe(uglify())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest(scriptsDest));
});

// Watch styles
gulp.task('watch:styles', function() {
  gulp.watch(stylesWatch, ['styles']);
});

// Watch scripts
gulp.task('watch:scripts', function() {
  gulp.watch(scriptsWatch, ['scripts']);
});

// Watches
gulp.task('watches', function() {
  gulp.watch(stylesWatch, ['styles']);
  gulp.watch(scriptsWatch, ['scripts']);
});

// Default
gulp.task('default', ['styles', 'scripts']);
