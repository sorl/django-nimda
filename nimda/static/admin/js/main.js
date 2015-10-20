$( document ).ready(function() {
  var $changelistForm = $('#changelist-form')
  var $changelistFormCheckboxes = $changelistForm.find('input[type=checkbox]')

  $changelistFormCheckboxes.on('change', function(e) {
    if ( $(this).is(':checked') ) {

      console.log('is checked');
    } else {

    }

    if ( $changelistFormCheckboxes.is(':checked') ) {
      console.log('at least one is checked');
      $changelistForm.find('.actions').slideDown()
    } else {
      console.log('none are checked');
      $changelistForm.find('.actions').slideUp()
    }
  })
});