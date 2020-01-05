
function ordenar(tipo){
      switch(tipo){
            case 'id':
                  $("#Personajes div.Personaje").sort(function(a, b) {
                    return String.prototype.localeCompare.call($(a).attr("idp"), $(b).attr("idp"));
                  }).appendTo("#Personajes");
            break;
            case 'idrev':
                  $("#Personajes div.Personaje").sort(function(a, b) {
                    return String.prototype.localeCompare.call($(b).attr("idp"), $(a).attr("idp"));
                  }).appendTo("#Personajes");
            break;
            case 'apa':
                  $("#Personajes div.Personaje").sort(function(a, b) {
                    return $(a).attr("numapa") - $(b).attr("numapa");
                  }).appendTo("#Personajes");
            break;
            case 'aparev':
                  $("#Personajes div.Personaje").sort(function(a, b) {
                    return $(b).attr("numapa") - $(a).attr("numapa");
                  }).appendTo("#Personajes");
            break;
      }	
}