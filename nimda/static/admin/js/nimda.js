String.prototype.format = function() {
  var args = arguments
  return this.replace(/{(\d+)}/g, function(match, j) {
    return args[j]
  })
}
