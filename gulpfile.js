var gulp = require('gulp')
var sass = require('gulp-sass')
var sourcemaps = require('gulp-sourcemaps')


gulp.task('build', function () {
  gulp.src('./scss/*.scss')
    .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest('./nimda/static/admin/css'))

  gulp.src('./js/*.js')
    .pipe(gulp.dest('./nimda/static/admin/js'))
})


gulp.task('default', function () {
  gulp.watch('./scss/*.scss', ['build'])
  gulp.watch('./js/*.js', ['build'])
})
