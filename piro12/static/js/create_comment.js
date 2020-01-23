function submit_comment(url, data) {
    $.ajax({
        url: url,// 요청 할 주
        type:'POST', // GET, PUT
        data: {
            content:data
        },// 전송할 데이터
        dataType:'text',// xml, json, script, html
        success:function(response) {
            console.log(response)
            $('.comment_container').append(response)
            $('input[name=content]').val('')
        },// 요청 완료 시
        error:function(jqXHR) {
            console.log(jqXHR)
            alert('제대로 입력하시게나')
        },// 요청 실패.
    })
}
