'use strict';

var gulp = require('gulp'),
	connect = require('gulp-connect'),
	scss = require('gulp-sass'),
	sourcemaps = require('gulp-sourcemaps'),
	autoprefixer = require('gulp-autoprefixer'),
	concat = require('gulp-concat');

var externalDeps = [
		'./bower_components/jquery/dist/jquery.min.js',
		'./bower_components/angularjs/angular.min.js',
		'./bower_components/materialize/dist/js/materialize.min.js',
		'./bower_components/bootstrap/dist/js/bootstrap.min.js',
		'./bower_components/angular-rangeslider/angular.rangeSlider.js'
]


gulp.task('scss', function(){
	gulp.src('./static/sass/*.scss')
		//.pipe(concat('main.scss'))
		.pipe(sourcemaps.init())
		.pipe(scss().on('error', scss.logError))
		.pipe(sourcemaps.write('/maps/'))
		.pipe(gulp.dest('static/css'))
		.pipe(connect.reload());
});




gulp.task('css', function () {
  gulp.src('./static/css/*.css')
  // .pipe(sourcemaps.init())
    .pipe(connect.reload());
});

gulp.task('js', function () {
  gulp.src('./static/js/*.js')
  .pipe(concat('scripts.js'))
		  .pipe(gulp.dest('static/build'));
});

gulp.task('extjs', function () {
  gulp.src(externalDeps)
  .pipe(concat('externalDeps.js'))
		  .pipe(gulp.dest('static/build'));
});

gulp.task('prefixe', function(){
	gulp.src('./static/css/*.css')
	.pipe(autoprefixer({
	    browsers: ['last 15 versions'],
	    cascade: false
	}))
	.pipe(gulp.dest('static/css'));
})


gulp.task('watch', function() {
	//gulp.watch(['./static/templates/*.html'],['html']);
	gulp.watch(['./static/css/*.css'], ['css']);
	gulp.watch(['./static/sass/*.scss'], ['scss']);
	gulp.watch(['./static/js/*.js'], ['js']);
	gulp.watch(externalDeps, ['extjs']);
});

gulp.task('default', ['extjs','js','watch']);