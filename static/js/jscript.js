$(function () {
    $("#upload-file-btn").click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/',
            data: form_data,
            contentType: false,
            cache: true,
            processData: false,
            async: true,
            success: function (data) {
                console.log('Success!');
            },
            complete: function (data) {
                var url_name=$("#name").val();
                $("#myImg").attr('src', 'static/uploads/'+url_name)
            }
        });
    });
});

$(function () {
    $("#process-type-btn").click(function () {
        //var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'GET',
            url: '/',
            success: function (data) {
                console.log('Success!');
            },
            complete: function (data) {
                console.log('complete ! ');
                $("#filtrer").attr('src', 'static/uploads/ImageFilter.png')
                $("#bruit").attr('src', 'static/uploads/Noise.png')
                $("#histogram").attr('src', 'static/uploads/Histogram.png')
            }
        });
    });
});