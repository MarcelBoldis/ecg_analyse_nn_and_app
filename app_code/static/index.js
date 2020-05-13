$('#csv_file').change(function(e){
    const fileName = e.target.files[0].name;
    $('.custom-file-label').html(fileName);
});

function fileSize(elem){
    document.cookie = 'filesize=' + elem.files[0].size;
}

$(document).ready(
    function(){
        $('#subBtn').attr('disabled',true).css('cursor', 'not-allowed');
        $('input:file').change(
            function(){
                if ($(this).val()){
                    $('#subBtn').removeAttr('disabled').css('cursor', 'pointer');
                }
                else {
                    $('#subBtn').attr('disabled',true).css('cursor', 'not-allowed');
                }
            });
    });

function loading() {
    $("#load").show();
    $("#content").hide();
}