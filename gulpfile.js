'use strict';

/**
 * Load npm modules
 */
const gulp = require('gulp');
const babel = require('gulp-babel');
const concat = require('gulp-concat');
const sass = require('gulp-sass');
const sourcemaps = require('gulp-sourcemaps');
const uglify = require('gulp-uglify');

/*****************************************************************************/

/**
 * Styles.
 */
const stylesWatch = ['./src/static/src/styles/**/*'];
const stylesSrc = [
  './src/static/bower_components/cookieconsent/src/styles/**/*.css',
  './src/static/src/styles/main.scss',
];
const stylesDest = './src/static/dist/css/';

/**
 * Scripts locales.
 */
const scriptsWatch = ['./src/static/src/scripts/**/*.js'];
const scriptsSrc = ['./src/static/src/scripts/**/*.js'];
const scriptsDest = './src/static/dist/js/';

/**
 * Scrtips de terceros.
 */
const scriptsVendorSrc = [
  './src/static/bower_components/jquery/dist/jquery.js',
  './src/static/bower_components/Materialize/dist/js/materialize.js',
  './src/static/bower_components/cookieconsent/src/cookieconsent.js',
];

/******************************************************************************
 * Copy files.
 */
gulp.task('copy', () => {
  /**
   * Fuentes.
   *
   * Material icons se ha de descargar manualmente.
   * @ver: src/static/src/styles/_material-icons.scss.
   */
  // Roboto de materialize.
  gulp.src(['./bower_components/Materialize/fonts/**/*'])
    .pipe(gulp.dest('./src/static/dist/fonts'));

  // font-awesome.
  gulp.src(['./bower_components/font-awesome/fonts/**/*'])
    .pipe(gulp.dest('./src/static/dist/fonts/font-awesome'));

  /**
   * Imágenes.
   */
  // Imágenes del proyecto.
  gulp.src(['./src/static/src/img/**/*'])
    .pipe(gulp.dest('./src/static/dist/img'));
});

/******************************************************************************
 * Styles.
 */

/**
 * Sass desarrollo.
 */
gulp.task('styles:dev', () => {
  gulp.src(stylesSrc)
    .pipe(concat('main.css'))
    .pipe(sourcemaps.init())
      .pipe(sass())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest(stylesDest));
});

/**
 * Sass producción.
 */
gulp.task('styles:prod', () => {
  gulp.src(stylesSrc)
    .pipe(concat('main.min.css'))
    .pipe(sass({outputStyle: 'compressed'}))
    .pipe(gulp.dest(stylesDest));
});

/*****************************************************************************
 * Javascript locales.
 */

/**
 * Javascript locales, desarrollo.
 */
gulp.task('scripts:local:dev', () => {
  gulp.src(scriptsSrc)
    .pipe(concat('main.js'))
    .pipe(sourcemaps.init())
      .pipe(babel({
        presets: ['es2015']
      }))
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest(scriptsDest));
});

/**
 * Javascript locales, producción.
 */
gulp.task('scripts:local:prod', () => {
  gulp.src(scriptsSrc)
    .pipe(concat('main.min.js'))
    .pipe(babel({
      presets: ['es2015']
    }))
    .pipe(uglify())
    .pipe(gulp.dest(scriptsDest));
});

/******************************************************************************
 * Javascript terceros.
 */

/**
 * Javascript terceros, desarrollo.
 */
gulp.task('scripts:third:dev', () => {
  gulp.src(scriptsVendorSrc)
    .pipe(concat('vendor.js'))
    .pipe(sourcemaps.init())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest(scriptsDest));
});

/**
 * Javascript terceros, producción.
 */
gulp.task('scripts:third:prod', () => {
  gulp.src(scriptsVendorSrc)
    .pipe(concat('vendor.min.js'))
    .pipe(uglify({
      output: {
        max_line_len: 100000
      }
    }))
    .pipe(gulp.dest(scriptsDest));
});

/******************************************************************************
 * Los Watch solo son para archivos locales y desarrollo.
 */

// Watch styles
gulp.task('watch:styles', () => {
  gulp.watch(stylesWatch, ['styles:dev']);
});

// Watch scripts
gulp.task('watch:scripts', () => {
  gulp.watch(scriptsWatch, ['scripts:local:dev']);
});

// Watches
gulp.task('watches', () => {
  gulp.watch(stylesWatch, ['styles:dev']);
  gulp.watch(scriptsWatch, ['scripts:local:dev']);
});

// Producción.
gulp.task('prod', ['styles:prod', 'scripts:third:prod', 'scripts:local:prod']);

// Desarrollo.
gulp.task('dev', ['styles:dev', 'scripts:third:dev', 'scripts:local:dev']);

// Default.
gulp.task('default', ['copy', 'prod', 'dev']);
