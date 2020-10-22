function fileSelect(id, e){
    var filename = e.target.files[0].name;
    console.log(filename)
    el = document.getElementById("arq-select");
  	$('#arq-select').html(filename);
};
