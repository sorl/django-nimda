$( document ).ready(function() {
  var $changelistForm = $('#changelist-form')
  var $changelistFormCheckboxes = $changelistForm.find('input[type=checkbox]')

  $changelistFormCheckboxes.on('change', function(e) {
    if ( $changelistFormCheckboxes.is(':checked') ) {
      $changelistForm.find('.actions').slideDown(200)
    } else {
      $changelistForm.find('.actions').slideUp(100)
    }
  })
});