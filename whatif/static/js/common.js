function initAutoCompleteField(inputField, outputField, searchUrl, searchParam, 
  labelField, valueField, minLength, lastHolder) {

  $(inputField).autocomplete({
    source: function(request, response) {
      $.ajax({
        url: searchUrl+"?"+searchParam+"="+request.term,
        success: function(data) {
          console.log(data);
          response($.map(data, function(item) {
            return {
              id: item.id,
              label: item[labelField],
              value: item[valueField]
            }
          }));
        }
      });
    },
    select: function(event, ui) {
      if(ui.item) {
        $(inputField).val(ui.item.label);
        $(outputField).val(ui.item.id);
        lastHolder = ui.item.label;
      }
    },
    close: function(event, ui) {
      if(lastHolder) {
        $(inputField).val(lastHolder);
      }
    },
    minLength: minLength
  });
}