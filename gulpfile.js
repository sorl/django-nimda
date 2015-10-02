var gulp = require('gulp')
var sass = require('gulp-sass')


gulp.task('build', function () {
  gulp.src('./scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./nimda/static/admin/css'))
})


gulp.task('default', function () {
  gulp.watch('./scss/*.scss', ['build'])
})
